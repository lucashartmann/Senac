import sqlite3


class Banco:
    def __init__(self):
        self.init_tables()

    def init_tables(self):
        with sqlite3.connect("Inventario.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
            CREATE TABLE Inventario (
            id_inventario PRIMARY KEY AUTOINCREMENT,
            nome_item TEXT,
            dano INTEGER
            );
                           
            ''')
            conexao.commit()

    def inserir(self, dados):
        with sqlite3.connect("Inventario.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                'INSERT INTO Inventario (nome_item, dano) VALUES (?, ?);', dados)
            conexao.commit()
            return True

    def consultar_itens(self):
        with sqlite3.connect("Inventario.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute('SELECT * from Inventario;')
            registros = cursor.fetchall()
            return registros

    def consulta_por_nome(self, nome):
        with sqlite3.connect("Inventario.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                'SELECT * from Inventario WHERE nome_item = ?;', (nome,))
            registro = cursor.fetchone()
            return registro

    def deletar_por_nome(self, nome):
        with sqlite3.connect("Inventario.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                'DELETE from Inventario WHERE nome_item = ?;', (nome,))
            conexao.commit()
            return True

    def atualizar_item(self, nome):
        with sqlite3.connect("Inventario.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                'UPDATE dano from Inventario WHERE nome_item = ?;', (nome,))
            conexao.commit()
            return True

um_banco = Banco()