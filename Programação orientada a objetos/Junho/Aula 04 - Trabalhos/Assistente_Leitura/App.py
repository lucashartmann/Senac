from Models import Livro, Estante
import Controller
import View
import sys


View.View.imprimir(
    "Assistente de Leitura 2025 (CLI) - v.0.1.0 - SENAC Tech - POA/RS")
# Controller.Controller.inicializar_objetos()

Controller.Controller.carregar_estante()

try:
    comando = sys.argv[1:]
except IndexError:
    View.View.imprimir("ERRO")
    View.View.ajuda()
    sys.exit(0)

# python App.py cadastrar_livro "DOM CASMURRO" "MACHADO DE ASSIS" 300
# python App.py cadastrar_livro "O PRINCIPE" "MAQUIAVEL" 200
# python App.py livros_cadastrados


match comando:
    case ["ajuda"]:
        View.View.ajuda()
    case ["cadastrar_livro", titulo, autor, quant_paginas]:
        livro = Livro.Livro(titulo.upper(), autor.upper(), int(quant_paginas))
        Controller.Controller.cadastrar_livro(livro)
    case ["remover_livro", id]:
        Controller.Controller.remover_livro(int(id))
    case ["marcar_pagina", id, pagina]:
        Controller.Controller.marcar_pagina(int(id), int(pagina))
    case ["status", id]:
        Controller.Controller.get_status(int(id))
    case ["pagina_atual", id]:
        Controller.Controller.get_pagina_atual(int(id))
    case ["quant_paginas_restantes", id]:
        Controller.Controller.get_quant_paginas_restantes(int(id))
    case ["percentual", id]:
        Controller.Controller.get_percentual_leitura(int(id))
    case ["livros_cadastrados"]:
        Controller.Controller.ver_livros_cadastrados()
    case ["leituras_em_andamento"]:
        Controller.Controller.ver_leituras_em_andamento()
    case ["leituras_concluidas"]:
        Controller.Controller.ver_leituras_concluidas()
    case ["leituras_nao_iniciadas"]:
        Controller.Controller.ver_leituras_nao_iniciadas()
    case ["ver_livros_do_autor", autor]:
        Controller.Controller.pesquisar_livros_do_autor(autor.upper())
    case ["pesquisar_livros_por_titulo", titulo]:
        Controller.Controller.pesquisar_livros_por_titulo(titulo.upper())
    case _:
        View.View.imprimir("Entrada inválida")
        View.View.ajuda()

Controller.Controller.salvar_estante()
