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

FUNÇOES
Módulos:
● Arquivos que contêm funções para incluir em nossas aplicações. *.py
Pacotes:
● Diretórios que contêm múltiplos módulos ou subpacotes.
○ Extensive Standard Library
■ Ex.: math, os, json, pandas, numpy, requests
○ Externos:
■ Ex.: pandas, numpy, requests
Venvs:
● Ambientes virtuais onde podemos instalar os pacotes de uma aplicação, evitando
instalá-los na nossa máquina.

Ler e inspecionar dados com Pandas
Dica:
Antes de manipular os dados, sempre faça uma leitura inicial para entender o
formato e evitar erros.
pd.read_csv() → carrega dados tabulares em DataFrame
head() → mostra as primeiras linhas do conjunto
shape → tamanho (linhas x colunas)
columns → nomes das colunas
info() → tipos de dados e valores ausentes

 """

olar = 'olá amigo, como voce é legal'
print(str.capitalize(olar))
print(str.upper(olar))

if olar == 'olá amigo, como voce é legal':
    print('Wow! você é INCRÍVEL')
else:
    print('Quase lá, amigão')

x,y= 5,2
potencia = x**y
print(potencia)

list = [10,20,30,40]
list.append(50)
x=list.count(20)
print(f'Contador: {x}')
index1 = list.index(30)
print(f'Index: {index1}')
list.insert(0,0)
print(list)

metricas = {"precisao":0.85, "recall": 0.80}


for key, value in metricas.items(): 
    print(key, value)

def media(nota1,nota2):
    return (nota1 + nota2)/2

print(media(8,9))

list = ["apple","banana","cherry"]

for index, value in enumerate(list): # enumerate retorna tbm o index
    print(index,value)