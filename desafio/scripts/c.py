import csv
import os
from collections import defaultdict
from datetime import date


PRODUCT_NAME = "Bússola de Bordo 702"
TRAIN_END = date(2025, 12, 31)
TEST_MONTHS = [(2026, 1), (2026, 2), (2026, 3)]


def read_csv(filepath: str) -> list[dict]:
    with open(filepath, mode="r", encoding="utf-8-sig", errors="replace", newline="") as file:
        return list(csv.DictReader(file))


def month_key(year: int, month: int) -> str:
    return f"{year:04d}-{month:02d}"


def previous_months(year: int, month: int, periods: int = 3) -> list[tuple[int, int]]:
    months = []
    current_year = year
    current_month = month

    for _ in range(periods):
        current_month -= 1
        if current_month == 0:
            current_month = 12
            current_year -= 1
        months.append((current_year, current_month))

    months.reverse()
    return months


def build_unified_dataset(base_dir: str) -> dict[str, float]:
    products = read_csv(os.path.join(base_dir, "products.csv"))
    product_variants = read_csv(os.path.join(base_dir, "product_variants.csv"))
    orders = read_csv(os.path.join(base_dir, "orders.csv"))
    order_items = read_csv(os.path.join(base_dir, "order_items.csv"))

    product_id = None
    for product in products:
        if product["name"] == PRODUCT_NAME:
            product_id = product["id"]
            break

    if product_id is None:
        raise ValueError(f"Produto '{PRODUCT_NAME}' não encontrado em products.csv.")

    variant_ids = {
        variant["id"]
        for variant in product_variants
        if variant["product_id"] == product_id
    }

    orders_by_id = {order["id"]: order for order in orders}
    monthly_sales = defaultdict(float)

    for item in order_items:
        if item["product_variant_id"] not in variant_ids:
            continue

        order = orders_by_id.get(item["order_id"])
        if not order:
            continue

        year, month, _ = map(int, order["created_at"].split(" ")[0].split("-"))
        monthly_sales[month_key(year, month)] += float(item["quantity"] or 0)

    return dict(sorted(monthly_sales.items()))


def moving_average_forecast(monthly_sales: dict[str, float]) -> list[dict]:
    forecasts = []

    for year, month in TEST_MONTHS:
        history_months = previous_months(year, month, periods=3)
        history_keys = [month_key(hist_year, hist_month) for hist_year, hist_month in history_months]
        history_values = [monthly_sales.get(hist_key, 0.0) for hist_key in history_keys]

        prediction = sum(history_values) / 3
        actual = monthly_sales.get(month_key(year, month), 0.0)
        absolute_error = abs(actual - prediction)

        forecasts.append(
            {
                "mes_referencia": month_key(year, month),
                "historico_utilizado": ", ".join(history_keys),
                "valor_real": actual,
                "previsao": round(prediction, 2),
                "erro_absoluto": round(absolute_error, 2),
            }
        )

    return forecasts


def calculate_mae(forecasts: list[dict]) -> float:
    if not forecasts:
        return 0.0
    return round(sum(item["erro_absoluto"] for item in forecasts) / len(forecasts), 2)


def print_results(monthly_sales: dict[str, float], forecasts: list[dict], mae: float) -> None:
    print(f"Produto analisado: {PRODUCT_NAME}")
    print(f"Fim do treino: {TRAIN_END}")
    print("Periodo de teste: 2026-01 a 2026-03\n")

    print("Base mensal unificada:")
    for month, quantity in monthly_sales.items():
        if month.startswith("2025") or month.startswith("2026"):
            print(f"{month}: {quantity}")

    print("\nPrevisoes do baseline (media movel de 3 meses):")
    for forecast in forecasts:
        print(
            f"{forecast['mes_referencia']} | historico: {forecast['historico_utilizado']} "
            f"| real: {forecast['valor_real']} | previsao: {forecast['previsao']} "
            f"| erro_absoluto: {forecast['erro_absoluto']}"
        )

    print(f"\nMAE: {mae}")


def main() -> None:
    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "1-lh_nautical_csv")
    )
    monthly_sales = build_unified_dataset(base_dir)
    forecasts = moving_average_forecast(monthly_sales)
    mae = calculate_mae(forecasts)
    print_results(monthly_sales, forecasts, mae)


if __name__ == "__main__":
    main()
