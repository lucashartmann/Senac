notas = []
print("### CALCULADORA DE MÉDIA ###")
nome = input("Informe seu nome: ")
turma = input("Informe sua turma: ")

for i in range(5):
    while True:
        nota = float(input(f"Informe sua nota {i}: "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Nota inválida! Digite novamente.")
soma = sum(notas)
media = soma / len(notas)

dados = f'''
#########
Nome: {nome}
Turma: {turma}
Notas: {notas}
Média: {media}
'''
print(dados)
