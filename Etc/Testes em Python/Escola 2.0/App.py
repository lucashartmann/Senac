def main():
    menu()

def menu():
    opcao = 0 
    while opcao < 1 or opcao > 4:
        print('1 -- Cadastrar Aluno')
        print('2 -- Cadastrar Professor')
        print('3 -- Cadastrar Curso')
        print('4 -- Cadastrar Turma')
        opcao = int(input('Digite o número correspondente a opção: '))
        match opcao:
            case 1:
                cadastroAluno()
                return
            case 2:
                cadastroProfessor()
                return
            case 3:
                cadastroCurso()
                return
            case 4:
                ## cadastroTurma()
                return
            case _:
                print('Opção errada, tente novamente')

def cadastroAluno():
    nome = input('Digite o nome do aluno: ')
    aluno = (nome)
    print('Aluno cadastrado')

def cadastroProfessor():
    nome = input('Digite o nome do professor: ')
    professor = (nome)
    print('Professor cadastrado')

def cadastroCurso():
    nome = input('Digite o nome do curso: ')
    curso = (nome)
    print('Curso cadastrado')

if __name__ == '__main__':
    main()