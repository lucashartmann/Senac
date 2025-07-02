class Aluno:
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma
        self.notas = []
        self.media = self.calcula_media()
        self.situacao = self.verifica_situacao()

    def adicionar_nota(self, nota):
        if nota not in self.notas:
            self.notas.append(nota)
            self.media = self.calcula_media()
            self.situacao = self.verifica_situacao()
            return True
        return False

    def remover_nota(self, nota):
        if nota in self.notas:
            self.notas.remove(nota)
            self.media = self.calcula_media()
            self.situacao = self.verifica_situacao()
            return True
        return False

    def verifica_situacao(self):
        if (len(self.notas) == 0):
            return "Cursando"
        if self.media >= 7:
            return "Aprovado"
        return "Reprovado"

    def calcula_media(self):
        if (len(self.notas) == 0):
            return 0
        self.media = sum(self.notas) / len(self.notas)
        return self.media
