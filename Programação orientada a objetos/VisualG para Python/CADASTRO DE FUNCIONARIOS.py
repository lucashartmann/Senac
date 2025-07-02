funcionarios = []


def cadastro(nome):
    if nome not in funcionarios:
        funcionarios.append(nome)
        return True
    return False


quant = int(input("Quantos funcionarios deseja cadastrar? "))

if quant > 10:
    print("O número máximo de funcionários é 10.")
    quant = 10

for i in range(quant):
    nome = input("Informe o nome do funcionario: ")
    if cadastro(nome):
        cadastro(nome)
        print("Funcionario cadastrado com sucesso!")
    else:
        print("Funcionario já cadastrado!")

print("Funcionarios cadastrados:")
for i in range(len(funcionarios)):
    print("Nome: ", funcionarios[i])
