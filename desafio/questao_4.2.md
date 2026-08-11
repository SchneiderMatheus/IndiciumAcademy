## Questão 4.2

Para chegar nas categorias mais vendidas, eu fiz o mapeamento a partir da cadeia de relacionamento entre as tabelas. Primeiro usei a tabela `orders` para identificar os pedidos de cada cliente. Depois relacionei com `order_items`, que mostra os itens comprados em cada pedido. A partir daí, liguei com `product_variants`, depois com `products` e por fim com `categories`, que é onde está a categoria de cada produto. Em resumo, a cadeia usada foi: `orders -> order_items -> product_variants -> products -> categories`.

A lógica para filtrar os clientes com diversidade mínima foi contar quantas categorias diferentes cada cliente comprou. Para isso, considerei `COUNT(DISTINCT p.category_id)` agrupando por `customer_id`. Depois apliquei o filtro para manter apenas os clientes com `13` ou mais categorias distintas, como a questão pedia.

Para garantir que a contagem de itens refletisse somente os Top 10, primeiro criei um conjunto com esses 10 clientes já filtrados e ordenados pelo maior ticket médio. Só depois disso fiz a soma da quantidade de itens (`SUM(quantity)`) por categoria. Assim, a contagem final considerou apenas pedidos pertencentes a esse grupo específico de clientes, e não da base inteira.
