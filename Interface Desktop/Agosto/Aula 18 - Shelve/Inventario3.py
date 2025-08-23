import shelve


class Item:
    def __init__(self, nome, tipo, dano):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano

    def get_nome(self):
        return self.nome


class Inventario:
    def __init__(self):
        self.itens = dict()

    def add_item(self, item):
        self.itens[item.get_nome()] = item

    def remove_item(self, nome):
        del self.itens[nome]

    # def get_item(self, nome):
    #     return self.itens[nome]

    def get_itens(self):
        return self.itens
    
    def __str__(self):
        return f"Inventario:\n {self.itens}"


class Cofre:
    def save(self, inventario: Inventario):
        with shelve.open('inventario.db') as db:
            db["inventario"] = inventario

    def read(self):
        with shelve.open('inventario.db') as db:
            inventario = db["inventario"]
        if inventario:
            return inventario
        return None

    def iterar(self, caminho):
        with shelve.open(caminho) as db:
            for chave in db:
                print(chave, db[chave])


cofre = Cofre()

try:
    inventario = cofre.read()
except KeyError:
    inventario = Inventario()


inventario.add_item(Item("espada", "arma", 10))
inventario.add_item(Item("picareta", "arma", 10))
inventario.add_item(Item("espada", "arma", 10))
inventario.add_item(Item("picareta2", "arma", 40))

cofre.save(inventario)
cofre.iterar('inventario.db')
