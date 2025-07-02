from models.Cena import Cena

class Personagem():
    def __init__(self):
        self.sala = Cena("Entrada")
        self.inventario = dict()
        self.item_equipado = None

    def coletar_item(self, nome_item):
        item_coletado = self.sala.coletar_item(nome_item)
        self.inventario[nome_item] = item_coletado

    def equipar_item(self, nome_item):
        self.item_equipado = self.inventario[nome_item]

    def desequipar_item(self):
        self.item_equipado = None

    def soltar_item(self, nome_item):
        if self.item_equipado.nome == nome_item:
            self.desequipar_item()
        item_soltado = self.inventario[nome_item]
        self.sala.colocar_item(item_soltado, nome_item)
        del self.inventario[nome_item]

    def andar_norte(self):
        if self.sala.norte: # norte é uma Sala
            self.sala =self.sala.norte # minha sala atual é a sala que está ao meu norte
    
    def andar_sul(self):
        if self.sala.sul: # sul é uma Sala
            self.sala =self.sala.sul # minha sala atual é a sala que está ao meu sul

    def andar_leste(self):
        if self.sala.leste: # leste é uma Sala
            self.sala =self.sala.leste # minha sala atual é a sala que está ao meu leste

    def andar_oeste(self):
        if self.sala.oeste: # oeste é uma Sala
            self.sala =self.sala.oeste # minha sala atual é a sala que está ao meu oeste

    def atacar(self):
        pass

    def __str__(self):        
        return f'''
Classe do personagem: {type(self).__name__}
Inventário: {self.inventario}
Item equipado: {self.item_equipado}
Sala atual: {self.sala.nome}
'''

class Mago(Personagem):
    def atacar(self):
        if self.item_equipado.nome == "lanca":
            print(f"{self.item_equipado}: Zaaappp! Zuum!")

class Guerreiro(Personagem):
    def atacar(self):
        if self.item_equipado.nome == "espada":
            print(f"{self.item_equipado}: Classhh! Smashh!!!")
