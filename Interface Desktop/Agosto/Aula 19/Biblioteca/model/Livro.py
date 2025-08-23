class Livro:
    cod = 0

    def __init__(self, titulo, autor, genero, quant):
        self.autor = autor
        self.genero = genero
        self.titulo = titulo
        self.codigo = self.gerar_cod()
        self.quant = quant
        self.disponivel = True

    def gerar_cod(self):
        Livro.cod += 1
        return Livro.cod

    def get_autor(self):
        return self.autor

    def get_genero(self):
        return self.genero

    def get_titulo(self):
        return self.titulo

    def get_codigo(self):
        return self.codigo

    def get_quant(self):
        return self.quant

    def is_disponivel(self):
        return self.disponivel

    def set_autor(self, novo_autor):
        self.autor = novo_autor

    def set_genero(self, novo_genero):
        self.genero = novo_genero

    def set_titulo(self, novo_titulo):
        self.titulo = novo_titulo

    def set_quant(self, novo_quant):
        self.quant = novo_quant

    def atualizar_disponivel(self):
        if self.get_quant() <= 0:
            self.disponivel = False

    def __str__(self):
        return f"Livro [Titulo = {self.get_titulo()}, Autor = {self.get_autor()}, Genero + {self.get_genero()}]"
