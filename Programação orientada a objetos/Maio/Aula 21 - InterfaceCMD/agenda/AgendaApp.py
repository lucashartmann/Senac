import AgendaModel
import AgendaController

import sys

AgendaModel.agenda_init()
print("Agenda 2025 (CLI) - v.0.1.0 - SENAC Tech - POA/RS")

try:
    comando = sys.argv[1]  # python AgendaApp.py listar
except IndexError:
    print("ERRO")
    AgendaController.ctrl_ajuda()
    sys.exit(0)


def recebe_email():
    try:
        email = sys.argv[2]
        return email
    except IndexError:
        print("ERRO")
        sys.exit(0)


match comando:
    case "listar":
        AgendaController.ctrl_listar()
    case "ajuda":
        AgendaController.ctrl_ajuda()
    case "consultar":
        email = recebe_email()
        AgendaController.ctrl_consultar(email)
    case "apagar":
        email = recebe_email()
        AgendaController.ctrl_apagar(email)
    case "favoritar":
        email = recebe_email()
        AgendaController.ctrl_favoritar(email)
    case "cadastrar":
        try:
            email = sys.argv[2]
            nome = sys.argv[3]
            idade = int(sys.argv[4])
            endereco = sys.argv[5]
            favorito = False
            try:
                cod_favorito = sys.argv[6]
                if cod_favorito == "s":
                    favorito = True
            except IndexError:
                pass
            AgendaController.ctrl_cadastrar(
                email, nome, idade, endereco, favorito)
            # python AgendaApp.py cadastrar lucas@email.com "Lucas Augusto" 21 "Avenida Bento 405" s
        except IndexError:
            print("Erro")
            pass
    case "atualizar":
        pass
