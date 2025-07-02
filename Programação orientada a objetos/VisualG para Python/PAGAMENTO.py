nome = input("Digite seu nome: ")
valorInicial = input("Digite o valor da venda: ")

print("## MENU PAGAMENTO ##")
print("Digite o número da operação desejada: ")
print("1 -- Venda a vista (10% de desconto)")
print("2 -- Venda a prazo de 30 dias (5% de desconto)")
print("3 -- Venda a prazo de 60 dias")
print("4 -- Venda a prazo de 90 dias (5% de acréscimo)")
print("5 -- Venda com cartão de débito (8% de desconto)")
print("6 -- Venda com cartão de crédito (7% de desconto)")
opcao = input("Digite o número correspondente a forma de pagamento: ")

match opcao:
    case 1:
        desconto = 10
    case 2:
        desconto = 5
    case 4:
        acrescimo = 5
    case 5:
        desconto = 8
    case 6:
        desconto = 7
    case _:
        print("Número digitado inv�lido. Tente novamente")

valorTotal = valorInicial - (valorInicial * (desconto/100))
if opcao == 3:
    valorTotal = valorInicial
print("Nome do vendedor: ", nome)
print("Valor da venda: ", valorInicial)
if (desconto > 0):
    print("Desconto: ", desconto, "%")
else:
    if (acrescimo > 0):
        print("Acréscimo: ", acrescimo, "%")
print("Valor total da venda: ", valorTotal)
