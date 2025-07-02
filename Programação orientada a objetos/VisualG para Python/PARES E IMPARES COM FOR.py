number = int(input("Digite um número: "))

print("Números primos de 1 até ", number, ":")
for i in range(number):
    divisao = i % 2
    if divisao == 0:
        print(i)


print("\nNúmeros ímpares de 1 até ", number, ":")
for i in range(number):
    divisao = i % 2
    if (divisao != 0):
        print(i)
