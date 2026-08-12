## Guia prático da Questão 3 no DBeaver

Aqui a ideia é entender o caminho manual mais simples para criar as tabelas no PostgreSQL e importar os CSVs no DBeaver.

### Visão geral

O processo inteiro pode ser dividido em 4 etapas:

1. Criar um banco PostgreSQL
2. Rodar o `schema.sql` para criar as tabelas
3. Importar os CSVs para dentro dessas tabelas
4. Validar se os dados foram carregados corretamente

---

## 1. Criar o banco no PostgreSQL

Se você já tiver uma conexão PostgreSQL no DBeaver:

1. Abra o DBeaver
2. No painel esquerdo, clique com o botão direito na sua conexão PostgreSQL
3. Vá em `Create`
4. Clique em `Database`
5. Dê um nome para o banco, por exemplo: `lh_nautical`
6. Confirme

Se você ainda não tiver uma conexão PostgreSQL:

1. Clique em `New Database Connection`
2. Escolha `PostgreSQL`
3. Preencha host, porta, nome do banco, usuário e senha
4. Clique em `Test Connection`
5. Se estiver tudo certo, finalize

---

## 2. Abrir o banco correto

Depois de criar o banco:

1. Expanda a conexão PostgreSQL no painel esquerdo
2. Encontre o banco `lh_nautical`
3. Clique nele
4. Abra um `SQL Editor` conectado a esse banco

Esse ponto é importante porque o `schema.sql` precisa ser executado no banco certo.

---

## 3. Criar as tabelas com o schema.sql

Agora você vai usar o arquivo gerado na Questão 2.

Arquivo:

- `schema.sql`

Passo a passo:

1. Abra o arquivo `schema.sql`
2. Copie o conteúdo inteiro
3. Cole no editor SQL do DBeaver
4. Execute tudo

Se der certo, o PostgreSQL vai criar tabelas como:

- `orders`
- `customers`
- `products`
- `product_variants`
- `order_items`
- `payments`
- e as demais tabelas da base

Para conferir:

1. Vá no painel esquerdo
2. Encontre a pasta `Tables`
3. Clique com o botão direito
4. Escolha `Refresh`

Se tudo estiver certo, as tabelas vão aparecer.

---

## 4. Importar os CSVs manualmente

Agora começa a carga manual dos dados.

A lógica é simples:

- cada arquivo CSV deve ser importado para a tabela com o mesmo nome

Exemplos:

- `orders.csv` vai para a tabela `orders`
- `customers.csv` vai para a tabela `customers`
- `products.csv` vai para a tabela `products`
- `order_items.csv` vai para a tabela `order_items`

---

## 5. Exemplo prático de importação no DBeaver

Vou usar `orders.csv` como exemplo.

### Importando `orders.csv`

1. No DBeaver, encontre a tabela `orders`
2. Clique com o botão direito nela
3. Clique em `Import Data`
4. Escolha a opção `CSV`
5. Selecione o arquivo `1-lh_nautical_csv/orders.csv`
6. Clique em avançar

Agora confira com atenção:

- o separador deve ser `,`
- a primeira linha deve estar marcada como cabeçalho
- o encoding deve estar como `UTF-8`

Depois:

1. Avance até a tela de mapeamento
2. Verifique se as colunas do CSV estão batendo com as colunas da tabela
3. Se estiver tudo certo, conclua a importação

Se der certo, a tabela `orders` vai receber os dados do arquivo.

---

## 6. Repetir para os demais arquivos

Você vai repetir esse mesmo processo para todos os CSVs.

Exemplos:

- `customers.csv` -> `customers`
- `products.csv` -> `products`
- `product_variants.csv` -> `product_variants`
- `order_items.csv` -> `order_items`
- `payments.csv` -> `payments`

---

## 7. Ordem prática de importação

Como o schema gerado não criou chaves estrangeiras explícitas, em teoria a ordem não trava a importação.

Mesmo assim, para ficar mais organizado, uma ordem prática seria:

1. `categories`
2. `brands`
3. `customers`
4. `employees`
5. `locations`
6. `suppliers`
7. `attributes`
8. `products`
9. `product_variants`
10. `variant_attribute_values`
11. `product_suppliers`
12. `orders`
13. `order_items`
14. `payments`
15. `purchase_orders`
16. `purchase_order_items`
17. `goods_receipts`
18. `goods_receipt_items`
19. `returns`
20. `return_items`
21. `stock_levels`
22. `stock_movements`
23. `fiscal_invoices`
24. `addresses`

---

## 8. Como validar se a carga funcionou

Depois de importar uma tabela, o ideal é validar com uma consulta simples.

Exemplo:

```sql
SELECT COUNT(*) FROM orders;
```

Para conferir várias tabelas de uma vez:

```sql
SELECT 'customers' AS tabela, COUNT(*) AS total FROM customers
UNION ALL
SELECT 'orders', COUNT(*) FROM orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM order_items
UNION ALL
SELECT 'payments', COUNT(*) FROM payments;
```

Os valores esperados são:

- `customers`: 2000
- `orders`: 48998
- `order_items`: 147320
- `payments`: 53546

Se esses números baterem, a carga dessas tabelas está correta.

---

## 9. Erros comuns

Se algo der errado, normalmente é por um destes motivos:

- o arquivo foi importado no banco errado
- você abriu uma conexão SQLite em vez de PostgreSQL
- a tabela ainda não existia antes da importação
- a primeira linha do CSV não foi marcada como cabeçalho
- o separador ficou errado
- o CSV foi importado na tabela errada

---

## 10. Onde entra o script `b.py`

O arquivo `scripts/b.py` foi criado para fazer essa carga automaticamente.

Ele:

- conecta no PostgreSQL
- lê todos os CSVs
- carrega os arquivos nas tabelas correspondentes

Ou seja:

- o processo manual no DBeaver serve para você entender melhor o funcionamento
- o script `b.py` serve para automatizar esse trabalho

---

## 11. Resumindo de forma bem prática

Se quiser pensar no fluxo da forma mais simples possível, é isso:

1. Criar o banco PostgreSQL
2. Rodar o `schema.sql`
3. Pegar cada CSV e importar na tabela com o mesmo nome
4. Rodar `COUNT(*)` para confirmar que os dados entraram

---

## 12. Arquivos importantes

Os principais arquivos dessa etapa são:

- `schema.sql`
- `scripts/b.py`
- pasta `1-lh_nautical_csv`

---

## 13. Dica final

Se você quiser praticar primeiro com uma tabela só, o melhor caminho é começar por:

1. `orders`
2. `order_items`
3. `customers`
4. `payments`

Porque são as tabelas mais usadas ao longo do desafio e já ajudam bastante a entender como a importação funciona.
