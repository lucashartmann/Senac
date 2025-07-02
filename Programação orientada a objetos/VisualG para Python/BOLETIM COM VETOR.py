notas = []

print("### BOLETIM ###")
nome = input("Informe o nome do aluno: ")
turma = input("Informe a turma do aluno: ")

for i in range(5):
    nota = float(input(f"Digite a nota {i} do aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\n## RESULTADOS ##")
print("Nome do aluno: ", nome)
print("Turma do aluno: ", turma)
print("Notas do Aluno: ")
for i in range(len(notas)):
    print(f"Nota {i}: {notas[i]}")
print("Média: ", media)
if media >= 7:
    situacao = "APROVADO"
elif media >= 5 and media < 7:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "REPROVADO"
print("Situação curricular: ", situacao)
