### Atalhos

- **q** -> sair do vi ou do les
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
        - **git config --global init.defaultBranch** main -> git define as branchs default como "master". Esse comando altera para "main"
- **git add**
    - **git add .** -> Prepara todos os arquivos para o commit. Salva as alterações
    - **git add -u** -> adiciona só os arquivos modificados
- **git commit**
    - **git commit -m** "nome do commit"
    - tecla i --> digita o nome do commit --> ESC -> :wq (salva e sai) (write and quit)
- **git pull** -> Traz as alterações do remoto para o local
    - **git pull origin main**
    - **git pull upstream main**
    - **git pull** github
- **git push** -> manda tuas mudanças locais para o remoto (Github)
    - **git push --set-upstream** github main -> Criou (ou usou) a branch main no remoto e mandou as mudanças do local para ela
    - **git push** github
- **git branch** -> lista todos as branchs
- **git merge**
    - **git merge** ver1 -> (estando na main) traz as alterações da branch ver1 para a branch main
- **git rm --cached** -> Tira os arquivos do git add. Remove as mudanças staged to commit
- **git revert** hashCommit -> Reverte o commit
- **git checkout**
    - **git checkout** hashCommit
    - **git checkout -b** main -> Cria a branch main e te leva até ela
    - **git checkout -b** ver1 -> Cria a branch ver1 e te leva até ela
    - **git checkout** main -> Te leva até a branch main
    - **git checkout** README.md -> Pega o README.md do remoto (do último commit) e trás pro local
    - **git checkout** main -- README.md
- **git diff** -> Vê todas as diferenças da branch local com a remota
- **git remote**
    - **git remote -v** -> exibe todos os repositorios remotos e locais
    - **git remote add** github https://github.com/proj01.git

### Comandos gerais:

- **pwd** 
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
    - **control + s** -> salva o arquivo
    - **control + x** -> sai do programa
- **vi** - outro editor de texto
    - **:qa!** -> sair sem salvar
    - **:q** -> salvar (quit)
    - **:wq** -> salva e sair (write and quit)
    - **:w** nome_do_arquivo.txt -> cria arquivo e salva (write)
    - **vi** index.html -> abre o arquivo para editar