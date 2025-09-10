import sqlite3


class Banco:
    def __init__(self):
        self.init_tables()

    def init_tables(self):
        with sqlite3.connect("Inventario.db") as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute('''
                CREATE TABLE Inventario (
                id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_item TEXT,
                dano INTEGER
                );
                            
                ''')
                conexao.commit()
            except Exception as e:
                print("ERRO!", e)

    def inserir(self, dados):
        with sqlite3.connect("Inventario.db") as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(
                    'INSERT INTO Inventario (nome_item, dano) VALUES (?, ?);', dados)
                conexao.commit()
                return True
            except Exception as e:
                print("ERRO!", e)
                return False

    def consultar_itens(self):
        with sqlite3.connect("Inventario.db") as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute('SELECT * from Inventario;')
                registros = cursor.fetchall()
                return registros
            except Exception as e:
                print("ERRO!", e)
                return []

    def consulta_por_nome(self, nome):
        with sqlite3.connect("Inventario.db") as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(
                    'SELECT * from Inventario WHERE nome_item = ?;', (nome,))
                registro = cursor.fetchone()
                return registro
            except Exception as e:
                print("ERRO!", e)
                return None

    def deletar_por_nome(self, nome):
        with sqlite3.connect("Inventario.db") as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(
                    'DELETE from Inventario WHERE nome_item = ?;', (nome,))
                conexao.commit()
                return True
            except Exception as e:
                print("ERRO!", e)
                return False

    def atualizar_item(self, nome):
        with sqlite3.connect("Inventario.db") as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(
                    'UPDATE dano from Inventario WHERE nome_item = ?;', (nome,))
                conexao.commit()
                return True
            except Exception as e:
                print("ERRO!", e)
                return False

