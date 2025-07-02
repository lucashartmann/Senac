def novo():
    print("Executando novo....")

def fechar():
    print("Executando fechar...")

comandos = {
    "new": novo,
    "close": fechar
}

comando = input("Comando: ")

comandos[comando]()