vendas = []
vendas_mes = []


def menu():
    nome = input("Informe o nome do vendedor: ")
    opcao = 0
    while True:
        vendas_mes = []
        menu = f'''
### MENU ###
1 - Cadastrar venda de janeiro:
2 - Cadastrar venda de fevereiro:
3 - Cadastrar venda de março:
4 - Cadastrar venda de abril:
5 - Cadastrar venda de maio:
6 - Cadastrar venda de junho:
7 - Sair do menu
        '''
        print(menu)
        opcao = int(input("Informe a opção desejada: "))
        match opcao:
            case 1:
                print("Você escolheu cadastrar venda de janeiro.")
                quant = int(input("Quantas vendas deseja cadastrar? "))
                for i in range(quant):
                    venda = float(input("Informe o valor da venda: "))
                    vendas_mes.append(venda)
                vendas.append(vendas_mes)
            case 2:
                print("Você escolheu cadastrar venda de fevereiro.")
                quant = int(input("Quantas vendas deseja cadastrar? "))
                for i in range(quant):
                    venda = float(input("Informe o valor da venda: "))
                    vendas_mes.append(venda)
                vendas.append(vendas_mes)
            case 3:
                print("Você escolheu cadastrar venda de março.")
                quant = int(input("Quantas vendas deseja cadastrar? "))
                for i in range(quant):
                    venda = float(input("Informe o valor da venda: "))
                    vendas_mes.append(venda)
                vendas.append(vendas_mes)
            case 4:
                print("Você escolheu cadastrar venda de abril.")
                quant = int(input("Quantas vendas deseja cadastrar? "))
                for i in range(quant):
                    venda = float(input("Informe o valor da venda: "))
                    vendas_mes.append(venda)
                vendas.append(vendas_mes)
            case 5:
                print("Você escolheu cadastrar venda de maio.")
                quant = int(input("Quantas vendas deseja cadastrar? "))
                for i in range(quant):
                    venda = float(input("Informe o valor da venda: "))
                    vendas_mes.append(venda)
                vendas.append(vendas_mes)
            case 6:
                print("Você escolheu cadastrar venda de junho.")
                quant = int(input("Quantas vendas deseja cadastrar? "))
                for i in range(quant):
                    venda = float(input("Informe o valor da venda: "))
                    vendas_mes.append(venda)
                vendas.append(vendas_mes)
            case 7:
                print("Você escolheu sair do menu.")
                break
            case _:
                print("Opção inválida. Tente novamente.")
    relatorio(nome)


def relatorio(nome):
    print(f"Relatório de vendas do vendedor {nome}:")
    for i in range(len(vendas)):
        print(f"Vendas do mês {i+1}: {vendas[i]}")
        print(f"Total de vendas do mês {i+1}: {sum(vendas[i])}")
        print(f"Média de vendas do mês {i+1}: {sum(vendas[i])/len(vendas[i])}")


menu()
