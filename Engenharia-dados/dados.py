""" Fundamentos da Engenharia de Dados:
O que é Engenharia de dados?
● Coleta: Integra múltiplas fontes APIs, bancos, arquivos, streams) com qualidade e
rastreabilidade.
● Armazenamento: define modelagem e camadas (data lake, data warehouse) para dados
brutos e tratados, com escalabilidade
● Processamento: Cria pipelines para trasnformar e consolidar dados em lote e tempo real
● Orquestração & Automação: Agenda, monitora e recupera falhas de jobs, garantindo
confiabilidade
● Governança & Segurança: Catálogo, linhagem, schema, acesso e compliance para uso
seguro dos dados

Implementar pipelines de dados eficazes é
crucial para empresas que buscam
insights precisos e em tempo real, pois
assegura que os dados fluam de maneira
contínua e confiável entre sistemas,
eliminando silos de informação e
aprimorando a qualidade dos dados
utilizados em processos analíticos.

INGESTÃO
A camada de ingestão de dados é o centro de uma arquitetura de analytics, é nela
que ocorre o processo de coletar os dados das suas fontes e levá-los para um
ambiente de destino, como data warehouses, data lakes, ou data marts.
Nós temos dois principais tipos de ingestão de dados, ingestão em lote (Batch) e
ingestão em tempo real (Streaming).

Streaming 
● Processamento de forma contínua
● Envolve filas (queues)
● Baixo volume de dados
● Alta complexidade
● Minoria das implementações
● Desafios como escalabilidade,
ordenamento, consistência e
tolerância

Batch
● Processamento em Blocos
● Envolve um agendamento (schedule)
● Alto volume de dados
● Normalmente executado em períodos
de baixa utilização
● “Simplesˮ de executar
● Maioria das implementações

ORQUESTRAÇÃO
É uma abordagem sistemática para coordenar e
automatizar processos complexos e cadeias de tarefas.
Esta metodologia permite que as organizações possam
integrar e gerenciar aplicações, automações e sistemas
em diferentes ambientes.

Orquestração de dados
Inclui a coleta, o processamento, a transformação e a entrega de dados para sistemas de análise e business
intelligence.
Orquestração de serviços
Foca na coordenação de microsserviços, redes, APIs e serviços de dados.
Orquestração de containers
Inclui automatizar o provisionamento, implantação, rede e a gestão do ciclo de vida dos containers em sistemas
como Docker e Kubernetes.
Orquestração de nuvem
Coordenação de recursos de computação em nuvem, como servidores, armazenamento e redes.

ORQUESTRAÇÃO DE DADOS:
Gerenciamento de workloads
Podemos evitar gargalos e garantir um desempenho mais
consistente e rápido, além de reduzir o risco de falhas

Alta escalabilidade de tarefas
Dimensionar recursos para acomodar volumes de dados
cada vez maiores, e novas fontes de dados

Flexibilidade
As dependências entre as tarefas são claras e ficam
centralizadas no mesmo ambiente

Redução de custos
Automatizando processos manuais e supervisão, a
orquestração de dados ajuda a reduzir os custos operacionais

Monitoramento
Monitorando continuamente os fluxos de trabalho e pipelines
de dados podemos identificar e resolver problemas rápidamente

Clareza de falha
Com a visualização do pipeline, conseguimos ter uma
clareza dos erros, e assim, prevenir e resolver rapidamente


 """