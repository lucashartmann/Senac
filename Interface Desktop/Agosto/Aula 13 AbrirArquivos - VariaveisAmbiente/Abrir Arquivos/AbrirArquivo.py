with open('Exemplo.txt', 'r') as arquivo:
    for linha in arquivo.readlines(): 
        print(linha, end="")
