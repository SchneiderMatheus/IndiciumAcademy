# Leitura da Atividade

Este arquivo resume, de forma organizada, tudo o que foi desenvolvido nesta atividade do desafio `lh_nautical`.

## 1. Entendimento inicial da base

O trabalho foi feito a partir dos arquivos CSV da pasta `1-lh_nautical_csv`. A base contém informações de clientes, pedidos, itens dos pedidos, produtos, variantes, pagamentos, estoque, fornecedores e outras entidades do negócio.

O primeiro passo prático foi entender a estrutura geral dos dados e identificar como as tabelas se relacionam entre si. Isso foi importante porque as respostas posteriores dependem diretamente desses relacionamentos.

## 2. Questão 1: análise exploratória inicial

Na questão 1 foi feita uma consulta simples sobre a tabela `orders` para levantar métricas básicas da base:

- total de linhas
- data mínima e máxima
- valor mínimo e máximo
- valor médio dos pedidos

Essa etapa serviu para validar o volume do dataset e entender a janela temporal de análise.

Arquivo relacionado:

- `questao_1.1.sql`

## 3. Questão 2: geração automática do schema

Depois da leitura inicial, foi criado um processo para transformar os CSVs em uma estrutura de tabelas compatível com PostgreSQL.

O script `script1.py` faz isso automaticamente:

- percorre os arquivos CSV
- detecta delimitador
- lê cabeçalhos
- sanitiza nomes de tabelas e colunas
- infere tipos de dados
- promove tipos quando encontra valores diferentes na mesma coluna
- gera o arquivo final `schema.sql`

O resultado dessa etapa foi um schema com `CREATE TABLE IF NOT EXISTS` para todas as tabelas da base.

Arquivos relacionados:

- `scripts/script1.py`
- `schema.sql`

## 4. Questão 3: carga dos dados no PostgreSQL

Com o schema pronto, a próxima etapa foi preparar a carga dos CSVs no banco.

Foram produzidos dois caminhos:

1. Um guia manual no DBeaver, explicando como:
   - criar o banco
   - executar o `schema.sql`
   - importar cada CSV
   - validar a carga com `COUNT(*)`

2. Um script automatizado de carga, `script2.py`, que:
   - lê todos os CSVs da pasta
   - identifica o nome correto da tabela
   - detecta o delimitador
   - lê os cabeçalhos
   - conecta ao PostgreSQL via `DATABASE_URL`
   - usa `COPY` para importar os dados
   - faz `TRUNCATE` antes da carga de cada tabela

Essa etapa resolveu a estruturação da base para consultas analíticas.

Arquivos relacionados:

- `guia_questao_3_dbeaver.md`
- `scripts/script2.py`

## 5. Questão 4: análise de clientes mais valiosos

Na questão 4 foi feita uma análise para encontrar clientes mais relevantes com base em:

- faturamento total
- frequência de compra
- ticket médio
- diversidade de categorias compradas

Na consulta SQL, os dados foram montados a partir da cadeia:

`orders -> order_items -> product_variants -> products`

Depois, os clientes com pelo menos 13 categorias distintas foram filtrados, e os 10 melhores foram ordenados pelo maior ticket médio.

Na parte escrita da resposta, foi explicado por que o relacionamento entre tabelas é necessário e como o filtro de diversidade afeta o resultado final.

Arquivos relacionados:

- `questao_4.1.sql`
- `questao_4.2.md`

## 6. Questão 5: média de vendas por dia da semana

Na questão 5 foi construída uma consulta para analisar vendas do canal `pos` sem distorcer a média dos dias da semana.

A solução usou:

- uma tabela calendário gerada com `generate_series`
- agregação das vendas por dia
- `LEFT JOIN` entre calendário e vendas
- `COALESCE` para preencher dias sem venda com zero

O ponto central dessa etapa foi mostrar que dias sem venda também precisam entrar no cálculo, senão a média fica inflada artificialmente.

Na resposta em Markdown, isso foi explicado de forma conceitual, destacando o problema de ignorar datas ausentes na tabela `orders`.

Arquivos relacionados:

- `questao_5.1.sql`
- `questao_5.2.md`

## 7. Questão 6: baseline de previsão de vendas

Na questão 6 foi criado um baseline de previsão para o produto `Bússola de Bordo 702`.

O script `script3.py`:

- lê `products.csv`, `product_variants.csv`, `orders.csv` e `order_items.csv`
- encontra o produto alvo
- identifica suas variantes
- relaciona os itens vendidos com os pedidos
- agrega as vendas por mês
- aplica uma média móvel simples de 3 meses
- calcula as previsões para janeiro, fevereiro e março de 2026
- mede o erro absoluto e o MAE

O resultado consolidado da previsão para o primeiro trimestre de 2026 foi de 107 unidades, após arredondamento da soma das previsões mensais.

Na parte teórica, também foi registrado:

- como evitar data leakage
- quais meses entram no histórico de cada previsão
- quais são as limitações do baseline

Arquivos relacionados:

- `scripts/script3.py`
- `questao_6.2.md`
- `questao_6.3.md`

## 8. Questão 7: recomendação por similaridade entre produtos

Na questão 7 foi implementada uma abordagem simples de recomendação baseada em histórico de compra.

O script `script4.py`:

- lê produtos, variantes, pedidos e itens de pedido
- relaciona pedidos a clientes
- transforma compras em uma matriz cliente-produto binária
- marca com `1` quando o cliente comprou o produto
- calcula similaridade de cosseno entre produtos
- usa como referência o produto `Motor de Popa 1949`
- retorna os 5 produtos mais similares

A explicação escrita detalha como a matriz foi construída, o que a similaridade de cosseno mede e quais são as limitações dessa abordagem, principalmente para produtos novos ou cenários com pouco histórico.

Arquivos relacionados:

- `scripts/script4.py`
- `questao_7.3.md`

## 9. Dashboard entregue

Além das respostas analíticas e scripts, também foi gerado um dashboard em HTML:

- `dashboard_lh_nautical.html`

Esse arquivo representa a parte visual da atividade, consolidando indicadores e facilitando a leitura dos resultados em formato de painel.

## 10. Resumo final do que foi feito

De forma prática, esta atividade cobriu um fluxo completo de dados:

1. leitura e entendimento dos CSVs
2. análise exploratória inicial
3. geração automática de schema
4. preparação da carga no PostgreSQL
5. documentação do processo manual no DBeaver
6. consultas SQL para responder perguntas de negócio
7. construção de um baseline de previsão
8. implementação de recomendação por similaridade
9. entrega de documentação complementar
10. geração de dashboard final

## 11. Arquivos principais da atividade

Os arquivos mais importantes desta entrega são:

- `questao_1.1.sql`
- `schema.sql`
- `guia_questao_3_dbeaver.md`
- `questao_4.1.sql`
- `questao_4.2.md`
- `questao_5.1.sql`
- `questao_5.2.md`
- `questao_6.2.md`
- `questao_6.3.md`
- `questao_7.3.md`
- `scripts/script1.py`
- `scripts/script2.py`
- `scripts/script3.py`
- `scripts/script4.py`
- `dashboard_lh_nautical.html`

## 12. Conclusão

O trabalho desenvolvido nesta atividade não ficou apenas na resposta textual das perguntas. Ele também incluiu automação, modelagem de dados, carga em banco, consultas analíticas, previsão e recomendação. Isso mostra um fluxo completo de preparação e uso de dados, indo da estruturação da base até a geração de análises e entregáveis finais.
