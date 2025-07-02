from models import Locomotiva, Vagao, Trem


class Garagem:

    id = 0

    def __init__(self, capacidade):
        self.veiculos_ferroviarios = []
        self.capacidade = capacidade
        self.quant_veiculos_ferroviarios = 0

    def estacionar(self, veiculo):
        if veiculo not in self.veiculos_ferroviarios and self.capacidade >= self.quant_veiculos_ferroviarios:
            self.veiculos_ferroviarios.append(veiculo)
            self.quant_veiculos_ferroviarios += 1
            Garagem.id += 1
            veiculo.id = Garagem.id
            return True
        return False

    def remove_veiculo(self, veiculo):
        try:
            self.veiculos_ferroviarios.remove(veiculo)
            return True
        except ValueError:
            return False

    def remover_todos_trens(self):
        for veiculo in self.veiculos_ferroviarios:
            if type(veiculo) == Trem.Trem:
                self.veiculos_ferroviarios.remove(veiculo)

    def remover_todas_locomotivas(self):
        for veiculo in self.veiculos_ferroviarios:
            if type(veiculo) == Locomotiva.Locomotiva:
                self.veiculos_ferroviarios.remove(veiculo)

    def remover_todos_vagoes(self):
        for veiculo in self.veiculos_ferroviarios:
            if type(veiculo) == Vagao.Vagao:
                self.veiculos_ferroviarios.remove(veiculo)

    def get_veiculos_ferroviarios(self):
        return self.veiculos_ferroviarios

    def get_capacidade(self):
        return self.capacidade

    def get_quant_veiculos_ferroviarios(self):
        return self.get_quant_veiculos_ferroviarios

    def get_veiculo_por_id(self, id):
        for veiculo in self.get_veiculos_ferroviarios:
            if veiculo.get_id() == id:
                return veiculo
        return None

    def esvaziar_garagem(self):
        self.veiculos_ferroviarios.clear()

    def get_lista_trens(self):
        trens_na_garagem = []
        for veiculo in self.veiculos_ferroviarios:
            if type(veiculo) == Trem.Trem:
                trens_na_garagem.append(veiculo)
        return trens_na_garagem

    def get_lista_locomotivas(self):
        locomotivas_na_garagem = []
        for veiculo in self.veiculos_ferroviarios:
            if type(veiculo) == Locomotiva.Locomotiva:
                locomotivas_na_garagem.append(veiculo)
        return locomotivas_na_garagem

    def get_lista_vagoes(self):
        vagoes_na_garagem = []
        for veiculo in self.veiculos_ferroviarios:
            if type(veiculo) == Vagao.Vagao:
                vagoes_na_garagem.append(veiculo)
        return vagoes_na_garagem
