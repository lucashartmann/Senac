print("#### BOLETIM ####")
quant = int(input("Quantas registros deseja realizar? "))
for i in range(quant):
    nome = input("Informe o nome do aluno: ")
    turma = input("Informe a turma do aluno: ")
    notas = []
    for j in range(3):
        while True:
            nota = float(input(f"Digite a nota {j} do aluno: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
    media = sum(notas) / len(notas)
    print("\n## RESULTADOS ##")
    print("Nome do aluno: ", nome)
    print("Turma do aluno: ", turma)
    print("Notas do Aluno: ")
    for j in range(len(notas)):
        print(f"Nota {j}: {notas[j]}")
    print("Média: ", media)
    if media >= 7:
        situacao = "APROVADO"
    elif media >= 5 and media < 7:
        situacao = "RECUPERAÇÃO"
    else:
        situacao = "REPROVADO"
    print("Situação curricular: ", situacao)
