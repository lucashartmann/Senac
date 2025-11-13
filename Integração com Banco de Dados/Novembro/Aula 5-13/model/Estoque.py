from database.Banco import Banco


class Estoque:  # ProdutoDAO

    def __init__(self):
        self.banco = Banco()

    def buscar_produtos(self):
        return self.banco.buscar_produtos()

    def excluir_produto(self, id_produto):
        return self.banco.excluir_produto(id_produto)

    def adicionar_produto(self, produto):
        return self.banco.adicionar_produto(produto)

    def alterar_produto(self, produto):
        return self.banco.alterar_produto(produto)
