print("## SISTEMA DE CONVERSÃO REAIS -> DOLARES ##")
valor_reais = float(input("Informe o valor em reais: "))
cotacao_dolar = float(input("Informe a cotação do dólar: "))
dolar = valor_reais / cotacao_dolar
print("Sua quantia em dólar é: ", dolar)

print("\n## SISTEMA DE CONVERSÃO DOLARES -> REAIS ##")
valor_dolares = float(input("Informe o valor em dólares: "))
cotacao_dolar = float(input("Informe a cotação do dólar: "))
reais = valor_dolares * cotacao_dolar
print("Sua quantia em reais é: ", reais)
