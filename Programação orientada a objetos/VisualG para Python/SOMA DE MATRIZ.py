matrix = [[0, 0], [0, 0]]
soma = 0

print("## ENTRADA DE DADOS ##")

for i in range(2):
    for j in range(2):
        matrix[i][j] = int(input(f"Informe o valor da posição [{i}][{j}]: "))

for j in range(2):
    for i in range(2):
        soma += matrix[i][j]

print("## DADOS ##")

for i in range(2):
    for j in range(2):
        print(f"Valor da posição [{i}][{j}]: {matrix[i][j]}")
print(f"Soma dos valores da matriz: {soma}")
