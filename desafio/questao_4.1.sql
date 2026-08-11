WITH customer_metrics AS (
    SELECT
        o.customer_id,
        SUM(o.total) AS faturamento_total,
        COUNT(DISTINCT o.id) AS frequencia,
        ROUND(SUM(o.total) / COUNT(DISTINCT o.id), 2) AS ticket_medio,
        COUNT(DISTINCT p.category_id) AS diversidade_categorias
    FROM orders o
    JOIN order_items oi
        ON oi.order_id = o.id
    JOIN product_variants pv
        ON pv.id = oi.product_variant_id
    JOIN products p
        ON p.id = pv.product_id
    WHERE o.customer_id IS NOT NULL
    GROUP BY o.customer_id
),
top_10_clientes_fieis AS (
    SELECT
        customer_id,
        faturamento_total,
        frequencia,
        ticket_medio,
        diversidade_categorias
    FROM customer_metrics
    WHERE diversidade_categorias >= 13
    ORDER BY ticket_medio DESC, customer_id ASC
    LIMIT 10
)
SELECT
    customer_id,
    faturamento_total,
    frequencia,
    ticket_medio,
    diversidade_categorias
FROM top_10_clientes_fieis;

/*
customer_id | faturamento_total | frequencia | ticket_medio | diversidade_categorias
22          | 1087838.44        | 26         | 41839.94     | 14
1477        | 916262.58         | 22         | 41648.30     | 14
929         | 1082775.89        | 26         | 41645.23     | 14
1116        | 655737.20         | 16         | 40983.57     | 14
1691        | 815471.30         | 20         | 40773.57     | 14
774         | 726127.99         | 18         | 40340.44     | 14
1470        | 1040553.09        | 26         | 40021.27     | 14
1599        | 997616.46         | 25         | 39904.66     | 14
965         | 677297.78         | 17         | 39841.05     | 14
1722        | 1146455.22        | 29         | 39532.94     | 14
*/
