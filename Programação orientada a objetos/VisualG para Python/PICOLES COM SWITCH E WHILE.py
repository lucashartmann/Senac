
def menu():
    menu = f'''
    ### MENU ###
print("1 -- Picol� de Uva (R$1,00)")
      print("2 -- Picol� de Laranja (R$1,25)")
      print("3 -- Picol� de Milho (R$1,50)")
      print("4 -- Picol� de Coco queimado (R$1,80)")
      print("5 -- Picol� de Tamarindo (R$2,00)")
        print("6 -- Sair do menu")
        '''
    return menu


def main():
    condicao = "S"
    print("#### VENDA DE PICOLÉS ####")
    while condicao == "S":
        print(menu())
        opcao = int(
            input("Digite o número correspondente ao picolé que você deseja: "))
        match opcao:
            case 1:
                quantidade = input("Quantos picol�s deseja comprar?")
                quantidadeTotal = quantidadeTotal + quantidade
                valorTotal = valorTotal + (quantidade * 1.00)
                picoleValue = quantidade * 1.00
                print("###############")
                print("Quantidade de picol�s de Uva comprado(s): ", quantidade)
                print("Valor gasto com picol�s de Uva: R$", picoleValue)
            case 2:
                quantidade = input("Quantos picol�s deseja comprar?")
                quantidadeTotal = quantidadeTotal + quantidade
                valorTotal = valorTotal + (quantidade * 1.25)
                picoleValue = quantidade * 1.25
                print("###############")
                print("Quantidade de picol�s de Laranja comprado(s): ", quantidade)
                print("Valor gasto com picol�s de Laranja: R$", picoleValue)
            case 3:
                quantidade = input("Quantos picol�s deseja comprar?")
                quantidadeTotal = quantidadeTotal + quantidade
                valorTotal = valorTotal + (quantidade * 1.50)
                picoleValue = quantidade * 1.50
                print("###############")
                print("Quantidade de picol�s de Milho comprado(s): ", quantidade)
                print("Valor gasto com picol�s de Milho: R$", picoleValue)
            case 4:
                quantidade = input("Quantos picol�s deseja comprar?")
                quantidadeTotal = quantidadeTotal + quantidade
                valorTotal = valorTotal + (quantidade * 1.80)
                picoleValue = quantidade * 1.80
                print("###############")
                print("Quantidade de picol�s de Coco queimado comprado(s): ", quantidade)
                print("Valor gasto com picol�s de Coco queimado: R$", picoleValue)
            case 5:
                quantidade = input("Quantos picol�s deseja comprar?")
                quantidadeTotal = quantidadeTotal + quantidade
                valorTotal = valorTotal + (quantidade * 2.00)
                picoleValue = quantidade * 2.00
                print("###############")
                print("Quantidade de picol�s de Tamarindo comprado(s): ", quantidade)
                print("Valor gasto com picol�s de Tamarindo: R$", picoleValue)
            case _:
                print("numero digitado incorreto. Tente novamente")
        menu()

    opcao = 0
    print()
    print("###############")
    print("Quantidade de picol�s comprados no total: ", quantidadeTotal)
    print("Valor a ser pago no total: R$", valorTotal)
    print()
    condicao = input("Deseja seguir comprando? (S/N) ")
    condicao = condicao.upper()
    opcao = 1
    while (opcao < 0) or (opcao > 6):
        print("#### CAIXA ####")
        print("1 -- A vista em dinheiro ou PIX (10% OFF)")
        print("2 -- No cartao de d�bito (5% OFF)")
        print("3 -- No cartao de credito em 1x")
        print("4 -- No cartao de credito em 2x (+5% acr�scimo)")
        print("5 -- No cartao de credito em 3x (+10% acr�scimo)")
        print("6 -- No cartao de credito em 4x (+15% acr�scimo)")
        opcao = input("Digite o n�mero correspondente � forma de pagamento: ")
        match opcao:
            case 1:
                desconto = 10
                valorFinal = valorTotal - (valorTotal * 0.10)
            case 2:
                desconto = 10
                valorFinal = valorTotal - (valorTotal * 0.05)
            case 4:
                parcelas = 2
                acrescimo = 5
                valorFinal = valorTotal + (valorTotal * 0.05)
            case 5:
                parcelas = 3
                acrescimo = 10
                valorFinal = valorTotal + (valorTotal * 0.10)
            case 6:
                parcelas = 4
                acrescimo = 15
                valorFinal = valorTotal + (valorTotal * 0.15)
            case _:
                print("o n�mero digitado � inv�lido! Tente novamente")
        print(recibo(valorTotal, quantidadeTotal, desconto, acrescimo, parcelas))


def recibo(valorTotal, quantidadeTotal, desconto, acrescimo, parcelas):
    recibo = f'''
## RECIBO ##
Quantidade de picolés comprados: {quantidadeTotal}
Valor total: {valorTotal}
Desconto: {desconto}
Acréscimo: {acrescimo}
Número de parcelas: {parcelas}
Valor final pago: {valorTotal}
        '''
    return recibo


if __name__ == "__main__":
    main()
