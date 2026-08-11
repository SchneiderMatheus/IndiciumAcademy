select 
    count(*) as total_linhas,
    min(created_at) as data_minima,
    max(created_at) as data_maxima
from orders;

/* 
+--------------+---------------------+---------------------+
| total_linhas | data_minima         | data_maxima         |
+--------------+---------------------+---------------------+
|        48998 | 2020-01-01 01:19:28 | 2026-12-31 23:43:09 |
+--------------+---------------------+---------------------+ 
*/

select 
    count(*) as total_colunas
from information_schema.columns
where table_name = 'orders';

/* 
+---------------+
| total_colunas |
+---------------+
|            13 |
+---------------+
*/

select 
    min(total) as valor_minimo,
    max(total) as valor_maximo,
    round(avg(total), 2) as valor_medio
from orders;
/*
+--------------+--------------+-------------+
| valor_minimo | valor_maximo | valor_medio |
+--------------+--------------+-------------+
|        32.62 |    127262.02 |    28704.99 |
+--------------+--------------+-------------+
1 row in set (0.01 sec)
*/

select 
    count(*) as total_linhas,
    min(created_at) as data_minima,
    max(created_at) as data_maxima,
    min(total) as valor_minimo,
    max(total) as valor_maximo,
    round(avg(total), 2) as valor_medio
from orders;

/*
+--------------+---------------------+---------------------+--------------+--------------+-------------+
| total_linhas | data_minima         | data_maxima         | valor_minimo | valor_maximo | valor_medio |
+--------------+---------------------+---------------------+--------------+--------------+-------------+
|        48998 | 2020-01-01 01:19:28 | 2026-12-31 23:43:09 |        32.62 |    127262.02 |    28704.99 |
+--------------+---------------------+---------------------+--------------+--------------+-------------+
1 row in set (0.02 sec)
*/
