import csv

with open('personagens.csv', 'r', encoding='utf-8') as arquivo:
	leitor = csv.reader(arquivo)
	for linha in leitor:
		print(linha)