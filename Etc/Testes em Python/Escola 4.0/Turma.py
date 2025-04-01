from Professor import Professor
from Aluno import Aluno
from Curso import Curso

class Turma:
    def __init__(self, name=None, Professor=Professor, Aluno=Aluno, Curso=Curso):
        self.name = name
        self.Professor = Professor
        self.Aluno = Aluno
        self.Curso = Curso
        self.id = None
    