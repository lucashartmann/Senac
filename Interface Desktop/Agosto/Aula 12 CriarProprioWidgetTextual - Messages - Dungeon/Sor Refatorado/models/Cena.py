class Cena():
    def __init__(self, nome="Indefinida"):
        # identificação
        self.nome = nome

        # propriedades
        self.itens = dict()

        # Para o mapa: Cenas conectadas a esta cena
        self.norte = None
        self.sul = None
        self.leste = None
        self.oeste = None
