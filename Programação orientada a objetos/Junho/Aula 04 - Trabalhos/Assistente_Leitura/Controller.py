from Models import Estante, Livro
import View
import shelve


class Controller:

    estante = Estante.Estante()
    estante_banco = shelve.open("estante.db", writeback=True)

    def salvar_estante():
        Controller.estante_banco['estante'] = Controller.estante.get_lista_livros()
        # Controller.estante_banco['id_estante'] = Controller.estante.get_id()
        Controller.estante_banco.close()

    def carregar_estante():
        if 'estante' in Controller.estante_banco:
            Controller.estante.livros_comprados = Controller.estante_banco['estante']
            # Controller.estante.id = Controller.estante_banco['id_estante']

    def inicializar_objetos():
        livro1 = Livro.Livro("DOM CASMURRO", "MACHADO DE ASSIS", 300)
        livro2 = Livro.Livro("O PRINCIPE", "MAQUIAVEL", 200)
        livro3 = Livro.Livro("A MORTE DE IVAN ILITCH", "TOLSTOI", 150)
        livro4 = Livro.Livro("A HERDEIRA", "JUDE DEVERAUX", 400)
        livro5 = Livro.Livro("A HERDEIRA", "SIDNEY SHELDON", 500)
        Controller.estante.adicionar_livro(livro1)
        Controller.estante.adicionar_livro(livro2)
        Controller.estante.adicionar_livro(livro3)
        Controller.estante.adicionar_livro(livro4)
        Controller.estante.adicionar_livro(livro5)

    def cadastrar_livro(livro):
        cadastro = Controller.estante.adicionar_livro(livro)
        if cadastro:
            View.View.imprimir("Livro cadastrado com sucesso!")
        else:
            View.View.imprimir("ERRO ao cadastrar livro")

    def remover_livro(id):
        livro = Controller.estante.get_livro_por_id(id)
        if livro:
            remocao = Controller.estante.remover_livro(livro)
            if remocao:
                View.View.imprimir(livro, "removido com sucesso!")
            else:
                View.View.imprimir("ERRO ao remover livro")
        else:
            View.View.imprimir(
                f"ERRO. Não existe livro cadastrado com o id {id}")

    def ver_livros_cadastrados():
        livros_cadastrados = Controller.estante.get_lista_livros()
        if livros_cadastrados:
            View.View.imprimir("LIVROS CADASTRADOS:")
            View.View.imprimir_lista(livros_cadastrados)
        else:
            View.View.imprimir("ERRO, lista vazia")

    def marcar_pagina(id, pagina):
        livro = Controller.estante.get_livro_por_id(id)
        if livro:
            pagina_atual = livro.marcar_pagina(pagina)
            percentual_leitura = livro.get_percentual_leitura()
            status = livro.atualizar_status(percentual_leitura)
            View.View.imprimir(
                f"Página {pagina_atual} marcada. Status: {status}")
        else:
            View.View.imprimir(
                f"ERRO. Não existe livro cadastrado com o id {id}")

    def ver_leituras_em_andamento():
        leituras_em_andamento = Controller.estante.get_leituras_em_andamento()
        if leituras_em_andamento:
            View.View.imprimir("LEITURAS EM ANDAMENTO:")
            View.View.imprimir_lista(leituras_em_andamento)
        else:
            View.View.imprimir("ERRO, não existem leituras em andamento")

    def ver_leituras_concluidas():
        leituras_concluidas = Controller.estante.get_leituras_concluidas()
        if leituras_concluidas:
            View.View.imprimir("LEITURAS CONCLUÍDAS:")
            View.View.imprimir_lista(leituras_concluidas)
        else:
            View.View.imprimir("ERRO, não existem leituras concluídas")

    def ver_leituras_nao_iniciadas():
        leituras_nao_iniciadas = Controller.estante.get_leituras_nao_iniciadas()
        if leituras_nao_iniciadas:
            View.View.imprimir("LEITURAS NÃO INICIADAS:")
            View.View.imprimir_lista(leituras_nao_iniciadas)
        else:
            View.View.imprimir("ERRO, não existem leituras não iniciadas")

    def pesquisar_livros_do_autor(autor):
        livros_do_autor = Controller.estante.get_livros_por_autor(autor)
        if livros_do_autor:
            View.View.imprimir(f"LIVROS DO AUTOR {autor}:")
            View.View.imprimir_lista(livros_do_autor)
        else:
            View.View.imprimir(f"ERRO, não existem livros do autor {autor}")

    def pesquisar_livros_por_titulo(titulo):
        livros = Controller.estante.pesquisar_livros_por_titulo(titulo)
        if livros:
            View.View.imprimir(f"LIVROS COM TITULO '{titulo}':")
            View.View.imprimir_lista(livros)
        else:
            View.View.imprimir(
                f"ERRO, não existem livros com o titulo {titulo}")

    def get_status(id):
        livro = Controller.estante.get_livro_por_id(id)
        if livro:
            status = livro.get_status()
            View.View.imprimir(f"Status do livro '{id}': {status}")
        else:
            View.View.imprimir(
                f"ERRO, não existe livro cadastrado com o id {id}")

    def get_percentual_leitura(id):
        livro = Controller.estante.get_livro_por_id(id)
        if livro:
            percentual_leitura = livro.get_percentual_leitura()
            View.View.imprimir(
                f"Percentual de leitura do livro '{id}': {percentual_leitura}%")
        else:
            View.View.imprimir(
                f"ERRO, não existe livro cadastrado com o id {id}")

    def get_pagina_atual(id):
        livro = Controller.estante.get_livro_por_id(id)
        if livro:
            pagina_atual = livro.get_pagina_atual()
            View.View.imprimir(f"Página atual do livro '{id}': {pagina_atual}")
        else:
            View.View.imprimir(
                f"ERRO, não existe livro cadastrado com o id {id}")

    def get_quant_paginas_restantes(id):
        livro = Controller.estante.get_livro_por_id(id)
        if livro:
            quant_paginas_restantes = livro.get_quant_paginas_restantes()
            View.View.imprimir(
                f"Quantidade de páginas restantes do livro '{id}': {quant_paginas_restantes}")
        else:
            View.View.imprimir(
                f"ERRO, não existe livro cadastrado com o id {id}")
