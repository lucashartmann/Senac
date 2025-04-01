def main():
    alunos = {}
    professores = {}
    cursos = {}
    turmas = {}
    menu(alunos, professores, cursos)

def menu(alunos, professores, cursos):
    opcao = 0 
    while opcao < 1 or opcao > 9:
        print()
        print('##### MENU ######')
        print('1 -- Cadastrar Aluno')
        print('2 -- Cadastrar Professor')
        print('3 -- Cadastrar Curso')
        print('4 -- Cadastrar Turma')
        print('5 -- Ver alunos cadastrados')
        print('6 -- Ver professores cadastrados')
        print('7 -- Ver Cursos cadastrados')
        print('8 -- Ver Turmas cadastradas')
        print('9 -- Sair do menu')
        opcao = int(input('Digite o número correspondente a opção: '))
        print()
        match opcao:
            case 1:
                cadastroAluno(alunos)
            case 2:
                cadastroProfessor(professores)
            case 3:
                cadastroCurso(cursos)
            case 4:
                cadastroTurma() # Falta implementar
            case 5:
                verAlunos(alunos)
            case 6:
                verProfessores(professores)
            case 7:
                verCursos(cursos)
            case 8:
                verTurmas # Falta implementar
            case 9:
                quit()
            case _:
                print('Opção errada, tente novamente')
        menu(alunos, professores, cursos)

def cadastroAluno(alunos):
    soma = 0
    quant = int(input('Quantos alunos deseja cadastrar? '))
    while quant > soma:
        nome = input("Digite o nome do aluno: ")
        if nome != '':
            aluno = (nome)
            alunos[soma] = aluno
            soma = soma + 1
            print('Aluno cadastrado')
        else:
            print('Nome inválido')

def cadastroProfessor(professores):
    soma = 0
    quant = int(input('Quantos professores deseja cadastrar? '))
    while quant > soma:
        nome = input("Digite o nome do professor: ")
        if nome != '':
            professor = (nome)
            professores[soma] = professor
            soma = soma + 1
            print('Professor cadastrado')
        else:
            print('Nome inválido')

def cadastroCurso(cursos):
    soma = 0
    quant = int(input('Quantos cursos deseja cadastrar? '))
    while quant > soma:
        nome = input("Digite o nome do curso: ")
        if nome != '':
            curso = (nome)
            cursos[soma] = curso
            soma = soma + 1
            print('Cursos cadastrado')
        else:
            print('Nome inválido')

def verAlunos(alunos):
    print('Alunos Cadastrados: ')
    for x in alunos:
        print(alunos[x])    

def verProfessores(professores):
    print('Professores Cadastrados: ')
    for x in professores:
        print(professores[x])    

def verCursos(cursos):
    print('Cursos Cadastrados: ')
    for x in cursos:
        print(cursos[x])    

if __name__ == '__main__':
    main()