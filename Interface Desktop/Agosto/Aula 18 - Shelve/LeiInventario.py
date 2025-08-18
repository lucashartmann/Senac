import shelve
from Inventario import Item

with shelve.open('inventario.db') as db:
    item1 = db["espada"]
    print(item1.nome, item1.tipo, item1.dano)