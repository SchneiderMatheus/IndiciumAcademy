-- Arquivo gerado automaticamente por script de auto-detecção de schema

-- Destino: PostgreSQL


CREATE TABLE IF NOT EXISTS addresses (
    id INTEGER,
    customer_id INTEGER,
    address_type VARCHAR(255),
    postal_code VARCHAR(255),
    street VARCHAR(255),
    number INTEGER,
    complement VARCHAR(255),
    district VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    country VARCHAR(255),
    is_primary BOOLEAN
);

CREATE TABLE IF NOT EXISTS attributes (
    id INTEGER,
    name VARCHAR(255),
    data_type VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS brands (
    id INTEGER,
    name VARCHAR(255),
    country VARCHAR(255),
    is_active BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS categories (
    id INTEGER,
    name VARCHAR(255),
    slug VARCHAR(255),
    parent_category_id INTEGER,
    is_active BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS customers (
    id INTEGER,
    person_type VARCHAR(255),
    legal_name VARCHAR(255),
    trade_name VARCHAR(255),
    tax_id BIGINT,
    state_registration VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    is_active BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS employees (
    id INTEGER,
    full_name VARCHAR(255),
    cpf BIGINT,
    email VARCHAR(255),
    role VARCHAR(255),
    primary_location_id INTEGER,
    hire_date DATE,
    termination_date DATE,
    is_active BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS fiscal_invoices (
    id INTEGER,
    order_id INTEGER,
    nfe_number VARCHAR(255),
    nfe_access_key BIGINT,
    series INTEGER,
    issued_at TIMESTAMP,
    status VARCHAR(255),
    total_amount NUMERIC,
    xml_storage_uri VARCHAR(255),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS goods_receipt_items (
    id INTEGER,
    goods_receipt_id INTEGER,
    purchase_order_item_id INTEGER,
    quantity_received NUMERIC
);

CREATE TABLE IF NOT EXISTS goods_receipts (
    id INTEGER,
    purchase_order_id INTEGER,
    received_by_employee_id INTEGER,
    received_at TIMESTAMP,
    notes VARCHAR(255),
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS locations (
    id INTEGER,
    name VARCHAR(255),
    location_type VARCHAR(255),
    postal_code VARCHAR(255),
    street VARCHAR(255),
    number INTEGER,
    complement VARCHAR(255),
    district VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    country VARCHAR(255),
    is_active BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER,
    order_id INTEGER,
    product_variant_id INTEGER,
    quantity INTEGER,
    unit_price NUMERIC,
    icms_rate NUMERIC,
    ipi_rate NUMERIC,
    line_total NUMERIC
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER,
    order_number VARCHAR(255),
    channel VARCHAR(255),
    customer_id INTEGER,
    salesperson_id INTEGER,
    location_id INTEGER,
    status VARCHAR(255),
    subtotal NUMERIC,
    discount_amount NUMERIC,
    total NUMERIC,
    placed_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS payments (
    id INTEGER,
    order_id INTEGER,
    method VARCHAR(255),
    installments INTEGER,
    amount NUMERIC,
    status VARCHAR(255),
    paid_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS product_suppliers (
    product_variant_id INTEGER,
    supplier_id INTEGER,
    supplier_sku VARCHAR(255),
    last_quoted_cost NUMERIC,
    lead_time_days INTEGER,
    is_preferred BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS product_variants (
    id INTEGER,
    product_id INTEGER,
    sku VARCHAR(255),
    barcode_ean BIGINT,
    sale_price NUMERIC,
    cost_price NUMERIC,
    weight_kg NUMERIC,
    icms_rate NUMERIC,
    ipi_rate NUMERIC,
    is_active BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER,
    name VARCHAR(255),
    description VARCHAR(255),
    brand_id INTEGER,
    category_id INTEGER,
    ncm_code INTEGER,
    unit_of_measure VARCHAR(255),
    is_active BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS purchase_order_items (
    id INTEGER,
    purchase_order_id INTEGER,
    product_variant_id INTEGER,
    quantity_ordered INTEGER,
    unit_cost NUMERIC,
    line_total NUMERIC
);

CREATE TABLE IF NOT EXISTS purchase_orders (
    id INTEGER,
    po_number VARCHAR(255),
    supplier_id INTEGER,
    buyer_id INTEGER,
    destination_location_id INTEGER,
    status VARCHAR(255),
    currency VARCHAR(255),
    subtotal NUMERIC,
    total NUMERIC,
    placed_at TIMESTAMP,
    expected_delivery_at DATE,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS return_items (
    id INTEGER,
    return_id INTEGER,
    order_item_id INTEGER,
    quantity NUMERIC,
    action VARCHAR(255),
    exchange_variant_id INTEGER,
    unit_refund_amount NUMERIC
);

CREATE TABLE IF NOT EXISTS returns (
    id INTEGER,
    return_number VARCHAR(255),
    order_id INTEGER,
    customer_id INTEGER,
    received_at_location_id INTEGER,
    status VARCHAR(255),
    reason VARCHAR(255),
    total_refund_amount NUMERIC,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS stock_levels (
    product_variant_id INTEGER,
    location_id INTEGER,
    quantity_on_hand NUMERIC,
    reorder_point VARCHAR(255),
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS stock_movements (
    id INTEGER,
    product_variant_id INTEGER,
    location_id INTEGER,
    movement_type VARCHAR(255),
    quantity NUMERIC,
    reference_table VARCHAR(255),
    reference_id VARCHAR(255),
    employee_id VARCHAR(255),
    notes VARCHAR(255),
    occurred_at TIMESTAMP,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS suppliers (
    id INTEGER,
    legal_name VARCHAR(255),
    trade_name VARCHAR(255),
    country VARCHAR(255),
    tax_id VARCHAR(255),
    tax_id_type VARCHAR(255),
    email VARCHAR(255),
    phone BIGINT,
    contact_name VARCHAR(255),
    is_active BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS variant_attribute_values (
    product_variant_id INTEGER,
    attribute_id INTEGER,
    value VARCHAR(255)
);