print("## DADOS ##")
salario = float(input("Informe seu salário: "))
while True:
    categoria = input(
        "Digite a categoria de aumento salarial (usando A, B ou C): ")
    categoria = categoria.upper()
    if categoria in ["A", "B", "C"]:
        break
    else:
        print("Categoria inválida! Digite novamente.")
categorias = ["A", "B", "C"]
if categoria in categorias:
    match categoria:
        case "A":
            aumento = salario * 0.50
        case "B":
            aumento = salario * 0.30
        case "C":
            aumento = salario * 0.10
    salarioFinal = salario + aumento
    dados = f'''
\n## RESULTADO DA CONSULTA ##
Salário atual: {salario}
Categoria de aumento: {categoria}
Salário final: {salarioFinal}
        '''
    print(dados)
print("CATEGORIA DE AUMENTO SALARIAL INVÁLIDO!")
