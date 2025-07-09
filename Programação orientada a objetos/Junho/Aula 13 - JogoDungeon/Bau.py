import random
import Item

class Bau:
     
    def __init__(self):
        self.itens_no_bau = []
        self.init()
  
    def init(self):
        quant_itens_no_bau = int(random.randrange(0, 10))

        for i in range(quant_itens_no_bau):
            item = Item.Item()
            quant_certo_item = int(random.randrange(0, 5))
            if item not in self.itens_no_bau:
                item.set_quant(quant_certo_item)
                self.itens_no_bau.append(item)
                i += 1

    def get_lista_itens(self):
        return Bau.itens
    
    def get_itens_no_bau(self):
        return self.itens_no_bau

    def __str__(self):
        return f"###ITENS NO BAÚ#### \n{"\n".join(str(item) for item in self.get_itens_no_bau())}"