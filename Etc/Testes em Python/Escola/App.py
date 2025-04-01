def main():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    media = (nota1 + nota2 + nota3) / 3
    soma = (nota1 + nota2 + nota3)
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Soma: {soma}")
    print(f"Media: {media:.2f}")

if __name__ == '__main__':
    main()