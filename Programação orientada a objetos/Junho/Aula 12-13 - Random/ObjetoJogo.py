import random

objetos = ["Rocha", "Espada", "Capa", "Foice", "Capacete", "Peitoral", "Calça", "Picareta", "Machado", "Cenoura", "Gema", "Moeda"]
adjetivos = ["Feroz", "Fulminante", "Vingativa", "Bela como a Lua", "Reluzente", "Fervescente"]
complementos = ["Forjada na lua", "do Minotauro", "dos confins do inferno", "Enferrujada", "Perfeita", "Usada pelo Rei de Minas"]

def gerar_numero(tamanho_lista):
    numero = int(random.randrange(tamanho_lista))
    return numero

def gerar_nome():
    nome = f"{objetos[gerar_numero(len(objetos))]} {adjetivos[gerar_numero(len(adjetivos))]} {complementos[gerar_numero(len(complementos))]}"    
    return nome

item1 = gerar_nome()
item2 = gerar_nome()
item3 = gerar_nome()

print("Item:", item1)
print("Item:", item2)
print("Item:", item3)