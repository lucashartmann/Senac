import csv

itens = [
	{'nome': 'Espada Longa', 'tipo': 'arma', 'dano': '1d8'},
	{'nome': 'Poção de Cura', 'tipo': 'consumível', 'dano': '-'},
	{'nome': 'Escudo de Ferro', 'tipo': 'armadura', 'dano': '-'}
]

with open('itens.csv', 'w', newline='', encoding='utf-8') as arquivo:
	campos = ['nome', 'tipo', 'dano']
	escritor = csv.DictWriter(arquivo, fieldnames=campos)
	escritor.writeheader()
	escritor.writerows(itens)