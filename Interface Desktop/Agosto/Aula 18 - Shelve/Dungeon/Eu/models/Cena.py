class Cena():
    def __init__(self, nome="Indefinida"):
        self.nome = nome
        self.itens = dict()
        self.norte = None
        self.sul = None
        self.leste = None
        self.oeste = None

    def pegar_item(self, item):
        del Cena.CENA_ATUAL.itens[item]
