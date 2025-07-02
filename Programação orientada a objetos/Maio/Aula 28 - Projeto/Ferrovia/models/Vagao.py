class Vagao:
    id = 0

    def __init__(self, peso):
        self.id = Vagao.id
        self.peso = peso
        # passageiros = []
        # self.peso += passageiro.get_peso()

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
