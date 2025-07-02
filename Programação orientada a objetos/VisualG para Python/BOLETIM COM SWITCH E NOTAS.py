notas = []

print("## BOLETIM ##")

for i in range(3):
    nota = input(f"Digite a nota {i} do aluno: ")
    notas.append(nota)

media = sum(notas) / len(notas)

print("\n## RESULTADOS ##")
print("Notas: ")
for i in range(len(notas)):
    print(f"Nota {i}: {notas[i]}")
print("Média: ", media)

match media:
    case media if media >= 7:
        situacao = "APROVADO"
    case media if media >= 5 and media < 7:
        situacao = "RECUPERAÇÃO"
    case _:
        situacao = "REPROVADO"
print("Situação curricular: ", situacao)
