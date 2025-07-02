print("## SISTEMA DE CADASTRO ##")
nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")
idade = int(input("Informe sua idade: "))
dados = f'''
## DADOS CADASTRADOS ##
Nome: {nome}
Sobrenome: {sobrenome}
Idade: {idade}
'''
print(dados)
