from models import Locomotiva, Vagao, Trem, Garagem
import view.View as View


class Controller:

    garagem = Garagem.Garagem(900)

    def get_garagem():
        return Controller.garagem

    def init():
        locomotiva1 = Locomotiva.Locomotiva(100.0, 500.0)
        locomotiva2 = Locomotiva.Locomotiva(100.0, 500.0)
        Controller.get_garagem().estacionar(locomotiva1)
        Controller.get_garagem().estacionar(locomotiva2)

        vagao1 = Vagao.Vagao(200.0)
        vagao2 = Vagao.Vagao(500.0)
        vagao3 = Vagao.Vagao(100.0)
        Controller.get_garagem().estacionar(vagao1)
        Controller.get_garagem().estacionar(vagao2)
        Controller.get_garagem().estacionar(vagao3)

        trem1 = Trem.Trem()
        Controller.get_garagem().estacionar(trem1)

    def cadastro(opcao):
        if opcao == 3:
            veiculo = Trem.Trem()
            cadastro = Controller.get_garagem().estacionar(veiculo)
        else:
            peso = float(View.View.pedir_dados("Digite o peso"))
            if opcao == 1:
                veiculo = Vagao.Vagao(peso)
                cadastro = Controller.get_garagem().estacionar(veiculo)
            else:
                combustivel = float(View.View.pedir_dados(
                    "Digite a quantidade de combustivel"))
                veiculo = Locomotiva.Locomotiva(combustivel, peso)
                cadastro = Controller.get_garagem().estacionar(veiculo)

        if cadastro:
            View.View.mostrar_mensagem("Cadastro realizado com sucesso")
            View.View.mostrar_mensagem(veiculo)
        else:
            View.View.mostrar_mensagem(
                "ERRO. Não foi possivel realizar cadastro")

    def remocao(opcao):
        id = int(View.View.pedir_dados("Digite id do veiculo"))
        if opcao == 4:
            vagao = Controller.get_garagem().get_veiculo_por_id(id)
            remocao = Controller.get_garagem().remove_veiculo(vagao)
        elif opcao == 5:
            locomotiva = Controller.get_garagem().get_veiculo_por_id(id)
            remocao = Controller.get_garagem().remove_veiculo(locomotiva)
        else:
            trem = Controller.get_garagem().get_veiculo_por_id(id)
            remocao = Controller.get_garagem().remove_veiculo(trem)

        if remocao:
            View.View.mostrar_mensagem("Veiculo removido com sucesso")
        else:
            View.View.mostrar_mensagem(
                "ERRO. Não foi possivel remover veiculo")

    def engatar_no_trem():
        id = int(View.View.pedir_dados("Digite id do trem"))
        trem = Controller.get_garagem().get_veiculo_por_id(id)
        if trem is None:
            View.View.mostrar_mensagem(f"Não existe trem com o id: {id}")
            return
        id = int(View.View.pedir_dados("Digite id do veiculo"))
        veiculo = Controller.get_garagem().get_veiculo_por_id(id)
        if type(veiculo) == Vagao.Vagao:
            if trem.possui_locomotiva() == False:
                View.View.mostrar_mensagem(
                    "ERRO. Não é possivel engatar um vagão em um trem sem locomotiva")
                return
        if veiculo is None:
            View.View.mostrar_mensagem(f"Não existe veiculo com o id: {id}")
            return
        trem.engatar(veiculo)
        Controller.get_garagem().remove_veiculo(veiculo)

    def desengatar():
        id = int(View.View.pedir_dados("Digite id do trem"))
        trem = Controller.get_garagem().get_veiculo_por_id(id)
        if trem is None:
            View.View.mostrar_mensagem(f"Não existe trem com o id: {id}")
            return
        id = int(View.View.pedir_dados("Digite id do veiculo"))
        veiculo = Controller.get_garagem().get_veiculo_por_id(id)
        if veiculo is None:
            View.View.mostrar_mensagem(f"Não existe veiculo com o id: {id}")
            return
        trem.desengatar(veiculo)
        Controller.get_garagem().estacionar(veiculo)

    def esvaziar_garagem():
        opcao = int(View.View.pedir_dados(
            "Selecione 1 - Vagao, 2 - Locomotiva, 3 - Trem: "))
        if opcao == 1:
            Controller.Controller.get_garagem().remover_todos_vagoes()
            View.View.mostrar_mensagem("Vagões removidos com sucesso")
            View.View.mostrar_mensagem("VAGÕES NA GARAGEM:")
            View.View.mostrar_mensagem(
                Controller.Controller.get_garagem().get_lista_vagoes())
        elif opcao == 2:
            Controller.Controller.garagem.remover_todas_locomotivas()
            View.View.mostrar_mensagem(
                "Locomotivas removidas com sucesso")
            View.View.mostrar_mensagem(
                "LOCOMOTIVAS NA GARAGEM:")
            View.View.mostrar_mensagem(
                Controller.Controller.get_garagem().get_lista_locomotivas())
        else:
            Controller.Controller.get_garagem().remover_todos_trens()
            View.View.mostrar_mensagem("Trens removidos com sucesso")
            View.View.mostrar_mensagem("TRENS NA GARAGEM:")
            View.View.mostrar_mensagem(
                Controller.Controller.get_garagem().get_lista_trens())

    def esvaziar_trem():
        id = int(View.View.pedir_dados("Digite o id do trem"))
        trem = Controller.Controller.get_garagem().get_veiculo_por_id(id)
        if trem is None:
            View.View.mostrar_mensagem(
                f"Não existe trem com o id: {id}")
            return
        trem.esvaziar()
        View.View.mostrar_mensagem("Trem esvaziado com sucesso!")
        View.View.mostrar_mensagem(trem)

    def listar_vagoes_garagem():
        vagoes = Controller.Controller.get_garagem().get_lista_vagoes()
        if not vagoes:
            View.View.mostrar_mensagem(
                "Não há vagões na garagem")
        else:
            View.View.mostrar_mensagem("VAGÕES NA GARAGEM:")
            View.View.mostrar_itens_da_lista(vagoes)

    def listar_locomotivas_garagem():
        locomotivas = Controller.Controller.get_garagem().get_lista_locomotivas()
        if not locomotivas:
            View.View.mostrar_mensagem(
                "Não há locomotivas na garagem")
        else:
            View.View.mostrar_mensagem(
                "LOCOMOTIVAS NA GARAGEM:")
            View.View.mostrar_itens_da_lista(locomotivas)

    def listar_trens_garagem():
        trens = Controller.Controller.get_garagem().get_lista_trens()
        if not trens:
            View.View.mostrar_mensagem(
                "Não há trens na garagem")
        else:
            View.View.mostrar_mensagem("TRENS NA GARAGEM:")
            View.View.mostrar_itens_da_lista(trens)

    def listar_veiculos_garagem():
        veiculos = Controller.Controller.get_garagem().get_veiculos_ferroviarios()
        if not veiculos:
            View.View.mostrar_mensagem(
                "Não há veículos na garagem")
        else:
            View.View.mostrar_mensagem(
                "VEÍCULOS NA GARAGEM:")
            View.View.mostrar_itens_da_lista(veiculos)

    def get_quant_veiculos_na_garagem():
        View.View.mostrar_mensagem(
            f"Quantidade de veículos na garagem: {Controller.get_quant_veiculos_na_garagem()}")
