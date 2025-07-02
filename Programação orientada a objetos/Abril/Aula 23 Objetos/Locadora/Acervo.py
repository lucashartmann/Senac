class Acervo:
    
    def __init__(self):
        self.midias = []
      
    def addMidia(self, midia):
        self.midias.append(midia)

    def removeMidia(self, midia):
        self.midias.remove(midia)