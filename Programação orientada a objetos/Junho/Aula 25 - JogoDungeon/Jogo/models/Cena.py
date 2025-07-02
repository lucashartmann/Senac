class Cena():
    def __init__(self, nome="Indefinida"):
        # identificação
        self.nome = nome

        self.itens = dict()

        # Cenas conectadas a esta cena
        self.norte = None
        self.sul = None
        self.leste = None
        self.oeste = None

    def colocar_item(self, um_item):
        self.itens[um_item.nome] = um_item

    def coletar_item(self, nome_item):
        # pegamos o item
        item_coletado = self.itens[nome_item]
        # retirar item da sala
        del self.itens[nome_item]
        # retornamos o item
        return item_coletado

    def __str__(self):
        return f'''
[{self.nome}]
Itens: {self.itens}
'''