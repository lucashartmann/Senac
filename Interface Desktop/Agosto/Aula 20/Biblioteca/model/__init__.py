from model import Leitor, Livro, Biblioteca
from controller import Controller


class Init:

    biblioteca = Biblioteca.Biblioteca()
    livro1 = Livro.Livro("Diario de um Banana", "Jeff Kinney", "Humor", 1)
    leitor1 = Leitor.Leitor("Lucas", "lucas@email.com")

    biblioteca.add_livro(livro1)
    biblioteca.add_leitor(leitor1)

    leitor1.add_emprestimo(biblioteca.emprestar(livro1, leitor1))
