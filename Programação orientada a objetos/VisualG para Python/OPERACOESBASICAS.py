import math

print("## OPERAÇÕES ##")
valorUm = int(input("Informe um valor: "))
valorDois = int(input("Informe outro valor: "))

resultado = valorUm + valorDois
print("\nSoma: ", resultado)

resultado = valorUm - valorDois
print("Subtração: ", resultado)

resultado = valorUm / valorDois
print("Divisão: ", resultado)

resultado = valorUm * valorDois
print("Multiplicação: ", resultado)

resultado = valorUm ^ valorDois
print("Potência: ", resultado)


print("Raiz do primeiro valor: ", math.sqrt(valorUm))
print("Raiz do segundo valor: ", math.sqrt(valorDois))
