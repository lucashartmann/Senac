from model import Livro, Leitor, Emprestimo


class Biblioteca:

    def __init__(self):
        self.nome = ""
        self.livros = dict()
        self.leitores = dict()

    def emprestar(self, livro: Livro.Livro, leitor: Leitor.Leitor):
        livro.set_quant(livro.get_quant() - 1)
        livro.atualizar_disponivel()
        return Emprestimo.Emprestimo(livro, leitor)

    def get_lista_livros(self):
        return self.livros

    def get_lista_leitores(self):
        return self.leitores

    def get_livro_por_cod(self, cod_livro):
        if cod_livro in self.livros.keys():
            return self.livros[cod_livro]
        return None

    def get_leitor_por_email(self, email):
        if email in self.leitores.keys():
            return self.leitores[email]
        return None

    def add_livro(self, cod_livro, livro):
        if cod_livro not in self.livros.keys():
            self.livros[cod_livro] = livro
            return True
        return False

    def add_leitor(self, email, leitor):
        if email not in self.leitores.keys():
            self.leitores[email] = leitor
            return True
        return False

    def remove_livro(self, cod_livro):
        if cod_livro in self.livros.keys():
            del self.livros[cod_livro]
            return True
        return False

    def remove_leitor(self, email):
        if email in self.leitores.keys():
            del self.leitores[email]
            return True
        return False

    def __str__(self):
        return f"Biblioteca [Livros = {self.get_lista_livros()}, Leitores = {self.get_lista_leitores()}]"
