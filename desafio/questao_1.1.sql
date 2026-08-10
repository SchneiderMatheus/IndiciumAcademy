SELECT 
    COUNT(*) AS total_linhas,
    MIN(created_at) AS data_minima,
    MAX(created_at) AS data_maxima
FROM orders;

/* 
+--------------+---------------------+---------------------+
| total_linhas | data_minima         | data_maxima         |
+--------------+---------------------+---------------------+
|        48998 | 2020-01-01 01:19:28 | 2026-12-31 23:43:09 |
+--------------+---------------------+---------------------+ 
*/

SELECT COUNT(*) AS total_colunas
FROM information_schema.columns
WHERE table_name = 'orders';

/* 
+---------------+
| total_colunas |
+---------------+
|            13 |
+---------------+
*/

SELECT 
    MIN(total) AS valor_minimo,
    MAX(total) AS valor_maximo,
    ROUND(AVG(total), 2) AS valor_medio
FROM orders;
/*
+--------------+--------------+-------------+
| valor_minimo | valor_maximo | valor_medio |
+--------------+--------------+-------------+
|        32.62 |    127262.02 |    28704.99 |
+--------------+--------------+-------------+
1 row in set (0.01 sec)
*/

SELECT 
    COUNT(*) AS total_linhas,
    MIN(created_at) AS data_minima,
    MAX(created_at) AS data_maxima,
    MIN(total) AS valor_minimo,
    MAX(total) AS valor_maximo,
    ROUND(AVG(total), 2) AS valor_medio
FROM orders;

/*
+--------------+---------------------+---------------------+--------------+--------------+-------------+
| total_linhas | data_minima         | data_maxima         | valor_minimo | valor_maximo | valor_medio |
+--------------+---------------------+---------------------+--------------+--------------+-------------+
|        48998 | 2020-01-01 01:19:28 | 2026-12-31 23:43:09 |        32.62 |    127262.02 |    28704.99 |
+--------------+---------------------+---------------------+--------------+--------------+-------------+
1 row in set (0.02 sec)
*/

