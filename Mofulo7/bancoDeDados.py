""" Conceito
ORACLE
“Um banco de dados é uma coleção organizada de informações - ou dados
- estruturadas, normalmente armazenadas eletronicamente em um sistema de computador.ˮ

Dados Estruturados: Dados organizados em um formato de
banco de dados com linhas e colunas, com chaves relacionais.

● Endereçáveis para análise eficaz
● Facilmente mapeados em campos pré-designados

Exemplo: Dados relacionais
armazenados em um banco de
dados SQL

Dados Semi-Estruturados: Informações com propriedades
organizacionais, porém não residem em um banco de dados relacional.

● Facilitam a análise, embora possam ser desafiadores para
armazenar em um banco de dados relacional
Exemplo: Dados em formato JSON.

Dados Não Estruturados: Dados sem organização pré-definida ou modelo de
dados, não adequados para um banco dedados relacional.
● Armazenados e gerenciados em plataformas alternativas
● Cada vez mais utilizados em sistemas de TI

Exemplo: Documentos em formato Word, PDF, texto, registros de mídia


O que são SGBD?

Um sistema de gerenciamento de
banco de dados (SGBD) é um
conjunto de programas de software
que permite aos usuários criar,
editar, atualizar, armazenar e
recuperar dados em tabelas de
banco de dados.

ARQUITETURA EM CAMADAS:
1. Nível Interno (Físico), que lida com o hardware e
define como os arquivos e índices são realmente
gravados no disco
2. Nível Conceitual (Lógico), que descreve a
estrutura global do banco, incluindo as tabelas,
regras e os relacionamentos entre os dados
3. Nível Externo (Visões), que apresenta recortes
específicos e simplificados das informações de
forma personalizada para diferentes usuários ou
aplicações 

Motor de Banco de Dados: Responsável pelo gerenciamento do armazenamento, recuperação e
manipulação dos dados. Executa operações como inserção, atualização, exclusão e consulta de dados.

Processador de Consultas: Interpreta as consultas SQL enviadas ao banco de dados. Analisa as consultas
para determinar a forma mais eficiente de recuperar os dados e gera um plano de execução.

Otimizador de Consultas: Avalia várias estratégias de execução e escolhe a mais eficiente com base em
fatores como custo de acesso aos dados, disponibilidade de índices e estatísticas de uso.

Gestor de Transações: Garante a atomicidade, consistência, isolamento e durabilidade (ACID) das
transações no banco de dados. Coordena e controla o início, a execução e o término das transações para
garantir segurança e integridade.

Gestor de Armazenamento: Gerencia o armazenamento físico dos dados no disco. Controla a alocação e
o acesso aos blocos de dados, garantindo eficiência e segurança nas operações de leitura e gravação.

PROPRIEDADES:
● Atomicidade
● Consistência
● Isolamento
● Durabilidade

Atomicidade da Transação:
● Transação ocorre totalmente ou não
ocorre.
● Não há estado intermediário.
● Abort:
○ Falha na transação resulta em
nenhuma modificação no banco
de dados.
● Commit:
○ Alterações visíveis após
confirmação.

Integridade dos Dados:
○ Garante consistência antes e depois das
transações.
○ Observa as regras de invariância do
sistema, como restrições, gatilhos ou
operações em cascata.

Isolamento de Transações:
● Evita estados conflitantes no banco de
dados por acessos simultâneos.
● Transações autônomas ocorrem
separadamente.
● Mudanças não são visíveis até serem
confirmadas ou armazenadas

Exemplo:
Imagine que você e um amigo têm uma
conta conjunta com R$ 1.000,00. Vocês
decidem sacar dinheiro no mesmo segundo
em caixas eletrônicos diferentes:
Sua transação A Lê o saldo de R$ 1.000,
subtrai R$ 200, mas ainda não salvou.
Transação do amigo B Lê o saldo de ainda
R$ 1.000, subtrai R$ 300.
Resultado Final: Se o banco não tiver
isolamento, a transação B pode sobrescrever
a A, e o saldo final ficaria R$ 700 (como se os
seus R$ 200 tivessem evaporado)

Garantia de Durabilidade:
● Dados permanecem no banco
permanentemente após operação.
● Deve resistir a falhas do sistema.
● Atualizações são gravadas no disco
após a transação.

Sistemas de Gerenciamento de Banco de
Dados Relacionais RDBMS
● MySQL
● PostgreSQL
● Oracle
● SQL Server
● IBM DB2

Sistemas de Gerenciamento de Banco de
Dados NoSQL
● MongoDB
● Cassandra
● Redis
● CouchDB

● SGBD são interfaces de interação
com o banco de dados.
● Existem ferramentas próprias como o
console do Google e Snowflake, mas
também é possível usar programas
de terceiros como Dbeaver.
INTERAÇÃO


"""