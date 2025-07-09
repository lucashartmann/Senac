import random

objeto = ["Rocha", "Espada", "Capa", "Foice", "Capacete", "Peitoral", "Calça", "Picareta", "Machado", "Cenoura", "Gema", "Moeda"]
adjetivo = ["Feroz", "Fulminante", "Vingativa", "Bela como a Lua", "Reluzente", "Fervescente"]
complemento = ["Forjada na lua", "do Minotauro", "dos confins do inferno", "Enferrujada", "Perfeita", "Usada pelo Rei de Minas"]

def gerar_nome():
    nome = f"{random.choice(objeto)} {random.choice(adjetivo)} {random.choice(complemento)}" 
    return nome

item1 = gerar_nome()
item2 = gerar_nome()
item3 = gerar_nome()

print("Item:", item1)
print("Item:", item2)
print("Item:", item3)