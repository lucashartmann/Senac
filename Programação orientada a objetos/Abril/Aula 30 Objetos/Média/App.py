from Aluno import Aluno

nome = input("Digite o nome do aluno: ")
turma = input("Digite a turma do aluno: ")

aluno = Aluno(turma, nome)

for n in range(3):
    nota = float(input(f"Digite a nota {n+1}: "))
    aluno.adicionar_nota(nota)


def imprimir(aluno):
    dados = f'''
    Nome: {aluno.nome}
    Turma: {aluno.turma}
    Notas: {aluno.notas}
    Média: {aluno.media}
    Situação: {aluno.situacao}
    '''
    print(dados)


imprimir(aluno)
