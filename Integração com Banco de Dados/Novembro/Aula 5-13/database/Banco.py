import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from model.Produto import Produto


class Banco:
    def get_conexao(self):
        conexao = None
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                database='padaria',
                user='root',
                password=''
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")

        except Error as e:
            messagebox.showerror("Erro", f"Erro ao conectar! {e}")
        return conexao

    def adicionar_produto(self, produto):
        try:
            with mysql.connector.connect(
                host='localhost',
                database='padaria',
                user='root',
                password=''
            ) as conexao:
                cursor = conexao.cursor()
                produto_dict = produto.to_dict()
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
        try:
            with mysql.connector.connect(
                host='localhost',
                database='padaria',
                user='root',
                password=''
            ) as conexao:
                cursor = conexao.cursor()
                produto_dict = produto.to_dict()
                print(produto_dict)

                sql = "UPDATE produtos SET nome = %s, valor = %s, quantidade = %s WHERE id_produtos = %s"
                valores = (
                    produto_dict['nome'],
                    produto_dict['valor'],
                    produto_dict['quantidade'],
                    produto_dict['id']
                )
                cursor.execute(sql, valores)
                conexao.commit()
                return True
        except Exception as e:
            print(e)
            return False

    def buscar_produtos(self):
        try:
            with mysql.connector.connect(
                host='localhost',
                database='padaria',
                user='root',
                password=''
            ) as conexao:
                cursor = conexao.cursor()
                lista = []
                cursor.execute("SELECT * FROM produtos")
                resultados = cursor.fetchall()
                for dados in resultados:
                    produto = Produto(*dados[1:])
                    produto.set_id(int(dados[0]))
                    lista.append(produto)
                return lista
        except Exception as e:
            print(e)
            return []

    def excluir_produto(self, id_produto):
        try:
            with mysql.connector.connect(
                host='localhost',
                database='padaria',
                user='root',
                password=''
            ) as conexao:
                cursor = conexao.cursor()
                sql_delete_query = """
                        DELETE FROM produtos
                        WHERE id_produtos = %s
                        """
                cursor.execute(sql_delete_query, (id_produto,))
                conexao.commit()
                return True
        except Exception as e:
            print(e)
            return False
