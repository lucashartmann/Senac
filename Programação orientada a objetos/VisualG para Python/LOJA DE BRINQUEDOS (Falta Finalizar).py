number = 0
parcelas = 0
quantAtual = 0
quantTotal = 0
i = 0
condicaoDois = 0
j = 0
valorProduto = 0.0
valorFinal = 0.0
valorParcelado = 0.0
valorTotal = 0.0
desconto = 0.0
acrescimo = 0.0
menu = ""
menuPagamento = ""
condicao = ""
nome = ""
pagamento = ""
valorAtual = 0.0
valorFinalTotal = 0.0
meiosPagamento = []
quantProduto = 0
l = 0
m = 0
quantPay = 0
produtos = {}
totalProdutos = {}


def cadastroProduto(nome, valorProduto):
    produtos[nome] = valorProduto
    totalProdutos[nome] = valorProduto
    return 1


def cadastroPagamento(pagamento, i):
    meiosPagamento[i] = pagamento
    return 1


def menu(valorAtual, quantAtual):
    number = 0
    while number < 1 or number > 7:
        print("### MENU ###")
        print("1 -- Carrinho a controle remoto super máquina - R$ 500,00")
        print("2 -- Boneca Barbie - R$ 450,00")
        print("3 -- Boneco cobra comandos em ação - R$ 300,00")
        print("4 -- Boneco fofão - R$ 480,00")
        print("5 -- Vídeo game Atari - R$ 820,00")
        print("6 -- Jogo Super Mário - R$ 100,00")
        print("7 -- Bicicleta caloi cross extra - R$ 5.000,00")
        number = int(
            input("Digite o número correspondente á oção desejada: "))
        match(number):
            case 1:
                valorProduto = 500.00
                nome = "Carrinho a controle remoto super máquina"
                quantProduto = int(
                    input("Informe quantos você deseja comprar: "))
                for l in range(quantProduto):
                    valorAtual = valorAtual + valorProduto
                    condicaoDois = cadastroProduto(nome, valorProduto)
                    if condicaoDois == 1:
                        print(nome, " comprado!")
                    else:
                        print("Não foi possivel finalizar a compra.")
                quantAtual = quantAtual + quantProduto
            case 2:
                valorProduto = 450.00
                nome = "Boneca Barbie"
                quantProduto = int(
                    input("Informe quantos você deseja comprar: "))
                for l in range(quantProduto):
                    valorAtual = valorAtual + valorProduto
                    condicaoDois = cadastroProduto(nome, valorProduto)
                    if condicaoDois == 1:
                        print(nome, " comprado!")
                    else:
                        print("Não foi possivel finalizar a compra.")
                quantAtual = quantAtual + quantProduto
            case 3:
                valorProduto = 300.00
                nome = "Boneco cobra comandos em ação"
                quantProduto = int(
                    input("Informe quantos você deseja comprar: "))
                for l in range(quantProduto):
                    valorAtual = valorAtual + valorProduto
                    condicaoDois = cadastroProduto(nome, valorProduto)
                    if condicaoDois == 1:
                        print(nome, " comprado!")
                    else:
                        print("Não foi possivel finalizar a compra.")
                quantAtual = quantAtual + quantProduto
            case 4:
                valorProduto = 480.00
                nome = "Boneco fofão"
                quantProduto = int(
                    input("Informe quantos você deseja comprar: "))
                for l in range(quantProduto):
                    valorAtual = valorAtual + valorProduto
                    condicaoDois = cadastroProduto(nome, valorProduto)
                    if condicaoDois == 1:
                        print(nome, " comprado!")
                    else:
                        print("Não foi possivel finalizar a compra.")
                quantAtual = quantAtual + quantProduto
            case 5:
                valorProduto = 820.00
                nome = "Vídeo game Atari"
                quantProduto = int(
                    input("Informe quantos você deseja comprar: "))
                for l in range(quantProduto):
                    valorAtual = valorAtual + valorProduto
                    condicaoDois = cadastroProduto(nome, valorProduto)
                    if condicaoDois == 1:
                        print(nome, " comprado!")
                    else:
                        print("Não foi possivel finalizar a compra.")
                quantAtual = quantAtual + quantProduto
            case 6:
                valorProduto = 100.00
                nome = "Jogo super Mário"
                quantProduto = int(
                    input("Informe quantos você deseja comprar: "))
                for l in range(quantProduto):
                    valorAtual = valorAtual + valorProduto
                    condicaoDois = cadastroProduto(nome, valorProduto)
                    if condicaoDois == 1:
                        print(nome, " comprado!")
                    else:
                        print("Não foi possivel finalizar a compra.")
                quantAtual = quantAtual + quantProduto
            case 7:
                valorProduto = 5000.00
                nome = "Bicicleta caloi cross extra"
                quantProduto = int(
                    input("Informe quantos você deseja comprar: "))
                for l in range(quantProduto):
                    valorAtual = valorAtual + valorProduto
                    condicaoDois = cadastroProduto(nome, valorProduto)
                    if condicaoDois == 1:
                        print(nome, " comprado!")
                    else:
                        print("Não foi possivel finalizar a compra.")
                quantAtual = quantAtual + quantProduto
            case _:
                print("Número inválido. Tente novamente")
    print(dados())


def menuPagamento():
    pagamento = "cartão de crédito em"
    number = 0
    while number < 1 or number > 7:
        print("### MENU DE PAGAMENTO ###")
        print("1 - A vista em dinheiro ou PIX, 5% de desconto")
        print("2 - No cartão de débito")
        print("3 - No cartão de crédito em 1x, Acréscimo de 5%")
        print("4 - No cartão de crédito em 2x, Acréscimo de 5%")
        print("5 - No cartão de crédito em 3x, Acréscimo de 8%")
        print("6 - No cartão de crédito em 4x, Acréscimo de 8%")
        print("7 - No cartão de crédito em 5x, Acréscimo de 10%")
        number = int(input("Digite o número correspondente á opção: "))
        match number:
            case 1:
                pagamento = "a vista"
                desconto = 5
                valorFinal = valorAtual - (valorAtual * (desconto / 100))
                valorFinalTotal = valorFinalTotal + valorFinal
                m = m + 1
                condicaoDois = cadastroPagamento(pagamento, m)
                quantPay = quantPay + 1
            case 2:
                pagamento = "cartão de débito"
                valorFinal = valorAtual
                valorFinalTotal = valorFinalTotal + valorFinal
                m = m + 1
                condicaoDois = cadastroPagamento(pagamento, m)
                quantPay = quantPay + 1
            case 3:
                pagamento = pagamento + " 1x"
                acrescimo = 5
                valorFinal = valorAtual + (valorAtual * (acrescimo / 100))
                parcelas = 1
                valorParcelado = valorFinal / parcelas
                valorFinalTotal = valorFinalTotal + valorFinal
                m = m + 1
                condicaoDois = cadastroPagamento(pagamento, m)
                quantPay = quantPay + 1
            case 4:
                pagamento = pagamento + " 2x"
                acrescimo = 5
                valorFinal = valorAtual + (valorAtual * (acrescimo / 100))
                parcelas = 2
                valorParcelado = valorFinal / parcelas
                valorFinalTotal = valorFinalTotal + valorFinal
                m = m + 1
                condicaoDois = cadastroPagamento(pagamento, m)
                quantPay = quantPay + 1
            case 5:
                pagamento = pagamento + " 3x"
                acrescimo = 8
                valorFinal = valorAtual + (valorAtual * (acrescimo / 100))
                parcelas = 3
                valorParcelado = valorFinal / parcelas
                valorFinalTotal = valorFinalTotal + valorFinal
                m = m + 1
                condicaoDois = cadastroPagamento(pagamento, m)
                quantPay = quantPay + 1
            case 6:
                pagamento = pagamento + " 4x"
                acrescimo = 8
                valorFinal = valorAtual + (valorAtual * (acrescimo / 100))
                parcelas = 4
                valorParcelado = valorFinal / parcelas
                valorFinalTotal = valorFinalTotal + valorFinal
                m = m + 1
                condicaoDois = cadastroPagamento(pagamento, m)
                quantPay = quantPay + 1
            case 7:
                pagamento = pagamento + " 5x"
                acrescimo = 10
                valorFinal = valorAtual + (valorAtual * (acrescimo / 100))
                parcelas = 5
                valorParcelado = valorFinal / parcelas
                valorFinalTotal = valorFinalTotal + valorFinal
                m = m + 1
                condicaoDois = cadastroPagamento(pagamento, m)
                quantPay = quantPay + 1
            case _:
                print("Número inválido. Tente novamente")
    print(dadosPagamento())
    quantAtual = 0
    valorAtual = 0
    i = 0
    desconto = 0
    acrescimo = 0
    parcelas = 0


def dados():
    print("Quantidade de produtos comprados na compra atual: ", quantAtual)
    print("-----------")
    print("Produtos comprados: ")
    for nome, valor in produtos.items():
        print("Nome: ", nome)
        print("Preço: R$", valor)
    print("-----------")
    print("Valor da compra atual: R$", valorAtual)


def dadosPagamento():
    print("#### DADOS DE PAGAMENTO ####")
    print(dados)
    print("Método de pagamento: ", pagamento)
    if (desconto > 0):
        print("Desconto: %", desconto)
    if (acrescimo > 0):
        print("Acréscimo: %", acrescimo)
        print("Valor Final: R$", valorFinal)
    if (parcelas > 0):
        print("Número de parcelas: ", parcelas)
        print("Valor das parcelas: R$", valorParcelado)


condicao = "s"
quantTotal = 0
valorTotal = 0
print("#### LOJA DE BRINQUEDOS ####")
while condicao == "s" or condicao == "S":
    while condicao == "s" or condicao == "S":
        print(menu(valorAtual, quantAtual))
        condicao = input("Deseja comprar mais? (S/N)")
        number = 0
    valorTotal = valorTotal + valorAtual
    quantTotal = quantTotal + quantAtual
    print(menuPagamento())
    condicao = input("Deseja comprar mais? (S/N)")
    number = 0
print("Produtos comprados no dia: ")
for nome, total in totalProdutos.items():
    print("Nome: ", nome)
    print("Preço: R$", total)
print("Quantidade total de produtos comprados no dia: ", quantTotal)
print("Valor total das compras no dia: R$", valorTotal)
print("Valor total final das compras no dia: R$", valorFinalTotal)
print("Meios de pagamento usados no dia: ")
for i in range(quantPay):
    print(meiosPagamento[i])
print("Obrigado por comprar conosco!")
