import sys
import random

numero_secreto = random.randrange(0, 10)


def mostrar_numero(numero):
    print("Número é", numero)


def listar():
    print("Listando...")


def ajuda():
    print("Comandos: listar, ajuda, numero")


try:
    comando = sys.argv[1]  # python interface.py numero
except IndexError:
    ajuda()
    sys.exit(0)

if comando == "listar":
    listar()
elif comando == "ajuda":
    ajuda()
elif comando == "numero":
    mostrar_numero(numero_secreto)
