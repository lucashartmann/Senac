import os

print(f"Diretorio atual: {os.getcwd()}")
print(f"Contúdo de dados: {os.listdir()}")

# with open(f"{os.getcwd()}/dados/config.txt") as config:
#     print(config.read())

try:
    os.mkdir("entrada")
    os.mkdir("entrada/corredor")
    os.mkdir("entrada/corredor/sala1")
    os.mkdir("entrada/corredor/sala2")
    os.mkdir("entrada/SalaDeEspera")
    print("Mapa criado!")
except FileExistsError:
    print("Mapa já existe")
