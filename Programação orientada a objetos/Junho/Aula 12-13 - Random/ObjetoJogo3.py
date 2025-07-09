import random

objetos = [
    {"nome": "Rocha", "genero": "f"},
    {"nome": "Espada", "genero": "f"},
    {"nome": "Capa", "genero": "f"},
    {"nome": "Foice", "genero": "f"},
    {"nome": "Capacete", "genero": "m"},
    {"nome": "Peitoral", "genero": "m"},
    {"nome": "Calça", "genero": "f"},
    {"nome": "Picareta", "genero": "f"},
    {"nome": "Machado", "genero": "m"},
    {"nome": "Cenoura", "genero": "f"},
    {"nome": "Gema", "genero": "f"},
    {"nome": "Moeda", "genero": "f"}
]

adjetivos = [
    {"f": "Feroz", "m": "Feroz"},
    {"f": "Fulminante", "m": "Fulminante"},
    {"f": "Vingativa", "m": "Vingativo"},
    {"f": "Bela como a Lua", "m": "Belo como a Lua"},
    {"f": "Reluzente", "m": "Reluzente"},
    {"f": "Fervescente", "m": "Fervescente"}
]

complementos = [
    {"f": "Forjada na lua", "m": "Forjado na lua"},
    {"f": "do Minotauro", "m": "do Minotauro"},
    {"f": "dos confins do inferno", "m": "dos confins do inferno"},
    {"f": "Enferrujada", "m": "Enferrujado"},
    {"f": "Perfeita", "m": "Perfeito"},
    {"f": "Usada pelo Rei de Minas", "m": "Usado pelo Rei de Minas"}
]


def gerar_nome():
    objeto = random.choice(objetos)
    adjetivo = random.choice(adjetivos)
    complemento = random.choice(complementos)

    genero_objeto = objeto["genero"]

    nome = f"{objeto["nome"]} {adjetivo[genero_objeto]} {complemento[genero_objeto]}"

    return nome


item1 = gerar_nome()
item2 = gerar_nome()
item3 = gerar_nome()

print("Item:", item1)
print("Item:", item2)
print("Item:", item3)
