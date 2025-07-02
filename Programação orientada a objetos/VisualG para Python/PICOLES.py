
def menu():
    menu = '''
## MENU ##
Digite o número correspondente ao picolé que você deseja:
1 -- Picolé de Uva (R$1,00)
2 -- Picolé de Laranja (R$1,25)
3 -- Picolé de Milho (R$1,50)
4 -- Picolé de Coco queimado (R$1,80)
5 -- Picolé de Tamarindo (R$2,00)
6 -- Sair do menu
        '''
    return menu

def main():
    opcao = 0
    quant = 0
    value = 0.0
    print("## VENDA DE PICOLÉS ##")
    while True:
        print(menu())
        opcao = int(input("Informe a opção desejada: "))
        match opcao:
            case 1:
                value = value + 1.00
                print("Picolé de Uva comprado!")
            case 2:
                value = value + 1.25
                print("Picolé de Laranja comprado!")
            case 3:
                value = value + 1.50
                print("Picolé de Milho comprado!")
            case 4:
                value = value + 1.80
                print("Picolé de Coco queimado comprado!")
            case 5:
                value = value + 2.00
                print("Picolé de Tamarindo comprado!")
            case 6:
                print("Você escolheu sair!")
                break
            case _:
                print("O número digitado é inválido!")
        quant = quant + 1
        print(dados(quant, value))


def dados(quant, value):
    dados = f'''
## RESULTADO DA COMPRA ##
Quantidade de picolés comprados: {quant}
Valor a ser pago: {value}
        '''
    return dados


if __name__ == "__main__":
    main()
