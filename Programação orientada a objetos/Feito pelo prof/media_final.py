class Aluno:    
    def __init__(self, nome, turma):        
        self.nome = nome
        self.turma = turma
        self.situacao = 'cursando'
        self.notas = []
        self.media = 0.0    

    def receber_nota(self, uma_nota):
        self.notas.append(uma_nota)

    def calcular_media(self):        
        total_notas = sum(self.notas) # sum = soma = somatório
        if total_notas > 0:
            self.media = total_notas / len(self.notas) # len = length = comprimento
            #self.atualizar_situacao()

    def atualizar_situacao(self):
        if len(self.notas) >=3:
            if self.media >=7:
                self.situacao = 'aprovado'
            else:
                self.situacao = 'reprovado'

def imprimir_boletim(turma):
    for aluno in turma:
        # Imprime boletim do aluno
        boletim = f"{aluno.nome}    {aluno.turma}   {aluno.notas}   {aluno.media}   {aluno.situacao}"  
        print(boletim)

def cadastrar_aluno(turma):
    # Cadastra um aluno e suas 3 notas
    _nome = input("Nome: ")
    _turma = input("Turma: ")

    _um_aluno = Aluno(_nome, _turma)

    for n in range(3):
        _nota = float(input(f"Nota {n+1}: "))
        _um_aluno.receber_nota(_nota)

    _um_aluno.calcular_media()
    _um_aluno.atualizar_situacao()

    turma.append(_um_aluno)


curso = []

for i in range(3):
    cadastrar_aluno(curso)

imprimir_boletim(curso)

