class View:

    def ajuda():
        comandos = '''
Comandos para a execução do programa:

1. "adicionar_vagao peso"
2. "adiconar_locomotiva combustivel peso"
3. "adicionar_trem"
4. "remover id_trem id_veiculo"
5. "engatar id_trem id_veiculo" 
6. "desengatar id_trem id_veiculo"
7. "esvaziar_garagem_locomotiva" 
8. "esvaziar_garagem_vagao"
9. "esvaziar_garagem_trem"
10. "esvaziar_trem id_veiculo"
11. "ajuda"
        '''
        View.mostrar_mensagem(comandos)

    def ver_menu():
        menu = '''
MENU TREM
1 - Adicionar Vagão
2 - Adicionar Locomotiva
3 - Adicionar Trem
4 - Remover Vagao
5 - Remover Locomotiva
6 - Remover Trem
7 - Engatar Vagão/Locomotiva no trem
8 - Desengatar Vagão/Locomotiva
9 - Esvaziar Garagem
10 - Esvaziar Trem
11 - Ver todos os vagões da garagem
12 - Ver todos as locomotivas da garagem
13 - Ver todos os trens da garagem
14 - Ver todos os veiculos da garagem
15 - Ver a quantidade de veiculos da garagem
16 - Encerrar programa
        '''
        View.mostrar_mensagem(menu)

    def pedir_dados(string):
        dado = input(f"{string}: ")
        return dado

    def mostrar_mensagem(mensagem):
        print(mensagem)

    def mostrar_itens_da_lista(lista):
        if not lista:
            View.mostrar_mensagem("Lista vazia")
        else:
            for item in lista:
                View.mostrar_mensagem(item)
