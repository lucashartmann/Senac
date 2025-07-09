from models import Locomotiva, Vagao, Trem, Garagem
import view.View as View


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
        trem2 = Trem.Trem()
        ControllerCMD.get_garagem().estacionar(trem1)
        ControllerCMD.get_garagem().estacionar(trem2)
        
        trem2.engatar(locomotiva2)
        trem2.engatar(vagao2)
        trem2.engatar(vagao3)
        ControllerCMD.get_garagem().remove_veiculo(locomotiva2)
        ControllerCMD.get_garagem().remove_veiculo(vagao2)
        ControllerCMD.get_garagem().remove_veiculo(vagao3)

    def adicionar_vagao(peso):
        vagao = Vagao.Vagao(peso)
        cadastro = ControllerCMD.get_garagem().estacionar(vagao)
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
            str = f"Cadastro realizado com sucesso!\n{locomotiva}"
        else:
            View.View.mostrar_mensagem(
                "ERRO. Não foi possivel realizar cadastro")
            str = "ERRO. Não foi possivel realizar cadastro"
        return str

    def adicionar_trem():
        trem = Trem.Trem()
        cadastro = ControllerCMD.get_garagem().estacionar(trem)
        if cadastro:
            View.View.mostrar_mensagem("Cadastro realizado com sucesso")
            View.View.mostrar_mensagem(trem)
            str = f"Cadastro realizado com sucesso!\n{trem}"
        else:
            View.View.mostrar_mensagem(
                "ERRO. Não foi possivel realizar cadastro")
            str = "ERRO. Não foi possivel realizar cadastro"
        return str

    def remover(id):
        veiculo = ControllerCMD.get_garagem().get_veiculo_por_id(id)
        remocao = ControllerCMD.get_garagem().remove_veiculo(veiculo)
        if remocao:
            View.View.mostrar_mensagem(veiculo, "removido com sucesso")
            str = f"{veiculo} removido com sucesso!"
        else:
            View.View.mostrar_mensagem(
                "ERRO. Não foi possivel remover", veiculo)
            str = f"ERRO. Não foi possivel remover {veiculo}"
        return str

    def engatar(id_trem, id_veiculo):
        trem = ControllerCMD.get_garagem().get_veiculo_por_id(id_trem)
        if trem is None:
            View.View.mostrar_mensagem(f"Não existe trem com o id: {id_trem}")
            return f"Não existe trem com o id: {id_trem}"
        else:
            veiculo = ControllerCMD.get_garagem().get_veiculo_por_id(id_veiculo)
            if type(veiculo) == Vagao.Vagao:
                if trem.possui_locomotiva() == False:
                    View.View.mostrar_mensagem(
                        "ERRO. Não é possivel engatar um vagão em um trem sem locomotiva")
                    return "ERRO. Não é possivel engatar um vagão em um trem sem locomotiva"
            if veiculo is None:
                View.View.mostrar_mensagem(
                    f"Não existe veiculo com o id: {id_veiculo}")
                return f"Não existe veiculo com o id: {id_veiculo}"
            engatado = trem.engatar(veiculo)
            if engatado:
                ControllerCMD.get_garagem().remove_veiculo(veiculo)
                View.View.mostrar_mensagem(f"{veiculo}, engatado com sucesso!")
                return f"{veiculo}, engatado com sucesso!"
            else:
                View.View.mostrar_mensagem(f"ERRO ao engatar {veiculo}")
                return f"ERRO ao engatar {veiculo}"

    def desengatar(id_trem, id_veiculo):
        trem = ControllerCMD.get_garagem().get_veiculo_por_id(id_trem)
        if trem is None:
            View.View.mostrar_mensagem(f"Não existe trem com o id: {id_trem}")
            return
        veiculo = trem.get_veiculo_por_id(id_veiculo)
        if veiculo is None:
            View.View.mostrar_mensagem(
                f"Não existe veiculo com o id: {id_veiculo}")
            return f"Não existe veiculo com o id: {id_veiculo}"
        desengatado, lista = trem.desengatar(veiculo)
        if lista is not None:
            for veiculo_na_lista in lista:
                ControllerCMD.get_garagem().estacionar(veiculo_na_lista)
        if desengatado:
            View.View.mostrar_mensagem(f"{veiculo}, desengatado com sucesso!")
            return f"{veiculo}, desengatado com sucesso!"
        else:
            View.View.mostrar_mensagem(f"ERRO ao desengatar, {veiculo}")
            return f"ERRO ao desengatar, {veiculo}"

    def remover_trens_da_garagem():
        remocao = ControllerCMD.get_garagem().remover_todos_trens()
        View.View.mostrar_mensagem("Trens removidos com sucesso")
        View.View.mostrar_mensagem("TRENS NA GARAGEM:")
        View.View.mostrar_itens_da_lista(
            ControllerCMD.get_garagem().get_lista_trens())

    def remover_locomotivas_da_garagem():
        ControllerCMD.get_garagem().remover_todas_locomotivas()
        View.View.mostrar_mensagem("Locomotivas removidas com sucesso")
        View.View.mostrar_mensagem("LOCOMOTIVAS NA GARAGEM:")
        View.View.mostrar_itens_da_lista(
            ControllerCMD.get_garagem().get_lista_locomotivas())

    def remover_vagoes_da_garagem():
        ControllerCMD.get_garagem().remover_todos_vagoes()
        View.View.mostrar_mensagem("Vagões removidos com sucesso")
        View.View.mostrar_mensagem("VAGÕES NA GARAGEM:")
        View.View.mostrar_itens_da_lista(
            ControllerCMD.get_garagem().get_lista_vagoes())

    def esvaziar_trem(id):
        trem = ControllerCMD.get_garagem().get_veiculo_por_id(id)
        if trem is None:
            View.View.mostrar_mensagem(f"Não existe trem com o id: {id}")
            return f"Não existe trem com o id: {id}"
        trem.esvaziar()
        View.View.mostrar_mensagem(f"Trem esvaziado com sucesso!, {trem}")
        return f"Trem esvaziado com sucesso!, {trem}"

    def listar_trens_garagem():
        trens = ControllerCMD.get_garagem().get_lista_trens()
        if ControllerCMD.get_garagem().get_quant_trens() == 0:
            View.View.mostrar_mensagem("Não há trens na garagem")
            return "Não há trens na garagem"
        View.View.mostrar_mensagem("TRENS NA GARAGEM:")
        View.View.mostrar_itens_da_lista(trens)
        return "\n".join(str(trem) for trem in trens)

    def listar_locomotivas_garagem():
        lista_locomotivas = ControllerCMD.get_garagem().get_lista_locomotivas()
        if ControllerCMD.get_garagem().get_quant_locomotivas() == 0:
            View.View.mostrar_mensagem("Não há locomotivas na garagem")
            return "Não há locomotivas na garagem"
        View.View.mostrar_mensagem("LOCOMOTIVAS NA GARAGEM:")
        View.View.mostrar_itens_da_lista(lista_locomotivas)
        return "\n".join(str(locomotiva) for locomotiva in lista_locomotivas)

    def listar_vagoes_garagem():
        vagoes = ControllerCMD.get_garagem().get_lista_vagoes()
        if ControllerCMD.get_garagem().get_quant_vagoes() == 0:
            View.View.mostrar_mensagem("Não há vagões na garagem")
            return "Não há vagões na garagem"
        View.View.mostrar_mensagem("VAGÕES NA GARAGEM:")
        View.View.mostrar_itens_da_lista(vagoes)
        return "\n".join(str(vagao) for vagao in vagoes)

    def listar_veiculos_garagem():
        veiculos = ControllerCMD.get_garagem().get_veiculos_ferroviarios()
        if not veiculos:
            View.View.mostrar_mensagem("Não há veículos na garagem")
            return "Não há veículos na garagem"
        View.View.mostrar_mensagem("VEÍCULOS NA GARAGEM:")
        View.View.mostrar_itens_da_lista(veiculos)
        return "\n".join(str(veiculo) for veiculo in veiculos)

    def get_quant_locomotivas_garagem():
        quant = ControllerCMD.get_garagem().get_quant_locomotivas()
        if quant == 0:
            return "Não há locomotivas na garagem"
        return f"Quantidade de locomotivas na garagem: {quant}"

    def get_quant_vagoes_garagem():
        quant = ControllerCMD.get_garagem().get_quant_vagoes()
        if quant == 0:
            return "Não há vagões na garagem"
        return f"Quantidade de vagões na garagem: {quant}"

    def get_quant_trens_garagem():
        quant = ControllerCMD.get_garagem().get_quant_trens()
        if quant == 0:
            return "Não há trens na garagem"
        return f"Quantidade de trens na garagem: {quant}"

    def get_quant_veiculos_garagem():
        quant = ControllerCMD.get_garagem().get_quant_veiculos()
        if quant == 0:
            return "Não há veículos na garagem"
        return f"Quantidade de veículos na garagem: {quant}"

    def get_quant_locomotivas_trem():
        trem = ControllerCMD.get_garagem().get_trem()
        if trem is None:
            return "Não há trens na garagem"
        quant = trem.get_quant_locomotivas()
        if quant == 0:
            return "Não há locomotivas no trem"
        return f"Quantidade de locomotivas no trem: {quant}"

    def get_quant_vagoes_trem():
        trem = ControllerCMD.get_garagem().get_trem()
        if trem is None:
            return "Não há trens na garagem"
        quant = trem.get_quant_vagoes()
        if quant == 0:
            return "Não há vagões no trem"
        return f"Quantidade de vagões no trem: {quant}"

    def listar_locomotivas_trem():
        trem = ControllerCMD.get_garagem().get_trem()
        if trem is None:
            View.View.mostrar_mensagem("Não há trens na garagem")
            return "Não há trens na garagem"
        locomotivas = trem.get_locomotivas()
        if not locomotivas:
            View.View.mostrar_mensagem("Não há locomotivas no trem")
            return "Não há locomotivas no trem"
        else:
            View.View.mostrar_mensagem("LOCOMOTIVAS NO TREM:")
            View.View.mostrar_itens_da_lista(locomotivas)
            return "\n".join(str(locomotiva) for locomotiva in locomotivas)
        
    def listar_vagoes_trem():
        trem = ControllerCMD.get_garagem().get_trem()
        if trem is None:
            View.View.mostrar_mensagem("Não há trens na garagem")
            return "Não há trens na garagem"
        vagoes = trem.get_vagoes()
        if not vagoes:
            View.View.mostrar_mensagem("Não há vagões no trem")
            return "Não há vagões no trem"
        else:
            View.View.mostrar_mensagem("VAGÕES NO TREM:")
            View.View.mostrar_itens_da_lista(vagoes)
            return "\n".join(str(vagao) for vagao in vagoes)

    def listar_veiculos_trem_por_id(id):
        trem = ControllerCMD.get_garagem().get_veiculo_por_id(id)
        if trem is None:
            View.View.mostrar_mensagem("Não há trens na garagem")
            return "Não há trens na garagem"
        veiculos = trem.get_veiculos()
        if not veiculos:
            View.View.mostrar_mensagem("Não há veículos no trem")
            return "Não há veículos no trem"
        else:
            View.View.mostrar_mensagem("VEÍCULOS NO TREM:")
            View.View.mostrar_itens_da_lista(veiculos)
            return "\n".join(str(veiculo) for veiculo in veiculos)
