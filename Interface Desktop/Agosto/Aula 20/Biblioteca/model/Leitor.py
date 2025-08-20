class Leitor:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.emprestimos = list()

    def add_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)
        return True

    def get_lista_emprestimos(self):
        return self.emprestimos

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_email(self, novo_email):
        self.email = novo_email


    def __str__(self):
        return f"Leitor [Nome = {self.get_nome()}, Email = {self.get_email()}]"
