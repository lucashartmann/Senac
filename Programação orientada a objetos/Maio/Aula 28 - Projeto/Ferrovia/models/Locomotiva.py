class Locomotiva:
    id = 0

    def __init__(self, quant_combustivel, peso):
        self.id = self.gerar_id()
        self.quant_combustivel = quant_combustivel
        self.peso = peso
        # potencia

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
        return f"Locomotiva [id = {self.get_id()}, peso = {self.get_peso()}]"
