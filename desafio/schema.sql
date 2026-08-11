-- Arquivo gerado automaticamente por script de auto-detecção de schema

-- Destino: SQLite


CREATE TABLE IF NOT EXISTS addresses (
    id INTEGER,
    customer_id INTEGER,
    address_type TEXT,
    postal_code TEXT,
    street TEXT,
    number INTEGER,
    complement TEXT,
    district TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    is_primary INTEGER
);

CREATE TABLE IF NOT EXISTS attributes (
    id INTEGER,
    name TEXT,
    data_type TEXT
);

CREATE TABLE IF NOT EXISTS brands (
    id INTEGER,
    name TEXT,
    country TEXT,
    is_active INTEGER,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS categories (
    id INTEGER,
    name TEXT,
    slug TEXT,
    parent_category_id INTEGER,
    is_active INTEGER,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS customers (
    id INTEGER,
    person_type TEXT,
    legal_name TEXT,
    trade_name TEXT,
    tax_id INTEGER,
    state_registration TEXT,
    email TEXT,
    phone TEXT,
    is_active INTEGER,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS employees (
    id INTEGER,
    full_name TEXT,
    cpf INTEGER,
    email TEXT,
    role TEXT,
    primary_location_id INTEGER,
    hire_date TEXT,
    termination_date TEXT,
    is_active INTEGER,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS fiscal_invoices (
    id INTEGER,
    order_id INTEGER,
    nfe_number TEXT,
    nfe_access_key INTEGER,
    series INTEGER,
    issued_at TEXT,
    status TEXT,
    total_amount REAL,
    xml_storage_uri TEXT,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS goods_receipt_items (
    id INTEGER,
    goods_receipt_id INTEGER,
    purchase_order_item_id INTEGER,
    quantity_received REAL
);

CREATE TABLE IF NOT EXISTS goods_receipts (
    id INTEGER,
    purchase_order_id INTEGER,
    received_by_employee_id INTEGER,
    received_at TEXT,
    notes TEXT,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS locations (
    id INTEGER,
    name TEXT,
    location_type TEXT,
    postal_code TEXT,
    street TEXT,
    number INTEGER,
    complement TEXT,
    district TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    is_active INTEGER,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER,
    order_id INTEGER,
    product_variant_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    icms_rate REAL,
    ipi_rate REAL,
    line_total REAL
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER,
    order_number TEXT,
    channel TEXT,
    customer_id INTEGER,
    salesperson_id INTEGER,
    location_id INTEGER,
    status TEXT,
    subtotal REAL,
    discount_amount REAL,
    total REAL,
    placed_at TEXT,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS payments (
    id INTEGER,
    order_id INTEGER,
    method TEXT,
    installments INTEGER,
    amount REAL,
    status TEXT,
    paid_at TEXT,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS product_suppliers (
    product_variant_id INTEGER,
    supplier_id INTEGER,
    supplier_sku TEXT,
    last_quoted_cost REAL,
    lead_time_days INTEGER,
    is_preferred INTEGER,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS product_variants (
    id INTEGER,
    product_id INTEGER,
    sku TEXT,
    barcode_ean INTEGER,
    sale_price REAL,
    cost_price REAL,
    weight_kg REAL,
    icms_rate REAL,
    ipi_rate REAL,
    is_active INTEGER,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER,
    name TEXT,
    description TEXT,
    brand_id INTEGER,
    category_id INTEGER,
    ncm_code INTEGER,
    unit_of_measure TEXT,
    is_active INTEGER,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS purchase_order_items (
    id INTEGER,
    purchase_order_id INTEGER,
    product_variant_id INTEGER,
    quantity_ordered INTEGER,
    unit_cost REAL,
    line_total REAL
);

CREATE TABLE IF NOT EXISTS purchase_orders (
    id INTEGER,
    po_number TEXT,
    supplier_id INTEGER,
    buyer_id INTEGER,
    destination_location_id INTEGER,
    status TEXT,
    currency TEXT,
    subtotal REAL,
    total REAL,
    placed_at TEXT,
    expected_delivery_at TEXT,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS return_items (
    id INTEGER,
    return_id INTEGER,
    order_item_id INTEGER,
    quantity REAL,
    action TEXT,
    exchange_variant_id INTEGER,
    unit_refund_amount REAL
);

CREATE TABLE IF NOT EXISTS returns (
    id INTEGER,
    return_number TEXT,
    order_id INTEGER,
    customer_id INTEGER,
    received_at_location_id INTEGER,
    status TEXT,
    reason TEXT,
    total_refund_amount REAL,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS stock_levels (
    product_variant_id INTEGER,
    location_id INTEGER,
    quantity_on_hand REAL,
    reorder_point TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS stock_movements (
    id INTEGER,
    product_variant_id INTEGER,
    location_id INTEGER,
    movement_type TEXT,
    quantity REAL,
    reference_table TEXT,
    reference_id TEXT,
    employee_id TEXT,
    notes TEXT,
    occurred_at TEXT,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS suppliers (
    id INTEGER,
    legal_name TEXT,
    trade_name TEXT,
    country TEXT,
    tax_id TEXT,
    tax_id_type TEXT,
    email TEXT,
    phone INTEGER,
    contact_name TEXT,
    is_active INTEGER,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS variant_attribute_values (
    product_variant_id INTEGER,
    attribute_id INTEGER,
    value TEXT
);