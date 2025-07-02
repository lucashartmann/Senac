class Estante:
    id = 0
    def __init__(self):
        self.livros_comprados = []

    def get_id():
        return Estante.id

    def adicionar_livro(self, livro):
        if livro not in self.livros_comprados:
            self.livros_comprados.append(livro)
            livro.id = Estante.id
            Estante.id += 1
            return True
        return False
    
    def remover_livro(self, livro):
        if livro in self.livros_comprados:
            self.livros_comprados.remove(livro)
            return True
        return False
    
    def get_lista_livros(self):
        return self.livros_comprados
    
    def get_lista_livros_nao_iniciados(self):
        livros_finalizados = []
        for livro in self.livros_comprados:
            if livro.get_status() == "Leitura não iniciada":
                livros_finalizados.append(livro)
        return livros_finalizados
    
    def get_lista_livros_em_curso(self):
        livros_em_curso = []
        for livro in self.livros_comprados:
            if livro.get_status() == "Leitura em curso":
                livros_em_curso.append(livro)
        return livros_em_curso
    
    def get_lista_livros_finalizados(self):
        livros_finalizados = []
        for livro in self.livros_comprados:
            if livro.get_status() == "Leitura encerrada":
                livros_finalizados.append(livro)
        return livros_finalizados
    
    def get_livro_por_id(self, id):
        for livro in self.livros_comprados:
            if livro.get_id() == id:
                return livro
        return None
    
    def get_livros_por_autor(self, autor):
        livros_por_autor = []
        for livro in self.livros_comprados:
            if livro.get_autor() == autor:
                livros_por_autor.append(livro)
        return livros_por_autor
    
    def pesquisar_livros_por_titulo(self, titulo):
        livros = []
        for livro in self.livros_comprados:
            if titulo in livro.get_titulo():
                livros.append(livro)
        return livros