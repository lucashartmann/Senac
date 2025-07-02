condicao = 0
while condicao == 0:
    print("\n## Menu ##")
    print("1 -- Cadastrar/editar nome")
    print("2 -- Cadastrar/editar Idade")
    print("3 -- Cadastrar/editar turma")
    print("4 -- Exibir dados do aluno")
    print("5 -- Sair do menu")
    option = int(input("Digite a opção desejada: "))
    match option:
        case 1:
            nome = input("Digite o nome: ")
        case 2:
            idade = input("Digite a idade: ")
        case 3:
            turma = input("Digite a turma: ")
        case 4:
            print("Aluno: [Nome: ", nome, ", Idade: ",
                  idade, ", turma: ", turma, "]")
        case 5:
            print("Saindo")
            condicao = 1
        case _:
            print("Numero digitado é inválido, tente novamente")
