class Aviao:
    def __init__(self, modelo):
        self.prefixo = ""
        self.modelo = modelo

class Modelo:
    
    def __init__(self, nome, capacidade, combustivel):
        self.nome = nome
        self.capacidade = capacidade
        self.combustivel = combustivel

frota = []

modelo1 = Modelo("765", 400, 1032.00)
modelo2 = Modelo("767", 500, 2032.00)
modelo3 = Modelo("745", 450, 1520.00)

aviao1 = Aviao(modelo1)
aviao2 = Aviao(modelo1)
aviao3 = Aviao(modelo2)
aviao4 = Aviao(modelo3)
aviao5 = Aviao(modelo3)

frota.append(aviao1)
frota.append(aviao2)
frota.append(aviao3)
frota.append(aviao4)
frota.append(aviao5)

for aviao in frota:
    print(f'pref: {aviao.prefixo} - Modelo: {aviao.modelo.nome}, capacidade: {aviao.modelo.capacidade}')
