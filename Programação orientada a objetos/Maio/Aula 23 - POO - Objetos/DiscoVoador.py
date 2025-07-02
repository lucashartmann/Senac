import Vaca


class DiscoVoador:
    def __init__(self):
        self.carga = 100
        self.potencia = 10
        self.celeiro = []

    def dispararLasers(self):
        self.carga -= self.potencia
        print("Piuu!!" + ('-' * self.potencia) + ">")

    def abduzir(self, vaca):
        self.celeiro.append(vaca)
        print(vaca.nome, "abduzida com sucesso")

    def cutucar_vacas(self):
        for vaca in self.celeiro:
            vaca.mugir()
