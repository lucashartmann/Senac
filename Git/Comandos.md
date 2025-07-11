### Atalhos

- ``q`` -> sair do Vim ou do Less
- ``control + l`` -> limpar a tela

### Comandos git

```bash 
git clone [link_do_repositório]
```

```bash 
git init # Inicializa o repositório

git init --bare # Inicia a ideia do teu próprio servidor git ao invés de usar github e etc
``` 

```bash 
git status
``` 

```bash 
git log # Mostra todos os commits
``` 

```bash 
git fetch # Informa tua branch local das mudanças que existem na remoto
``` 

```bash 
git config

git config --local
git config --local user.email [email]
git config --local user.name [nome_do_usuário]

git config --global
git config --global user.email [email]
git config --global user.name [nome_do_usuário]
git config --global init.defaultBranch [nome_da_branch] # git define as branchs default como "master". Esse comando altera para "main" ou outra desejada
``` 

```bash 
git add

git add . # Prepara todos os arquivos para o commit. Salva as alterações

git add -u # adiciona só os arquivos modificados
``` 

```bash 
git commit

# Passo a passo:
#    1. tecla i 
#    2. digita o nome do commit 
#    3. ESC 
#    4. :wq (salva e sai) (write and quit)

git commit -m [titulo_do_commit]
``` 

```bash 
git pull # Traz as alterações do remoto para o local

git pull origin [nome_da_branch]

git pull upstream [nome_da_branch]

git pull [apelido_do_repositório]
``` 

```bash 
git push # manda tuas mudanças locais para o remoto (Github)

git push --set-upstream [apelido_do_repositório] [nome_da_branch] # Criou (ou usou) a branch main no remoto e mandou as mudanças do local para ela

git push [apelido_do_repositório]
``` 

```bash 
git branch # lista todos as branchs
``` 

```bash 
git merge

git merge [nome_da_branch] # (estando na main) traz as alterações da branch desejada para a branch main
``` 

```bash 
git rm --cached # Tira os arquivos do git add. Remove as mudanças staged to commit
``` 

```bash 
git revert [hash_do_commit] # Reverte o commit
``` 

```bash 
git checkout

git checkout [hash_do_commit]

git checkout -b [nome_da_branch] # Cria (se não existir) a branch e te leva até ela

git checkout [nome_da_branch] # Te leva até a branch

git checkout [nome_do_arquivo] # Pega o arquivo do remoto (do último commit) e trás pro local

git checkout [nome_da_branch] -- [nome_do_arquivo]
``` 

```bash 
git diff # Vê todas as diferenças da branch local com a remota
``` 

```bash 
git remote

git remote -v # exibe todos os repositorios remotos e locais

git remote add [apelido_do_repositório] [link_do_repositório]

``` 

### VS Code
- clica no "+" para stage commit (git add)

### Comandos gerais:
```bash 
pwd # Imprime o diretório que a pessoa está
```

```bash 
rm [nome_do_arquivo] # Apaga arquivo

rm -r [nome_do_diretorio] # Apaga diretório
```

```bash 
cd [nome_da_pasta/] # Vai para o diretorio 
```

```bash 
mkdir [nome_da_nova_pasta] # Cria diretorio (pasta) 
```

```bash 
rmdir [nome_da_nova_pasta] # Remove diretorio (pasta) 
```

```bash 
cp [nome_do_arquivo] a # Copia arquivo para diretorio "a"
```

```bash 
ls # Lista arquivos do diretorio

ls -l

ls -a 

ls -la 
```

```bash 
mv [nome_do_arquivo] [novo_nome_do_arquivo] # Renomeia o arquivo 

mv [nome_do_diretorio] [novo_nome_do_diretorio] # Renomeia o arquivo 

mv [nome_do_arquivo] [nome_diretorio] # Move o arquivo para dentro do diretorio 
```

```bash 
echo # imprime algo 

echo oi, oi, oi > [nome_do_arquivo] # imprime o conteudo (oi, oi, oi) dentro do arquivo (sobreescreve o conteudo do arquivo)

echo oi, oi, oi >> [nome_do_arquivo] # imprime o conteudo (oi, oi, oi) dentro do arquivo (adicionando no final do arquivo, não sobreescreve)
```

```bash 
cat [nome_do_arquivo] # imprime o conteudo do arquivo no terminal
```

```bash 
less [nome_do_arquivo] # imprime o conteudo do arquivo
```

#### Nano
```bash 
nano # editor de texto
```
```bash 
nano [nome_do_arquivo] # cria o arquivo (se não existir) e abre o editor de texto
```
```bash 
control + s # salva o arquivo
```
```bash 
control + x # sai do programa
```

#### Vim
```bash 
vi # outro editor de texto
```
```bash 
vi [nome_do_arquivo] # abre o arquivo para editar
```
```bash 
:qa! # sair sem salvar
```
```bash 
:q # salvar (quit)
```
```bash 
:wq # salva e sair (write and quit)
```
```bash 
:w [nome_do_arquivo] # cria arquivo e salva (write)
```