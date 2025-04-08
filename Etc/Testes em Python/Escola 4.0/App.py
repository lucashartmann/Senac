def main():
    alunos = []
    professores = []
    cursos = []
    turmas = []
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
                # return
                quit()
            case _:
                print('Opção errada, tente novamente')
        menu(alunos, professores, cursos)

def cadastroTurma(turmas, alunos, professores, cursos):
    nomeTurma = input("Digite o nome da turma: ")
    turma = (nomeTurma)
    nomeAluno = input("Digite o nome do aluno: ")
    aluno = (nomeAluno)
    nomeProfessor = input("Digite o nome do professor: ") 
    professor = (nomeProfessor)
    nomeCurso = input("Digite o nome do curso: ")
    curso = (nomeCurso)
    boolProfessor, boolAluno, boolCurso = False
    for x in alunos:
        if (alunos[x] == aluno):
            return boolAluno==True
    for x in professores:
        if(professores[x] == professor):
            return boolProfessor==True
    for x in cursos:
        if(cursos[x] == curso):
            return boolCurso==True
    # if boolProfessor == True and boolCurso != True and boolAluno != True:]
    turma = (nomeTurma, professor, aluno, curso)

def cadastroAluno(alunos):
    soma = 0
    quant = int(input('Quantos alunos deseja cadastrar? '))
    while quant > soma:
        nome = input("Digite o nome do aluno: ")
        if nome != '':
            aluno = (nome)
            if (len(alunos) > 0):
                for x in alunos:
                    if(x == aluno):
                        print("Erro. Aluno já está cadastrado")
                        break
                    else:
                        alunos.append(aluno)
                        soma = soma + 1
                        print('Aluno cadastrado')
            else:
                alunos.append(aluno)
                soma = soma + 1
                print('Aluno cadastrado')
        else:
            print('Erro. Nome inválido')

def cadastroProfessor(professores):
    soma = 0
    quant = int(input('Quantos professores deseja cadastrar? '))
    while quant > soma:
        nome = input("Digite o nome do professor: ")
        if nome != '':
            professor = (nome)
            if (len(professores) > 0):
                for x in professores:
                    if(x == nome):
                        print("Erro. Professor já está cadastrado")
                        break
                    else:
                        professores.append(professor)
                        soma = soma + 1
                        print('Professor cadastrado')
            else:
                professores.append(professor)
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
            if (len(cursos) > 0):
                for x in cursos:
                    if(x == nome):
                        print("Erro. Cursos já está cadastrado")
                        break
                    else:
                        cursos.append(curso)
                        soma = soma + 1
                        print('Cursos cadastrado')
            else: 
                cursos.append(curso)
                soma = soma + 1
                print('Cursos cadastrado')
        else:
            print('Nome inválido')

def verAlunos(alunos):
    if (len(alunos) > 0):
        print('Alunos Cadastrados: ')
        for x in alunos:
            print(x)
    else:
        print("Erro. Não há alunos cadastrados")    

def verProfessores(professores):
    if (len(professores) > 0):
        print('Professores Cadastrados: ')
        for x in professores:
            print(x)    
    else:
        print("Erro. Não há professores cadastrados") 

def verCursos(cursos):
    if (len(cursos) > 0):
        print('Cursos Cadastrados: ')
        for x in cursos:
            print(x)    
    else:
        print("Erro. Não há cursos cadastrados") 

if __name__ == '__main__':
    main()