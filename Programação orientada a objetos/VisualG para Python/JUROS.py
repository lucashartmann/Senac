print("## SISTEMA DE COBRAN�A DE JUROS")
prestacao = float(input("Informe sua prestaçãoo: "))
dias = int(input("Informe os dias de atraso: "))
juros = 2 / 100
juros = (prestacao * juros) * dias
print("\n## RESULTADO DA CONSULTA")
print("Valor da prestação: R$", prestacao)
print("Dias em atraso: ", dias)
print("Valor do juros: R$", juros)
prestacao = prestacao + juros
print("Valor final para pagar: R$", prestacao)
