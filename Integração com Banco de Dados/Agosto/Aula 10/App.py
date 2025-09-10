import sys
from InventarioDB import Banco

comando = sys.argv[1:] # python .\App.py inserir lucas 10 

um_banco =  Banco()

def menu(comando):
    match comando:
        case ["inserir", nome_item, dano]:
            print(um_banco.inserir((nome_item, dano)))
        case ["remover", nome_item]:
            print(um_banco.deletar_por_nome(nome_item))
        case ["atualizar", nome_item]:
            print(um_banco.atualizar_item(nome_item))
        case ["consultar", nome_item]:
            print(um_banco.consulta_por_nome(nome_item))
        case ["listar", nome_item]:
            print(um_banco.consultar_itens())


if __name__ == "__main__":
    if len(comando) > 0:
        menu(comando)
