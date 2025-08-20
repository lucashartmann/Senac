from model import Leitor, Livro, Biblioteca

class Init:

    biblioteca = Biblioteca.Biblioteca()
    # livro1 = Livro.Livro("Mãos de cavalo", "Daniel Galera", "Ficção", 1)
    leitor1 = Leitor.Leitor("Lucas", "lucas@email.com")

    # biblioteca.add_livro(livro1)
    biblioteca.add_leitor(leitor1)

    # print("Livro disponivel:", livro1.disponivel)
    # print(livro1.get_quant())

    # emprestimo1 = biblioteca.emprestar(livro1, leitor1)
    # leitor1.add_emprestimo(emprestimo1)

    # print("Quant livro1:", livro1.get_quant())

    # emprestimo1.calcular_data_devolucao()

    # print("Leitor tem livros consigo?", len(leitor1.emprestimos) > 0)

    # print("Livro disponivel:", livro1.disponivel)

    # print("Data de devolução:", emprestimo1.data_devolucao)
