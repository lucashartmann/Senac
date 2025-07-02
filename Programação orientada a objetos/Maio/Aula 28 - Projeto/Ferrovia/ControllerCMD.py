from models import Locomotiva, Vagao, Trem, Garagem
import View


class ControllerCMD:

    garagem = Garagem.Garagem(900)

    def get_garagem():
        return ControllerCMD.garagem

    def init():
        locomotiva1 = Locomotiva.Locomotiva(100.0, 500.0)
        locomotiva2 = Locomotiva.Locomotiva(100.0, 500.0)
        ControllerCMD.get_garagem().estacionar(locomotiva1)
        ControllerCMD.get_garagem().estacionar(locomotiva2)

        vagao1 = Vagao.Vagao(200.0)
        vagao2 = Vagao.Vagao(500.0)
        vagao3 = Vagao.Vagao(100.0)
        ControllerCMD.get_garagem().estacionar(vagao1)
        ControllerCMD.get_garagem().estacionar(vagao2)
        ControllerCMD.get_garagem().estacionar(vagao3)

        trem1 = Trem.Trem()
        ControllerCMD.get_garagem().estacionar(trem1)

    def adicionar_vagao(peso):
        vagao = Vagao.Vagao(peso)
        cadastro = ControllerCMD.get_garagem().estacionar(vagao)
        str = ""
        if cadastro:
            View.View.mostrar_mensagem("Cadastro realizado com sucesso")
            View.View.mostrar_mensagem(vagao)
            str = f"Cadastrado realizado com sucesso!\n{vagao}"
        else:
            View.View.mostrar_mensagem(
                "ERRO. Não foi possivel realizar cadastro")
            str = "ERRO. Não foi possivel realizar cadastro"

        return str

    def adicionar_locomotiva(combustivel, peso):
        locomotiva = Locomotiva.Locomotiva(combustivel, peso)
        cadastro = ControllerCMD.get_garagem().estacionar(locomotiva)
        if cadastro:
            View.View.mostrar_mensagem("Cadastro realizado com sucesso")
            View.View.mostrar_mensagem(locomotiva)
        else:
            View.View.mostrar_mensagem(
                "ERRO. Não foi possivel realizar cadastro")

    def adicionar_trem():
        trem = Trem()
        cadastro = ControllerCMD.get_garagem().estacionar(trem)
        if cadastro:
            View.View.mostrar_mensagem("Cadastro realizado com sucesso")
            View.View.mostrar_mensagem(trem)
        else:
            View.View.mostrar_mensagem(
                "ERRO. Não foi possivel realizar cadastro")

    def remover(id):
        veiculo = ControllerCMD.get_garagem().get_veiculo_por_id(id)
        remocao = ControllerCMD.get_garagem().remove_veiculo(veiculo)
        if remocao:
            View.View.mostrar_mensagem(veiculo, "removido com sucesso")
        else:
            View.View.mostrar_mensagem(
                "ERRO. Não foi possivel remover", veiculo)

    def engatar(id_trem, id_veiculo):
        trem = ControllerCMD.get_garagem().get_veiculo_por_id(id_trem)
        if trem is None:
            View.View.mostrar_mensagem(f"Não existe trem com o id: {id_trem}")
            return
        else:
            veiculo = ControllerCMD.get_garagem().get_veiculo_por_id(id_veiculo)
            if type(veiculo) == Vagao.Vagao:
                if trem.possui_locomotiva() == False:
                    View.View.mostrar_mensagem(
                        "ERRO. Não é possivel engatar um vagão em um trem sem locomotiva")
                    return
            if veiculo is None:
                View.View.mostrar_mensagem(
                    f"Não existe veiculo com o id: {id_veiculo}")
                return
            engatado = trem.engatar(veiculo)
            if engatado:
                ControllerCMD.get_garagem().remove_veiculo(veiculo)
                View.View.mostrar_mensagem(veiculo, "engatado com sucesso!")
            else:
                View.View.mostrar_mensagem("ERRO ao engatar", veiculo)

    def desengatar(id_trem, id_veiculo):
        trem = ControllerCMD.get_garagem().get_veiculo_por_id(id_trem)
        if trem is None:
            View.View.mostrar_mensagem(f"Não existe trem com o id: {id_trem}")
            return
        veiculo = ControllerCMD.get_garagem().get_veiculo_por_id(id_veiculo)
        if veiculo is None:
            View.View.mostrar_mensagem(
                f"Não existe veiculo com o id: {id_veiculo}")
            return
        desengatado = trem.desengatar(veiculo)
        if desengatado:
            ControllerCMD.get_garagem().estacionar(veiculo)
            View.View.mostrar_mensagem(veiculo, "desengatado com sucesso!")
        else:
            View.View.mostrar_mensagem("ERRO ao desengatar", veiculo)

    def remover_trens_da_garagem():
        remocao = ControllerCMD.get_garagem().remover_todos_trens()
        View.View.mostrar_mensagem("Trens removidos com sucesso")
        View.View.mostrar_mensagem("TRENS NA GARAGEM:")
        View.View.mostrar_mensagem(
            ControllerCMD.get_garagem().get_lista_trens())

    def remover_locomotivas_da_garagem():
        ControllerCMD.get_garagem().remover_todas_locomotivas()
        View.View.mostrar_mensagem("Locomotivas removidas com sucesso")
        View.View.mostrar_mensagem("LOCOMOTIVAS NA GARAGEM:")
        View.View.mostrar_mensagem(
            ControllerCMD.get_garagem().get_lista_locomotivas())

    def remover_vagoes_da_garagem():
        ControllerCMD.get_garagem().remover_todos_vagoes()
        View.View.mostrar_mensagem("Vagões removidos com sucesso")
        View.View.mostrar_mensagem("VAGÕES NA GARAGEM:")
        View.View.mostrar_mensagem(
            ControllerCMD.get_garagem().get_lista_vagoes())

    def esvaziar_trem(id):
        trem = ControllerCMD.get_garagem().get_veiculo_por_id(id)
        if trem is None:
            View.View.mostrar_mensagem(f"Não existe trem com o id: {id}")
            return
        trem.esvaziar()
        View.View.mostrar_mensagem("Trem esvaziado com sucesso!", trem)

    def listar_trens():
        View.View.mostrar_mensagem("TRENS NA GARAGEM:")
        View.View.mostrar_mensagem(
            ControllerCMD.ControllerCMD.get_garagem().get_lista_trens())

    def listar_locomotivas():
        View.View.mostrar_mensagem("LOCOMOTIVAS NA GARAGEM:")
        View.View.mostrar_mensagem(
            ControllerCMD.get_garagem().get_lista_locomotivas())

    def listar_vagoes():
        View.View.mostrar_mensagem("VAGÕES NA GARAGEM:")
        View.View.mostrar_mensagem(
            ControllerCMD.get_garagem().get_lista_vagoes())

    def listar_veiculos():
        veiculos = ControllerCMD.get_garagem().get_veiculos_ferroviarios()
        if not veiculos:
            View.View.mostrar_mensagem("Não há veículos na garagem")
        else:
            View.View.mostrar_mensagem("VEÍCULOS NA GARAGEM:")
            View.View.mostrar_itens_da_lista(veiculos)
