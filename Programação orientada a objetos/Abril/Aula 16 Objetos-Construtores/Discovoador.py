class Discovoador:
    def __init__(self):
        self.vacas = []
        self.velocidade = 0
    
    def acelerar(self):
        if self.velocidade < 10:
            self.velocidade += 1    
        return self.velocidade

    def frear(self):
        self.velocidade = 0
        return self.velocidade

    def abduzir(self, vaca):
        if vaca not in self.vacas:
            self.vacas.append(vaca)
            return True
        return False