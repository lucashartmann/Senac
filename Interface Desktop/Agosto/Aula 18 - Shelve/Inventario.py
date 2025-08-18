import shelve


class Item:
    def __init__(self, nome, tipo, dano):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano


item1 = Item("espada", "arma", 10)
item2 = Item("picareta", "arma", 10)



with shelve.open('inventario.db') as db:
    db["espada"] = item1
    db["picareta"] = item2
