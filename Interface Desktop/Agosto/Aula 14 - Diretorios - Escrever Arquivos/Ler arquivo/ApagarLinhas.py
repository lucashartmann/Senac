import os
import sys

nome_arquivo = "apagar_linha.txt"
novas_linhas = list()

with open(nome_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        if not linha.startswith("*"):
            novas_linhas.append(linha)


with open(nome_arquivo, 'w') as arquivo:
    arquivo.writelines(novas_linhas)
