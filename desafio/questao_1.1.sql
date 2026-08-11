SELECT
    COUNT(*) AS total_linhas,
    MIN(created_at) AS data_minima,
    MAX(created_at) AS data_maxima,
    MIN(total) AS valor_minimo,
    MAX(total) AS valor_maximo,
    ROUND(AVG(total), 2) AS valor_medio
FROM orders;
/*
48998	2020-01-01 01:19:28	2026-12-31 23:43:09	1000.77	9997.50	28704.99 
*/