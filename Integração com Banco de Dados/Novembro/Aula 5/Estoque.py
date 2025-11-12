from Banco import Banco
from Produto import Produto


class Estoque: # ProdutoDAO
    
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
                    DELETE FROM produtos
                    WHERE id_produtos = ?
                    """
            cursor.execute(sql_delete_query, (id_produto,))
            conexao.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def adicionar_produto(self, produto):
        banco = Banco()
        conexao = banco.get_conexao()
        cursor = conexao.cursor()
        produto_dict = produto.to_dict()
        try:
            sql = "INSERT INTO produtos(nome, valor, quantidade) VALUES(%s, %s, %s)"
            valores = (
                produto_dict['nome'], produto_dict['valor'], produto_dict['quantidade'])
            cursor.execute(sql, valores)
            conexao.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def alterar_produto(self, produto):
        banco = Banco()
        conexao = banco.get_conexao()
        cursor = conexao.cursor()
        produto_dict = produto.to_dict()
        try:
            sql = "UPDATE produtos SET nome = ?, valor = ?, quantidade = ?  WHERE produtos_id = ?"
            
            valores = (
                produto_dict['nome'], produto_dict['valor'], produto_dict['quantidade'], produto.get_id())
            cursor.execute(sql, valores)
            conexao.commit()
            return True
        except Exception as e:
            print(e)
            return False