## Questão 7.3

A matriz foi construída cruzando os clientes com os produtos comprados. Em cada linha ficou um `customer_id` e em cada coluna um `product_id`. Quando o cliente comprou aquele produto pelo menos uma vez, o valor ficou `1`. Quando nunca comprou, ficou `0`. Nesse caso, a quantidade comprada não entrou na conta, porque a ideia era olhar só presença ou ausência de compra.

A similaridade de cosseno, nesse contexto, serve para medir o quanto dois produtos têm um padrão parecido de compra entre os clientes. Ou seja, se muitos dos mesmos clientes compraram os dois produtos, a similaridade entre eles fica mais alta. Então, quanto maior esse valor, mais parecido é o comportamento de compra desses produtos.

Uma limitação desse método é que ele depende só do histórico de compra. Ele não considera contexto, preço, categoria, sazonalidade ou perfil do cliente. Além disso, se um produto for novo e ainda tiver poucas compras, ele praticamente não vai ter informação suficiente para gerar boas recomendações.
