notas = []


def media(notas):
    media = sum(notas) / len(notas)
    return media


def situacao(media):
    if media >= 7:
        return "APROVADO"
    elif media >= 5 and media < 7:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"


print("### BOLETIM ###")
for i in range(3):
    nota = input(f"Digite a nota {i} do aluno: ")
    notas.append(nota)

print("\n## RESULTADOS ##")
print("Notas: ")
for nota in notas:
    print(f"Nota {i}: {nota[i]}")
media = media(notas)
print("Média: ", media)
situacao = situacao(media)
print("Situação curricular: ", situacao)
