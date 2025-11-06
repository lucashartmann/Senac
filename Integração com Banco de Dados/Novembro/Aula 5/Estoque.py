from Banco import Banco
from Produto import Produto


class Estoque:
    def buscar_produtos(self):
        try:
            banco = Banco()
            conexao = banco.get_conexao()
            cursor = conexao.cursor()
            lista = []
            cursor.execute("SELECT * FROM produtos")
            resultados = cursor.fetchall()
            for dados in resultados:
                produto = Produto(*dados[1:])
                lista.append(produto)
            return lista
        except Exception as e:
            print(e)
            return []

    def excluir_produto(self, id_produto):
        banco = Banco()
        conexao = banco.get_conexao()
        cursor = conexao.cursor()
        try:
            sql_delete_query = """
                    DELETE FROM Produto
                    WHERE id_produto = ?
                    """
            cursor.execute(sql_delete_query, (id_produto,))
            conexao.commit()
            return True
        except Exception as e:
            print(e)
            return False
