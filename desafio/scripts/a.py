import csv
import glob
import os
import re
import sys
from datetime import datetime


def sanitize_identifier(name: str) -> str:
    """Sanitiza nome de arquivo ou coluna para identificador válido no PostgreSQL."""
    # Remove a extensão se houver
    name = os.path.splitext(name)[0]
    # Substitui caracteres não alfanuméricos por underline
    sanitized = re.sub(r"\W+", "_", name.strip())
    # Remove underlines duplicados e ajusta para minúsculas
    sanitized = re.sub(r"_", "_", sanitized).strip("_").lower()
    # Se começar com número, adiciona um prefixo
    if sanitized and sanitized[0].isdigit():
        sanitized = f"tbl_{sanitized}"
    return sanitized or "coluna_desconhecida"


def infer_type(value: str) -> str:
    """Infere um tipo intermediário a partir de um valor individual."""
    val = value.strip()

    if not val:
        return "UNKNOWN"

    # Integer / Bigint
    if re.match(r"^-?\d+$", val):
        num = int(val)
        if -2147483648 <= num <= 2147483647:
            return "INTEGER"
        return "BIGINT"

    # Boolean textual
    if val.lower() in ("true", "false", "t", "f"):
        return "BOOLEAN"

    # Numeric / Float
    # Aceita ponto decimal ou vírgula
    if re.match(r"^-?\d+[\.,]\d+$", val):
        return "NUMERIC"

    # Data e Timestamp (testa formatos comuns)
    date_formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%Y/%m/%d",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%d/%m/%Y %H:%M:%S",
    ]

    for fmt in date_formats:
        try:
            datetime.strptime(val, fmt)
            if " " in val or "T" in val:
                return "TIMESTAMP"
            return "DATE"
        except ValueError:
            pass

    # Texto com tamanho
    length = len(val)
    if length <= 255:
        return "VARCHAR(255)"
    return "TEXT"


def promote_type(current_type: str, new_type: str) -> str:
    """Promove o tipo de dado da coluna considerando hierarquia de compatibilidade.

    Evita perda de dados ao analisar múltiplas linhas.
    """
    if current_type == "UNKNOWN":
        return new_type
    if new_type == "UNKNOWN" or current_type == new_type:
        return current_type

    # Regras de promoção
    hierarchy = {
        "BOOLEAN": 1,
        "INTEGER": 2,
        "BIGINT": 3,
        "NUMERIC": 4,
        "DATE": 5,
        "TIMESTAMP": 6,
        "VARCHAR(255)": 7,
        "TEXT": 8,
    }

    # Tratamento especial para números x texto
    if current_type in (
        "INTEGER",
        "BIGINT",
        "NUMERIC",
    ) and new_type in ("INTEGER", "BIGINT", "NUMERIC"):
        order = ["INTEGER", "BIGINT", "NUMERIC"]
        return order[max(order.index(current_type), order.index(new_type))]

    # Tratamento especial para data x timestamp
    if current_type in ("DATE", "TIMESTAMP") and new_type in (
        "DATE",
        "TIMESTAMP",
    ):
        return "TIMESTAMP"

    # Se houver divergência entre tipos incompatíveis (ex: INTEGER e DATE), cai para VARCHAR/TEXT
    type1_rank = hierarchy.get(current_type, 8)
    type2_rank = hierarchy.get(new_type, 8)

    max_rank = max(type1_rank, type2_rank)
    if max_rank <= 7:
        return "VARCHAR(255)"
    return "TEXT"


def analyze_csv(filepath: str, max_rows: int = 5000) -> dict:
    """Lê o arquivo CSV, detecta o delimitador e infere os tipos de cada coluna."""
    table_name = sanitize_identifier(os.path.basename(filepath))

    with open(filepath, mode="r", encoding="utf-8-sig", errors="replace") as f:
        # Detecta delimitador (vírgula ou ponto e vírgula)
        sample = f.read(2048)
        f.seek(0)
        delimiter = ";" if sample.count(";") > sample.count(",") else ","

        reader = csv.reader(f, delimiter=delimiter)

        try:
            headers = next(reader)
        except StopIteration:
            return None  # Arquivo vazio

        sanitized_headers = [sanitize_identifier(h) for h in headers]
        column_types = {col: "UNKNOWN" for col in sanitized_headers}

        row_count = 0
        for row in reader:
            if row_count >= max_rows:
                break
            for idx, cell in enumerate(row):
                if idx < len(sanitized_headers):
                    col_name = sanitized_headers[idx]
                    inferred = infer_type(cell)
                    column_types[col_name] = promote_type(
                        column_types[col_name], inferred
                    )
            row_count += 1

    # Substitui UNKNOWN remanescentes (colunas sem dados/nulas) por VARCHAR(255)
    for col, dtype in column_types.items():
        if dtype == "UNKNOWN":
            column_types[col] = "VARCHAR(255)"

    return {"table_name": table_name, "columns": column_types}


def generate_schema(
    input_dir: str = ".", output_file: str = "schema.sql"
) -> None:
    """Busca todos os arquivos CSV do diretório e escreve a DDL PostgreSQL."""
    input_dir = os.path.abspath(input_dir)
    output_file = os.path.abspath(output_file)
    csv_files = glob.glob(os.path.join(input_dir, "*.csv"))

    if not csv_files:
        print(f"Nenhum arquivo .csv encontrado no diretório: {input_dir}")
        return

    sql_statements = [
        "-- Arquivo gerado automaticamente por script de auto-detecção de schema",
        "-- Destino: PostgreSQL\n",
    ]

    for filepath in sorted(csv_files):
        print(f"Analisando: {os.path.basename(filepath)}...")
        schema_info = analyze_csv(filepath)

        if not schema_info or not schema_info["columns"]:
            continue

        table_name = schema_info["table_name"]
        columns_ddl = []

        for col_name, col_type in schema_info["columns"].items():
            columns_ddl.append(f"    {col_name} {col_type}")

        ddl = f"CREATE TABLE IF NOT EXISTS {table_name} (\n"
        ddl += ",\n".join(columns_ddl)
        ddl += "\n);"

        sql_statements.append(ddl)

    # Escreve o resultado no arquivo final
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(sql_statements))

    print(f"\nSucesso! O arquivo DDL '{output_file}' foi gerado.")


if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    default_input_dir = os.path.join(base_dir, "1-lh_nautical_csv")
    default_output_file = os.path.join(base_dir, "schema.sql")

    input_dir = sys.argv[1] if len(sys.argv) > 1 else default_input_dir
    output_file = sys.argv[2] if len(sys.argv) > 2 else default_output_file

    generate_schema(input_dir=input_dir, output_file=output_file)
