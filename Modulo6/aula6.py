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


 """