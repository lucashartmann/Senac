notas = []
nome = input("Informe o nome do aluno: ")
turma = input("Informe a turma do aluno: ")

for i in range(5):
    while True:
        nota = float(input(f"Digite a nota {i} do aluno: "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break

media = sum(notas) / len(notas)

if media >= 7:
    situcao = "APROVADO"
elif media >= 5 and media < 7:
    situcao = "RECUPERAÇÃO"
else:
    situcao = "REPROVADO"

dados = f'''
Nome do aluno: {nome}
Turma do aluno: {turma}
Notas do Aluno: {notas}
Media: {media}
Situação curricular: {situcao}
    '''
print(dados)
