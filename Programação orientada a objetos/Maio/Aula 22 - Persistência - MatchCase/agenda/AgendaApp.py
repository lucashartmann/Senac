import AgendaModel
import AgendaController

import sys

print("Agenda 2025 (CLI) - v.0.1.0 - SENAC Tech - POA/RS")

argumentos = sys.argv[1:]

match argumentos:
    case ["listar"]:  # python AgendaApp.py listar
        AgendaController.ctrl_listar()
    case ["ajuda"]:  # python AgendaApp.py ajuda
        AgendaController.ctrl_ajuda()
    case ["consultar", email]:  # python AgendaApp.py consultar "lucas@gmail.com"
        AgendaController.ctrl_consultar(email)
    case ["apagar", email]:  # python AgendaApp.py apagar "lucas@gmail.com"
        AgendaController.ctrl_apagar(email)
    case ["favoritar", email]:  # python AgendaApp.py favoritar "lucas@gmail.com"
        AgendaController.ctrl_favoritar(email)
    case ["cadastrar", email, nome, idade, endereco]:
        AgendaController.ctrl_cadastrar(email, nome, idade, endereco)
    case ["cadastrar", email, nome, idade, endereco, ("*") as favoritar]:
        if favoritar == "*":
            favorito = True
        AgendaController.ctrl_cadastrar(email, nome, idade, endereco, favorito)
    case ["atualizar", email, nome, idade, endereco, favorito]:
        AgendaController.ctrl_atualizar(email, nome, idade, endereco, favorito)
    case ["atualizar_nome", email, nome]:
        AgendaController.ctrl_atualizar_nome(email, nome)

AgendaModel.minha_agenda.close()
