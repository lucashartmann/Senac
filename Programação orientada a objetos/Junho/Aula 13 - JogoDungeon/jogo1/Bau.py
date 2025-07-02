import random

class Bau:
    quant = int(random.randrange(0, 5))
    itens = []
     
    def __init__(self):
        self.itens_no_bau = []
        self.init()
  
    def init(self):
        quant_itens = int(random.randrange(0, 10))
        qaunt_itens_add = int(random.randrange(0, 5))

        for i in range(qaunt_itens_add):
            item = random.choice(Bau.itens)
            if item not in self.itens_no_bau:
                item.set_quant(quant_itens)
                self.itens_no_bau.append(item)
                i += 1


    def get_lista_itens(self):
        return Bau.itens
    
    def get_itens_no_bau(self):
        return self.itens_no_bau

    def __str__(self):
        return f"Baú [{" ".join(str(item) for item in self.get_itens_no_bau())}]"