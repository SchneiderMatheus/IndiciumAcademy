""" Operações com strings
● str.capitalize() - Primeira letra caixa alta → str
● str.upper() - Toda a string em caixa alta → str
● str.lower() ou casefold() - Toda a string em caixa baixa → str
● str.split(separator, maxsplit) - Separa de acordo com o separador
definido → list
● separator.str.join(iterable) - Une elementos de uma lista em uma string
→ str
● str.count(value, start, end) - Retorna quantidade de vezes que valor
aparece em um intervalo numa string → int
● str.replace(oldvalue, newvalue, count) - substitui um valor por outro na
quantidade definida numa string → str """

"""Operações com números
Operações com números são determinadas pelos operadores
OperatorNameExample Operator Name Example Returns
+ Addition x + y int or float
- Subtraction x - y int or float
* Multiplication x * y int or float
/ Division x / y float (always)
% Modulus x % y int or float
** Exponentiation x ** y int or float
// Floor division x // y int or float """

""" Lists - []
● Ordenadas, mutáveis e
permitem duplicatas
● Itens são indexados
● Acesso: list[i] ou list[range]
Métodos:
● list.append(value)
● list.count(value)
● list.index(i)
● list.insert(i, elmnt)
● list[i] = new_value
● list.pop(i)
● list.remove(elmnt)
● list.sort()
● lent(list) """

""" Dicts - {k: v}
● Guardam dados em {chave:
valor}
● Ordenados, mutáveis e não
permitem duplicatas
● Acesso: dict[key] ou
dict.get(key)
Métodos:
● dict.pop(keyname) """

""" LOGICAL OPERATORS
and            Returns True if both statements are true                x < 5 and x < 10
or             Returns True if one of the statements is true           x < 5 or x < 4
not            Reverse the result, returns False if true               not(x < 5 and x < 10)

Identity operators

is             Returns True if both variables are same object          x is y
is not         Returns True if both variables are NOT same object      x is not y

Membership operators

in             Returns True if sequence is present in object           x in y
not in         Returns True if sequence is NOT present                 x not in y
 """