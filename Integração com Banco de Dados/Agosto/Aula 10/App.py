import sys
from InventarioDB import Banco

comando = sys.argv[1:]

um_banco = Banco()


def menu(comando):
    match comando:
        case ["inserir", nome_item, dano]:  # python .\App.py inserir lucas 10
            print(um_banco.inserir((nome_item, dano)))
        case ["remover", nome_item]:  # python .\App.py remover lucas
            print(um_banco.deletar_por_nome(nome_item))
        case ["atualizar", nome_item, novo_dano]:  # python .\App.py atualizar lucas 20
            print(um_banco.atualizar_item(nome_item, novo_dano))
        case ["consultar", nome_item]:  # python .\App.py consultar lucas
            print(um_banco.consultar_por_nome(nome_item))
        case ["listar"]:  # python .\App.py listar
            print(um_banco.consultar_itens())
        case _:
            print("Valor inválido!")


if __name__ == "__main__":
    if len(comando) > 0:
        menu(comando)
