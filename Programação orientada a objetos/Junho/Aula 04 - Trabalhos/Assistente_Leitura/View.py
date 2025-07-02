class View:

    def imprimir_lista(lista):
        for objeto in lista:
            print(objeto)

    def imprimir(mensagem):
        print(mensagem)

    def pedir_dado(mensagem):
        dado = input(f"{mensagem}: ")
        return dado

    def ajuda():
        ajuda = '''
"Comandos disponíveis:"
"cadastrar_livro <titulo> <autor> <ano>"
"remover_livro <titulo>"
"ver_livros_cadastrados"
"marcar_pagina <id> <pagina>"
"leituras_em_andamento"
"leituras_concluidas"
"leituras_nao_iniciadas"
"ver_livros_do_autor <autor>"
"pesquisar_livros_por_titulo <titulo>"
"status <id>"
"pagina_atual <id>"
"quant_paginas_restantes <id>"
"percentual <id>"
"ajuda"
        '''
        View.imprimir(ajuda)
