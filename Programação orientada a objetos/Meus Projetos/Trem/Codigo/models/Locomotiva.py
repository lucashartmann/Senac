class Locomotiva:
    id = 0

    def __init__(self, quant_combustivel, peso):
        self.id = Locomotiva.id
        self.quant_combustivel = quant_combustivel
        self.peso = peso
        self.potencia = 0
        tipo_combustivel = ""

    def gerar_id(self):
        Locomotiva.id += 1
        return Locomotiva.id

    def get_peso(self):
        try:
            return self.peso
        except AttributeError:
            return 0

    def get_quant_combustivel(self):
        try:
            return self.quant_combustivel
        except AttributeError:
            return 0

    def get_id(self):
        try:
            return self.id
        except AttributeError:
            return 0

    def __str__(self):
        return f"Locomotiva [id = {self.get_id()}, combustivel = {self.get_quant_combustivel()}, peso = {self.get_peso()}]"
