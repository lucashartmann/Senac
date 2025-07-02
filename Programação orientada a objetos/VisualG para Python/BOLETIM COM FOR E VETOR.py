notas = []

print("### BOLETIM ###")
nome = input("Informe o nome do aluno: ")
turma = input("Informe a turma do aluno: ")

for i in range(5):
    nota = float(input(f"Digite a nota {i} do aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

dados = f'''
\n## RESULTADOS ##
Nome do aluno: {nome}
Turma do aluno: {turma}
Notas do Aluno: {notas}
Media: {media}
'''
print(dados)
