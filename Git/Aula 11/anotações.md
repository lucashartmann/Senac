# Linux:

ssh lucashartmann@10.10.202.6
tech@2025

mkdir repos

git init --bare projeto.git

git config --global init.defaultBranch main

git init --bare dungeon.git

mkdir trab

git clone ~/repos/dungeon.git/

git clone ~/repos/dungeon.git/ ./novo_dungeon

touch README.md

git config --global user.email "lucashartmann@email"

git config --global user.name "lucashartmann"

# Windows:

cd Documents/

git clone lucashartmann@10.10.202.6:~/repos/dungeon.git

git remote add upstream https://github.com/lgmaciel/introgit.git