import random

objetos = [
        {"nome": "Rocha", "genero": "f", "dano": 0, "protecao": 0},
        {"nome": "Espada", "genero": "f", "dano": 5, "protecao": 0},
        {"nome": "Capa", "genero": "f", "dano": 0, "protecao": 0},
        {"nome": "Foice", "genero": "f", "dano": 2, "protecao": 0},
        {"nome": "Capacete", "genero": "m", "dano": 0, "protecao": 5},
        {"nome": "Peitoral", "genero": "m", "dano": 0, "protecao": 5},
        {"nome": "Calça", "genero": "f", "dano": 0, "protecao": 5},
        {"nome": "Picareta", "genero": "f", "dano": 3, "protecao": 0},
        {"nome": "Machado", "genero": "m", "dano": 4, "protecao": 0},
        {"nome": "Cenoura", "genero": "f", "dano": 0, "protecao": 0},
        {"nome": "Gema", "genero": "f", "dano": 0, "protecao": 0},
        {"nome": "Moeda", "genero": "f", "dano": 0, "protecao": 0},
        {"nome": "lira", "genero": "f", "dano": 0, "protecao": 0}
    ]

adjetivos = [
        {"f": "Feroz", "m": "Feroz", "dano": 5, "protecao": 0},
        {"f": "Fulminante", "m": "Fulminante", "dano": 5, "protecao": 0},
        {"f": "Vingativa", "m": "Vingativo", "dano": 5, "protecao": 0},
        {"f": "Bela como a Lua", "m": "Belo como a Lua", "dano": 0, "protecao": 0},
        {"f": "Reluzente", "m": "Reluzente", "dano": 0, "protecao": 0},
        {"f": "Fervescente", "m": "Fervescente", "dano": 0, "protecao": 0}
    ]

complementos = [
        {"f": "Forjada na lua", "m": "Forjado na lua", "dano": 5, "protecao": 5},
        {"f": "do Minotauro", "m": "do Minotauro", "dano": 5, "protecao": 5},
        {"f": "dos confins do inferno",
            "m": "dos confins do inferno", "dano": 0, "protecao": 0},
        {"f": "Enferrujada", "m": "Enferrujado", "dano": -2, "protecao": -2},
        {"f": "Perfeita", "m": "Perfeito", "dano": 0, "protecao": 0},
        {"f": "Usada pelo Rei de Minas",
            "m": "Usado pelo Rei de Minas", "dano": 0, "protecao": 0}
    ]

icone_objeto = {
    "espada" : "🗡️",
    "machado" : "🪓",
    "picareta" : "⛏️",
    #"foice" : "",
    "escudo" : "🛡️",
    "calça" : "👖",
    "capacete" : "🪖",
    # "capa" : "",
    #"peitoral" : "",
    "rocha" : "🪨",
    "cenoura" : "🥕",
    "gema" : "💎",
    "moeda" : "🪙",
    #"lira" : "",
}

icone_adjetivo = {
    #"feroz" : "",
    "fulminante" : "💥",
    #"vingativo" : "",
    "belo como a lua" : "🌙",
    "reluzente" : "🌟",
}

icone_complemento = {
    "forjada na lua" : "🌙",
    #"do minotauro" : "",
    #"dos confins do inferno" : "🔥",
    #"enferrujada" : "",
    #"perfeita" : "",
}

import random

class Item:

    def __init__(self):
        self.dano = 0
        self.protecao = 0
        self.nome = str()
       
        self.objeto = random.choice(objetos)
        self.adjetivo = random.choice(adjetivos)
        self.complemento = random.choice(complementos)

        self.dano = self.objeto["dano"] + self.adjetivo["dano"] + self.complemento["dano"]
        
        self.protecao = self.objeto["protecao"] + self.adjetivo["protecao"] + self.complemento["protecao"]
        
        self.genero_objeto = self.objeto["genero"]
        
        
        self.nome = f"{self.objeto["nome"]} {self.adjetivo[self.genero_objeto]} {self.complemento[self.genero_objeto]}"

    def get_nome(self):
        return self.nome

    def set_dano(self, novo_Dano):
        self.dano = novo_Dano

    def get_dano(self):
        return self.dano

    def set_protecao(self, nova_protecao):
        self.protecao = nova_protecao

    def get_protecao(self):
        return self.protecao

    def __str__(self):
        if self.dano > 0:
            return f"Item [Nome: {self.get_nome()}, dano = {self.get_dano()}]"

        if self.protecao > 0:
            return f"Item [Nome: {self.get_nome()}, protecao = {self.protecao}]"

        if self.dano > 0 and self.protecao > 0:
            return f"Item [Nome: {self.get_nome()}, dano = {self.get_dano()}, protecao = {self.protecao}]"

        return f"Item [Nome: {self.get_nome()}"
