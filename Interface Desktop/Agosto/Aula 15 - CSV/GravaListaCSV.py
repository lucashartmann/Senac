import csv

personagens = [
	['nome', 'classe', 'nivel', 'hp'],
	['Arthos', 'Guerreiro', 5, 42],
	['Lyra', 'Maga', 4, 28],
	['Dorn', 'Clérigo', 3, 35]
]

with open('personagens.csv', 'w', newline='', encoding='utf-8') as arquivo:
	escritor = csv.writer(arquivo)
	escritor.writerows(personagens)