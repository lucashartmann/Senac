from models import Locomotiva, Vagao, Trem, Garagem
import Controller
import View
import sys
import ControllerCMD

Controller.Controller.init()

View.View.mostrar_mensagem(
    "Ferroviária 2025 (CLI) - v.0.1.0 - SENAC Tech - POA/RS")

try:
    comando = sys.argv[1:]  # python App.py ajuda
except IndexError:
    View.View.mostrar_mensagem("ERRO")
    View.View.ajuda()
    sys.exit(0)

match comando:
    case ["ajuda"]:  # python App.py ajuda
        View.View.ajuda()
    case ["adicionar_vagao", peso]:  # python App.py adicionar_vagao 100.0
        ControllerCMD.ControllerCMD.adicionar_vagao(peso)
    # python App.py adicionar_locomotiva 100.0 500.0
    case ["adicionar_locomotiva", combustivel, peso]:
        ControllerCMD.ControllerCMD.adicionar_locomotiva(combustivel, peso)
    case ["adicionar_trem"]:  # python App.py adicionar_trem
        ControllerCMD.ControllerCMD.adicionar_trem()
    case ["remover", id_veiculo]:  # python App.py remover 1
        ControllerCMD.ControllerCMD.remover(id_veiculo)
    case ["engatar", id_trem, id_veiculo]:  # python App.py engatar 1 2
        ControllerCMD.ControllerCMD.engatar(id_trem, id_veiculo)
    case ["desengatar", id_trem, id_veiculo]:  # python App.py desengatar 1 2
        ControllerCMD.ControllerCMD.desengatar(id_trem, id_veiculo)
    case ["esvaziar_garagem_locomotiva"]:  # python App.py esvaziar_garagem_locomotiva
        ControllerCMD.ControllerCMD.remover_locomotivas_da_garagem()
    case ["esvaziar_garagem_vagao"]:  # python App.py esvaziar_garagem_vagao
        ControllerCMD.ControllerCMD.remover_vagoes_da_garagem()
    case ["esvaziar_garagem_trem"]:  # python App.py esvaziar_garagem_trem
        ControllerCMD.ControllerCMD.remover_trens_da_garagem()
    case ["esvaziar_trem", id_veiculo]:  # python App.py esvaziar_trem 1
        ControllerCMD.ControllerCMD.esvaziar_trem(id_veiculo)
    case ["listar_trens"]:  # python App.py listar_trens
        ControllerCMD.ControllerCMD.listar_trens()
    case ["listar_locomotivas"]:  # python App.py listar_locomotivas
        ControllerCMD.ControllerCMD.listar_locomotivas()
    case ["listar_vagoes"]:  # python App.py listar_vagoes
        ControllerCMD.ControllerCMD.listar_vagoes()
    case ["listar_veiculos"]:  # python App.py listar_veiculos
        ControllerCMD.ControllerCMD.listar_veiculos()
    case _:
        View.View.mostrar_mensagem("Entrada inválida")
        View.View.ajuda()


def menu():
    while True:
        View.View.ver_menu()
        opcao = int(View.View.pedir_dados("Digite o número da opção desejada"))
        match opcao:
            case 1 | 2 | 3:
                Controller.Controller.cadastro(opcao)
            case 4 | 5 | 6:
                Controller.Controller.remocao(opcao)
            case 7:
                Controller.Controller.engatar_no_trem()
            case 8:
                Controller.Controller.desengatar()
            case 9:
                Controller.Controller.esvaziar_garagem()
            case 10:
                Controller.Controller.esvaziar_trem()
            case 11:
                Controller.Controller.listar_vagoes_garagem()
            case 12:
                Controller.Controller.listar_locomotivas_garagem()
            case 13:
                Controller.Controller.listar_trens_garagem()
            case 14:
                Controller.Controller.listar_veiculos_garagem()
            case 15:
                Controller.Controller.get_quant_veiculos_na_garagem()
            case 16:
                break
            case _:
                View.View.mostrar_mensagem("Opção inválida, tente novamente")


if __name__ == "__main__":
    View.View.mostrar_mensagem(
        "Ferroviária 2025 - v.0.1.0 - SENAC Tech - POA/RS")
    menu()
    View.View.mostrar_mensagem("Programa encerrado.")
