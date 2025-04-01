def main():
    alunos = {}
    soma = 0
    quant = int(input('Quantos alunos deseja cadastrar? '))
    while quant > soma:
        nome = input("Digite o nome do aluno: ")
        alunos[soma] = nome
        soma = soma + 1
    for x in alunos:
        print('Alunos Cadastrados: ')
        print(alunos[x])

if __name__ == '__main__':
    main()