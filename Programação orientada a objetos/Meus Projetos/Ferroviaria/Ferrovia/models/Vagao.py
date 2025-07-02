class Vagao:
    id = 0

    def __init__(self, peso):
        self.id = Vagao.id
        self.peso_max = 0
        self.peso = peso
        self.peso_atual = 0
        self.quant_passageiros = 0
        self.quant_assentos = 0

    def carregar(self, carga):
        self.peso_atual += carga

    def descarregar(self, carga):
        self.peso_atual -= carga

    def get_peso(self):
        try:
            return self.peso
        except AttributeError:
            return 0

    def get_id(self):
        try:
            return self.id
        except AttributeError:
            return 0

    def __str__(self):
        return f"Vagao [id = {self.get_id()}, peso = {self.get_peso()}]"
