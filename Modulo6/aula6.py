""" HANDS ON
● ls → Lista os arquivos e diretórios no diretório atual.
    ○ Com o parâmetro -a, mostra tudo.
    ○ Pedir um help --help
● cd → Navega entre diretórios.
● pwd → Mostra o diretório atual em que você está.
● mkdir → Cria um novo diretório.
● rmdir → é ótimo para remover diretórios não usados e vazios de forma segura. Se você quer remover arquivos ou diretórios que
contém arquivos, você deve usar o comando rm.
    ○ rm → Remove arquivos. Use com cuidado, pois isso pode excluir permanentemente arquivos.
    ○ rmdir → remove pasta.
■ Se tiver uma pasta dentro de pasta… Use o Help + -rm -r
● cp → Copia arquivos e diretórios.
● mv → Move arquivos e diretórios. Pode ser usado para renomear também.
● cat ou nano → Exibe o conteúdo de um arquivo. Por exemplo, "cat nome_do_arquivo".
    ○ Comando less para paginação. Para sair, aperte Q.

HANDS ON
● grep → Filtra o conteúdo de um arquivo de texto usando expressões regulares.
    ○ (grep "exemplo" exemplo.txt)
● echo → Exibe uma linha de texto ou variável.
    ○ Nome=ˮLuisˮ → echo $nome)
● sudo → Executa um comando como superusuário (root). Use com cuidado, pois pode modificar o sistema.
● apt-get → Gerenciador de pacotes para instalar, atualizar e remover software no sistema (dependendo da distribuição Linux).
● wget ou curl → Baixa arquivos da internet. O segundo geralmente é usado em chamadas de API
    ○ Exemplo: curl X GET "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json"
● ps → Exibe os processos em execução.
● kill → Termina um processo. Você precisa fornecer o ID do processo.
● history → Exibe o histórico de comandos recentes.
Temos muitos outros comandos para uso, como chmod (modificar permissões), chown (alterar proprietário ou grupo).



Conceito de Versão por Git
Branches
Branch significa “ramoˮ, ou seja, uma ramificação do seu código.
Imagine a seguinte situação: você tem o seu código que já está funcionando em
produção e precisa desenvolver uma nova funcionalidade (“featureˮ). Mas você não
pode mexer direto no código em produção.
Para isso, você cria uma ramificação do seu código, uma branch, em que você pega
o estado atual daquele código e cria um novo ambiente para desenvolver a nova
feature a partir dali. Dessa forma, você não altera a versão principal do seu código,
consegue desenvolver sua funcionalidade com segurança.

Commits
Um commit é um conjunto de alterações que você fez em um projeto. Ele marca uma
versão do seu código. Um commit guarda as alterações feitas nos arquivos, quem
fez essas alterações e uma mensagem que resume essa alteração.
Além disso, cada commit tem um hash único que pode ser usado para acompanhar
todas as alterações feitas no passado e inclusive pode ser usado para voltar em
alguma alteração específica ou em algum ponto no tempo específico do seu código.
Pull Request
Um pull request é um pedido que se faz ao dono do repositório para que este
atualize o código dele com o seu código. Ou seja, você pede para que o dono do
projeto ao qual você quer contribuir adicione suas modificações ao projeto oficial.

Clone
Um clone de um repositório funciona como uma branch de um repositório online em
um repositório local. Ou seja, quando se deseja trabalhar em um repositório
hospedado no github (por exemplo), clona-se esse repositório para o seu
computador, trabalha-se nele, e então é pedida a permissão para atualizar as
alterações online.
Fork
Um fork é um novo repositório que compartilha configurações de código e
visibilidade com o repositório "upstream" original. Os forks geralmente são usados
para iterar ideias ou alterações antes de serem propostas de volta para o repositório
upstream, como em projetos código aberto ou quando um usuário não tem acesso
de gravação ao repositório upstream.

HANDS ON
● git init → Inicializa um repositório Git em um diretório local.
● git remote -v → Lista os repositórios remotos vinculados ao seu repositório local.
    ○ git remote add [nome] [url] → Adiciona um novo repositório remoto.
    ○ git remote remove [nome] → Remove um repositório remoto.
● git clone [url] → Clonar um repositório Git existente para o seu diretório local.
● git branch→ Lista todas as branches do repositório.
    ○ git branch [nome] → Cria uma branch com esse nome no repositório.
    ○ git branch -D [nome] → Apaga uma branch com esse nome
    ○ git branch -m [nome] → Renomeia a branch com esse nome no repositório
● git checkout [branch] → Muda para a branch especificada.
    ○ git checkout -b [branch] → Cria e muda para uma branch especificada.

● git status → Mostra o estado atual do seu repositório, incluindo arquivos modificados, adicionados ou removidos.
● git add [arquivo] → Adicionar arquivos ao staging area para prepará-los para o commit.
    ○ git add . → Adicionar TODOS os arquivos ao staging area para prepará-los para o commit.
■ Se eu modificar o arquivo agora, terei dois arquivos. Um no Workspace e um no Stage.
● git reset (padrão --mixed): Retorna a staging para o último commit do repositório e volta os arquivos para o workspace.
    ○ Tem o --hard que reseta até o workspace. MUITO CUIDADO Ideal para alterações locais)
● git revert: mantém o conjunto de alterações original e usa um novo commit para aplicar a ação de desfazer. Ideal para alterações
remotas/públicas)
● git restore [arquivo] → Descarta as alterações feitas em um arquivo no diretório de trabalho, revertendo-o para o estado do último
commit, sem afetar o staging area.
● git diff → Mostra as diferenças entre arquivos no diretório de trabalho e o staging area.

● git commit -m "mensagem" → Realiza um commit dos arquivos no staging area com uma mensagem descritiva.
    ○ git commit -a -m "mensagem" → Comando pula a staging area apenas para arquivos que já são rastreados pelo Git;
arquivos novos ainda precisam do git add.
● git log → Exibe o histórico de commits do repositório.
● git shortlog → Exibe o histórico de commits do repositório por autor.
● git reflog → Exibe as ações dentro do repositório.
● git push → Envia seus commits locais para o repositório remoto.
● git pull → Puxa as alterações do repositório remoto para o seu repositório local

Arquivo .gitignore
É um arquivo de texto simples que diz ao Git quais arquivos ou pastas ele deve ignorar e nunca enviar para o repositório.
Por que usar?
● Segurança: Evita subir senhas, chaves de API e arquivos de configuração local (.env).
● Limpeza: Não polui o repositório com arquivos desnecessários (ex: pastas de bibliotecas como venv/ ou n
 """