import csv
import math
import os
from collections import defaultdict


PRODUCT_NAME = "Motor de Popa 1949"


def read_csv(filepath: str) -> list[dict]:
    with open(filepath, mode="r", encoding="utf-8-sig", errors="replace", newline="") as file:
        return list(csv.DictReader(file))


def load_data(base_dir: str) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    products = read_csv(os.path.join(base_dir, "products.csv"))
    product_variants = read_csv(os.path.join(base_dir, "product_variants.csv"))
    orders = read_csv(os.path.join(base_dir, "orders.csv"))
    order_items = read_csv(os.path.join(base_dir, "order_items.csv"))
    return products, product_variants, orders, order_items


def build_user_item_matrix(
    products: list[dict],
    product_variants: list[dict],
    orders: list[dict],
    order_items: list[dict],
) -> tuple[dict[str, dict[str, int]], dict[str, str], dict[str, set[str]]]:
    product_names = {product["id"]: product["name"] for product in products}
    variant_to_product = {
        variant["id"]: variant["product_id"] for variant in product_variants
    }
    order_to_customer = {
        order["id"]: order["customer_id"]
        for order in orders
        if order.get("customer_id")
    }

    customer_products = defaultdict(set)
    for item in order_items:
        customer_id = order_to_customer.get(item["order_id"])
        if not customer_id:
            continue

        product_id = variant_to_product.get(item["product_variant_id"])
        if not product_id:
            continue

        customer_products[customer_id].add(product_id)

    user_item_matrix = {}
    for customer_id, product_ids in customer_products.items():
        user_item_matrix[customer_id] = {
            product_id: 1 for product_id in product_ids
        }

    product_customers = defaultdict(set)
    for customer_id, product_ids in customer_products.items():
        for product_id in product_ids:
            product_customers[product_id].add(customer_id)

    return user_item_matrix, product_names, product_customers


def cosine_similarity(
    product_a_customers: set[str], product_b_customers: set[str]
) -> float:
    if not product_a_customers or not product_b_customers:
        return 0.0

    intersection = len(product_a_customers.intersection(product_b_customers))
    denominator = math.sqrt(len(product_a_customers) * len(product_b_customers))
    if denominator == 0:
        return 0.0

    return intersection / denominator


def rank_similar_products(
    products: list[dict], product_names: dict[str, str], product_customers: dict[str, set[str]]
) -> list[tuple[str, str, float]]:
    reference_product_id = None
    for product in products:
        if product["name"] == PRODUCT_NAME:
            reference_product_id = product["id"]
            break

    if reference_product_id is None:
        raise ValueError(f"Produto '{PRODUCT_NAME}' não encontrado.")

    reference_customers = product_customers.get(reference_product_id, set())
    ranking = []

    for product_id, customers in product_customers.items():
        if product_id == reference_product_id:
            continue

        similarity = cosine_similarity(reference_customers, customers)
        ranking.append((product_id, product_names.get(product_id, "NAO INFORMADO"), similarity))

    ranking.sort(key=lambda item: (-item[2], int(item[0])))
    return ranking[:5]


def main() -> None:
    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "1-lh_nautical_csv")
    )
    products, product_variants, orders, order_items = load_data(base_dir)
    user_item_matrix, product_names, product_customers = build_user_item_matrix(
        products, product_variants, orders, order_items
    )
    ranking = rank_similar_products(products, product_names, product_customers)

    print(f"Produto de referencia: {PRODUCT_NAME}")
    print(f"Clientes na matriz: {len(user_item_matrix)}")
    print(f"Produtos na matriz: {len(product_customers)}\n")
    print("Top 5 produtos mais similares:")
    for product_id, product_name, similarity in ranking:
        print(f"{product_id} | {product_name} | similaridade={similarity:.6f}")


if __name__ == "__main__":
    main()
