## Questão 6.3

O baseline foi construído a partir de uma série mensal de vendas do produto **Bússola de Bordo 702**. Primeiro, os dados de `products.csv`, `product_variants.csv`, `orders.csv` e `order_items.csv` foram relacionados para identificar todas as vendas desse produto. Depois, essas vendas foram agregadas por mês com base na quantidade vendida. A previsão foi feita usando uma média móvel simples dos últimos 3 meses anteriores ao mês que seria previsto.

Para evitar data leakage, em cada previsão foram usados apenas dados que já existiam antes do mês analisado. Por exemplo, para prever janeiro de 2026 foram usados apenas outubro, novembro e dezembro de 2025. Para prever fevereiro de 2026, foram usados novembro de 2025, dezembro de 2025 e janeiro de 2026. Assim, a previsão nunca utilizou informações do próprio mês previsto nem de meses futuros.

Uma limitação desse modelo é que ele é muito simples e considera apenas o histórico recente de vendas. Ele não leva em conta sazonalidade mais longa, tendência, promoções, rupturas de estoque ou qualquer outro fator de negócio que possa influenciar a demanda. Por isso, pode funcionar como uma referência inicial, mas não necessariamente como um modelo ideal para tomada de decisão mais precisa.
