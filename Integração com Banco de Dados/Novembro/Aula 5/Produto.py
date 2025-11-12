class Produto:
    def __init__(self, nome, valor, quantidade):
        self.id = None
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
        
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, value):
        self.nome = value

    def get_valor(self):
        return self.valor

    def set_valor(self, value):
        self.valor = value

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, value):
        self.quantidade = value


    def to_dict(self):
        return {"nome": self.nome,
                "valor": self.valor,
                "quantidade": self.quantidade
                }
