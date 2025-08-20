from controller import Controller
from model import Init

dados_livro = ["Mãos de cavalo", "Daniel Galera", "Ficção", 1]
dados_leitor = ["Leo", "Leo@email.com"]

cadastro_livro = Controller.cadastrar_livro(dados_livro)
cadastro_leitor = Controller.cadastrar_leitor(dados_leitor)

print(cadastro_livro)
print(cadastro_leitor)

leitor = Init.biblioteca.get_leitor_por_email("Leo@email.com")

print("".join(str(emprestimo)
      for emprestimo in leitor.get_lista_emprestimos()))
print(Controller.emprestar(1, "Leo@email.com"))
print("".join(str(emprestimo)
      for emprestimo in leitor.get_lista_emprestimos()))
print(Controller.devolver(1, "Leo@email.com"))
print("".join(str(emprestimo)
      for emprestimo in leitor.get_lista_emprestimos()))

# # for chave, livro in Init.biblioteca.get_lista_livros().items():
# #     print(f"Chave: {chave}, {livro}")

# for chave, leitor in Init.biblioteca.get_lista_leitores().items():
#     print(f"Chave: {chave}, {leitor}")

# novos_dados_leitor = ["", "Jorge@email.com"]

# print(Controller.editar_leitor("Leo@email.com", novos_dados_leitor))


# for chave, leitor in Init.biblioteca.get_lista_leitores().items():
#     print(f"Chave: {chave}, {leitor}")
