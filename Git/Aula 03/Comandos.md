### Atalhos

- **q** -> sair do arquivo
- **control + l** -> limpar a tela

### Comandos git

- **git clone**
- **git init** -> Inicializa o repositório
- **git status**
- **git log** -> Mostra todos os commits
- **git config**
    - **git config --local**
        - **git config --local user.email** "lucas@email.com"
        - **git conig --local user.name** "lucas"
    - **git config --global**
        - **git config --global user.email** "lucas@email.com"
        - **git conig --global user.name** "lucas"
        - **git config --global init.defaultBranch** main -> git define as branchs default como master. Esse comando altera para main
- **git add** . -> Prepara todos os arquivos para o commit. Salva as alterações
- **git commit**
    - **git commit -m** "nome do commit"
    - tecla i --> digita o nome do commit --> ESC -> :wq (salva e sai)
- **git pull**
    - **git pull origin main**
    - **git pull upstream main**
- **git push**
- **git branch**
- **git merge**
- **git rm --cached** -> Tira os arquivos do git add. Remove as mudanças staged to commit
- **git revert** hashCommit
- **git checkout** hashCommit

### Comandos gerais:

- **cd** trabgit/ -> Vai para o diretorio "trabgit"
- **mkdir** trabgit -> Cria diretorio (pasta) "trabgit"
- **cp** arquivo.txt a -> Copia "arquivo.txt" para diretorio "a"
- **ls** ou **ls -l** ou **ls -a** ou **ls -la** -> Lista arquivos do diretorio
- **mv** arquivo.txt arquivo.md -> Renomeia o "arquivo.txt" para "arquivo.md"
    - **mv** a temp -> Renomeia o diretorio "a" para "temp"
    - **mv** arquivo.md a -> Move o "arquivo.md" para dentro do diretorio "a"
- **echo** - imprime algo 
    - **echo** oi, oi, oi > arquivo.txt -> imprime o conteudo (oi, oi, oi) dentro do arquivo.txt  (sobreescreve o conteudo do arquivo)
    - **echo** oi, oi, oi >> arquivo.txt -> imprime o conteudo (oi, oi, oi) dentro do arquivo.txt  (adicionando no final do arquivo, não sobreescreve)
- **cat** arquivo.txt -> imprime o conteudo do arquivo.txt no terminal
- **less** arquivo.txt -> imprime o conteudo do arquivo
- **nano** - editor de texto
    - **nano** arquivo.txt -> abre o editor de texto com o arquivo.txt
    - **nano** index.html -> cria o arquivo index.html e abre o editor de texto
    - **^O** -> salva e sai do arquivo
    - **control + s** -> salva o arquivo
- **vi** - outro editor de texto
    - **:qa!** -> sair sem salvar
    - **:q** -> salvar 
    - **:wq** -> salva e sair
    - **:w** nome_do_arquivo.txt -> cria arquivo e salva
    - **vi** index.html -> abre o arquivo para editar