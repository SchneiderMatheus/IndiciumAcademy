import csv
import glob
import os
import re
import sys
""" O script b.py foi criado para carregar todos os arquivos CSV no banco PostgreSQL a partir do schema
  definido na etapa anterior. Ele lê automaticamente todos os arquivos do diretório 1-lh_nautical_csv,
  Para isso, o script usa uma conexão com o PostgreSQL via DATABASE_URL e executa a carga com COPY,
  que é uma forma mais apropriada para importar arquivos CSV. A lógica foi feita para carregar todos
  formulário"""

def sanitize_identifier(name: str) -> str:
    """Sanitiza nome de arquivo ou coluna para identificador válido no PostgreSQL."""
    name = os.path.splitext(name)[0]
    sanitized = re.sub(r"\W+", "_", name.strip())
    sanitized = re.sub(r"_+", "_", sanitized).strip("_").lower()
    if sanitized and sanitized[0].isdigit():
        sanitized = f"tbl_{sanitized}"
    return sanitized or "coluna_desconhecida"


def detect_delimiter(filepath: str) -> str:
    with open(filepath, mode="r", encoding="utf-8-sig", errors="replace") as file:
        sample = file.read(2048)
    return ";" if sample.count(";") > sample.count(",") else ","


def get_csv_headers(filepath: str, delimiter: str) -> list[str]:
    with open(filepath, mode="r", encoding="utf-8-sig", errors="replace") as file:
        reader = csv.reader(file, delimiter=delimiter)
        try:
            headers = next(reader)
        except StopIteration:
            return []
    return [sanitize_identifier(header) for header in headers]


def get_connection():
    """Cria conexão PostgreSQL usando psycopg ou psycopg2."""
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError(
            "Defina a variável de ambiente DATABASE_URL com a conexão PostgreSQL."
        )

    try:
        import psycopg

        return psycopg.connect(database_url), "psycopg"
    except ImportError:
        try:
            import psycopg2

            return psycopg2.connect(database_url), "psycopg2"
        except ImportError as exc:
            raise RuntimeError(
                "Instale psycopg ou psycopg2 para executar a carga dos CSVs."
            ) from exc


def truncate_table(cursor, table_name: str) -> None:
    cursor.execute(f"TRUNCATE TABLE {table_name};")


def copy_with_psycopg(cursor, filepath: str, table_name: str, columns: list[str]) -> None:
    delimiter = detect_delimiter(filepath)
    copy_sql = (
        f"COPY {table_name} ({', '.join(columns)}) "
        f"FROM STDIN WITH (FORMAT CSV, HEADER TRUE, DELIMITER '{delimiter}')"
    )

    with open(filepath, mode="r", encoding="utf-8-sig", errors="replace") as file:
        with cursor.copy(copy_sql) as copy:
            while True:
                chunk = file.read(65536)
                if not chunk:
                    break
                copy.write(chunk)


def copy_with_psycopg2(cursor, filepath: str, table_name: str, columns: list[str]) -> None:
    delimiter = detect_delimiter(filepath)
    copy_sql = (
        f"COPY {table_name} ({', '.join(columns)}) "
        f"FROM STDIN WITH CSV HEADER DELIMITER '{delimiter}'"
    )

    with open(filepath, mode="r", encoding="utf-8-sig", errors="replace") as file:
        cursor.copy_expert(copy_sql, file)


def load_csv_file(cursor, driver_name: str, filepath: str) -> None:
    table_name = sanitize_identifier(os.path.basename(filepath))
    delimiter = detect_delimiter(filepath)
    columns = get_csv_headers(filepath, delimiter)

    if not columns:
        print(f"Pulando arquivo vazio: {os.path.basename(filepath)}")
        return

    print(f"Carregando: {os.path.basename(filepath)} -> {table_name}")
    truncate_table(cursor, table_name)

    if driver_name == "psycopg":
        copy_with_psycopg(cursor, filepath, table_name, columns)
    else:
        copy_with_psycopg2(cursor, filepath, table_name, columns)


def load_all_csvs(input_dir: str) -> None:
    input_dir = os.path.abspath(input_dir)
    csv_files = sorted(glob.glob(os.path.join(input_dir, "*.csv")))

    if not csv_files:
        print(f"Nenhum arquivo .csv encontrado no diretório: {input_dir}")
        return

    connection, driver_name = get_connection()

    try:
        with connection:
            with connection.cursor() as cursor:
                for filepath in csv_files:
                    load_csv_file(cursor, driver_name, filepath)
    finally:
        connection.close()

    print("\nCarga concluída com sucesso.")


if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    default_input_dir = os.path.join(base_dir, "1-lh_nautical_csv")
    input_dir = sys.argv[1] if len(sys.argv) > 1 else default_input_dir
    load_all_csvs(input_dir)
