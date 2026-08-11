WITH calendario AS (
    SELECT
        generate_series(
            (SELECT MIN(created_at::date) FROM orders),
            (SELECT MAX(created_at::date) FROM orders),
            INTERVAL '1 day'
        )::date AS data_calendario
),
vendas_pos_diarias AS (
    SELECT
        created_at::date AS data_venda,
        SUM(total) AS valor_venda
    FROM orders
    WHERE channel = 'pos'
    GROUP BY created_at::date
)
SELECT
    c.data_calendario,
    CASE EXTRACT(ISODOW FROM c.data_calendario)
        WHEN 1 THEN 'Segunda-feira'
        WHEN 2 THEN 'Terça-feira'
        WHEN 3 THEN 'Quarta-feira'
        WHEN 4 THEN 'Quinta-feira'
        WHEN 5 THEN 'Sexta-feira'
        WHEN 6 THEN 'Sábado'
        WHEN 7 THEN 'Domingo'
    END AS dia_semana,
    COALESCE(v.valor_venda, 0) AS valor_venda
FROM calendario c
LEFT JOIN vendas_pos_diarias v
    ON v.data_venda = c.data_calendario
ORDER BY c.data_calendario;
