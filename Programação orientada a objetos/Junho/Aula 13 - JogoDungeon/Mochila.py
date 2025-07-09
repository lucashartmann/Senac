class Mochila:

    def __init__(self):
        self.mochila = []

    def get_mochila(self):
        return self.mochila

    def esvaziar(self):
        self.get_mochila().clear()

    def guardar(self, item):
        if len(self.mochila) < 10 and item not in self.mochila:
            self.mochila.append(item)
            return True
        return False
