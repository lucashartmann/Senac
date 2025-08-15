import csv


class Item:
    def __init__(self, nome, tipo, dano):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano

    def get_nome(self):
        return self.nome

    def as_dict(self):
        return {"nome": self.nome, "tipo": self.tipo, "dano": self.dano}


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

    def as_list(self):
        itens = list()
        for item in self.itens.values():
            itens.append(item.as_dict())
        return itens


class Cofre:
    def save(self, inventario: Inventario):
        with open(f'inventario.csv', 'w', newline='', encoding='utf-8') as arquivo:
            campos = ['nome', 'tipo', 'dano']
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(inventario.as_list())

    def read(self):
        inventario = Inventario()
        with open('inventario.csv', 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                nome, tipo, dano = linha.values()
                inventario.add_item(
                    Item(nome, tipo, dano))
        return inventario


inventario = Inventario()
cofre = Cofre()

inventario.add_item(Item("espada", "arma", 10))
inventario.add_item(Item("picareta", "arma", 10))
inventario.add_item(Item("espada", "arma", 10))
inventario.add_item(Item("picareta2", "arma", 40))

inventario.remove_item("picareta2")

cofre.read()

print(inventario.get_itens())
