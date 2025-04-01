class App:

    def executar(self):
        sorveteMorango = ('Sorvete de Morango', 2.99)
        bolacha = ('Bolacha de chocolate', 1.00)
        banana = ('Banana', 3.50)
        self.menu()

    def menu(self):
        opcao = 0 
        while opcao < 1 or opcao > 3:
            print('1 -- Sorvete de Morango 2.99')
            print('2 -- Bolacha de chocolate 1.00')
            print('3 -- Banana 3.50')
            opcao = int(input('Digite o número correspondente a opção: '))
            match opcao:
                case 1:
                    print('Sorvete comprado!')
                    return
                case 2:
                    print('Bolacha comprada!')
                    return
                case 3:
                    print('Banana comprada')
                    return
                case _:
                    print('Opção errada, tente novamente')
                    
