print("## LOJA DE VEICULOS MARCELÃO ##")
nome = input("Informe o nome do veículo: ")
preco_fabrica = float(input("Informe o preço de fábrica do veículo: "))
imposto = 45 / 100
percent_vendedor = 28 / 100
percent_vendedor = preco_fabrica * percent_vendedor
imposto = preco_fabrica * imposto
preco_final = preco_fabrica + percent_vendedor + imposto
dados = f'''
Nome do veículo: {nome}
Preço de fábrica: {preco_fabrica}
Percentual do vendedor: {percent_vendedor}
Imposto: {imposto}
Preço final: {preco_final}
'''
print(dados)
