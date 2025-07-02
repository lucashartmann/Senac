print("## SISTEMA DE COBRAN�A DE JUROS")
prestacao = float(input("Informe sua prestação: "))
dias = int(input("Informe os dias de atraso: "))
juros = float(input("Informe a taxa de juros: "))

print("\n## RESULTADO DA CONSULTA")
print("Valor da prestação: R$", prestacao)
print("Dias em atraso: ", dias)
print("Juros: %", juros)
juros = (juros * dias) / 30
print("Valor do juros: R$", juros)
prestacao = prestacao + juros
print("Valor final para pagar: R$", prestacao)
