nomeBebidas = []

print("### SISTEMA DO BAR DO ITO ###")
quantBebidas = int(input("Quantas bebidas foram pedidas? (Máximo 10) "))

if quantBebidas > 10:
    quantBebidas = 10

for i in range(quantBebidas):
    nome = input("Informe o nome da bebida pedida: ")
    nomeBebidas.append(nome)

maxContagem = 0
maisPedida = ""
empate = "False"

for i in range(quantBebidas):
    contagemAtual = 0
    for j in range(quantBebidas):
        if nomeBebidas[i] == nomeBebidas[j]:
            contagemAtual = contagemAtual + 1
    if contagemAtual > maxContagem:
        maxContagem = contagemAtual
        maisPedida = nomeBebidas[i]
        empate = "False"
    else:
        if contagemAtual == maxContagem and nomeBebidas[i] != maisPedida:
            empate = "True"


if maxContagem > 1 and empate == "False":
    print("A bebida mais pedida foi: ", maisPedida,
          " com ", maxContagem, " pedidos.")
else:
    print("Não teve uma bebida mais pedida.")
