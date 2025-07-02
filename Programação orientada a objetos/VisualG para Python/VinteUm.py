print("## CADASTRO LOJA MARCELINHO ##")
nome = input("Informe o nome do cliente: ")
sobrenome = input("Informe o sobrenome do cliente: ")
cidade = input("Informe a cidade do cliente: ")
sexo = input("Informe o sexo do cliente: ")
endereco = input("Informe o endereço do cliente: ")
idade = int(input("Informe a idade do cliente: "))
rg = input("Informe o rg do cliente: ")
cpf = input("Informe o cpf do cliente: ")
dados = f'''
\n## DADOS DO CADASTRADOS ##
Nome: {nome}
Sobrenome: {sobrenome}
cidade: {cidade}
Sexo: {sexo}
Endereço: {endereco}
Idade: {idade}
RG: {rg}
CPF: {cpf}
'''
print(dados)
