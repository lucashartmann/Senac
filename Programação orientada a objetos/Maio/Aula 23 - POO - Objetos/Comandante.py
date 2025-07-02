from DiscoVoador import DiscoVoador


class Comandante:
    def __init__(self):
        self.frota = {}
        self.frota["disco1"] = DiscoVoador()
        self.frota["disco2"] = DiscoVoador()

    def perseguir_sorrateiramente(self, vaca):
        disco = self.frota["disco1"]
        disco.potencia = 5
        disco.dispararLasers()
        disco.dispararLasers()
        disco.abduzir(vaca)

    def perseguir_ofensivamente(self, vaca):
        disco = self.frota["disco2"]
        disco.potencia = 30
        disco.dispararLasers()
        disco.dispararLasers()
        disco.dispararLasers()
        disco.abduzir(vaca)

    def relatorio(self):
        for nome, disco in self.frota.items():
            print(nome)
            disco.cutucar_vacas()
