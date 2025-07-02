class Caneta():
    def escrever(self):
        print("Escrevendo....")

class Marcador(Caneta):
    def apagar(self):
        print("Marcador apagando...")

class Lapis(Caneta):
    def escrever(self):
        super().escrever()
        print("Rabiscando...")

m = Marcador()
m.escrever()
m.apagar()

l = Lapis()
l.escrever()
