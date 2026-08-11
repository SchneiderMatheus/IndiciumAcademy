## Questão 5.2

É necessário usar uma tabela de datas porque a tabela de vendas só mostra os dias em que realmente existiu alguma venda registrada. Ou seja, se a loja abriu em um dia mas não vendeu nada, esse dia simplesmente não aparece na tabela `orders`. Se eu agrupar direto a tabela de vendas, vou ignorar esses dias zerados e a média vai ficar artificialmente maior do que a realidade.

Com a tabela de calendário, eu consigo garantir que todos os dias do período entrem no cálculo, inclusive os dias sem venda. Depois, com o `LEFT JOIN`, os dias que não tiverem registro em `orders` continuam aparecendo, e o valor da venda pode ser preenchido com zero.

Se um dia da semana tiver muitos dias sem nenhuma venda registrada e eles não forem considerados, a média desse dia vai ficar inflada. Na prática, vai parecer que esse dia vende melhor do que realmente vende. Foi exatamente esse o problema do exemplo do domingo: como os domingos sem venda ficaram fora da conta, a média ficou mais alta do que deveria.
