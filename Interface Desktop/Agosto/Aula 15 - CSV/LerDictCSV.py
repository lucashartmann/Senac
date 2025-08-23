import csv

with open('itens.csv', 'r', encoding='utf-8') as arquivo:
	leitor = csv.DictReader(arquivo)
	for linha in leitor:
		print(linha['nome'], linha['tipo'], linha['dano'])
		

with open('itens.csv', 'r', encoding='utf-8') as arquivo:
	leitor = csv.DictReader(arquivo)
	for linha in leitor:
		print(linha)
		