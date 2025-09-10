import random
import datetime
import sqlite3

sql_create_table_Livro = '''
CREATE TABLE IF NOT EXISTS Livro (
    id_livro INTEGER PRIMARY KEY NOT NULL,
    codigo TEXT,
    titulo TEXT,
    emprestado INTEGER
);

'''


sql_create_table_leitor = '''
CREATE TABLE IF NOT EXISTS Leitor (
    nome TEXT NOT NULL,
    email TEXT PRIMARY KEY
)
'''

sql_create_table_emprestimo = '''
CREATE TABLE IF NOT EXISTS Emprestimo (
    id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
    id_livro INT NOT NULL,
    email_leitor TEXT NOT NULL,
    data_para_devolucao TEXT NOT NULL,
    FOREIGN KEY (id_livro) REFERENCES Livro(id_livro),
    FOREIGN KEY (email_leitor) REFERENCES Leitor(email)
);
'''

sql_create_table_lista_de_emprestimos = '''
CREATE TABLE IF NOT EXISTS leitor_emprestimo (
    email_leitor TEXT NOT NULL,
    id_emprestimo INTEGER NOT NULL,
    FOREIGN KEY (id_emprestimo) REFERENCES Emprestimo (id_emprestimo),
    FOREIGN KEY (email_leitor) REFERENCES Leitor (email)
);
'''


sql_inserir_dados_livro = '''
    INSERT INTO Livro (codigo, titulo, emprestado)
    VALUES (?, ?, ?);
'''


sql_inserir_dados_leitor = '''
    INSERT INTO Leitor (nome, email)
    VALUES (?, ?);
'''


sql_inserir_dados_emprestimo = '''
    INSERT INTO Emprestimo (id_livro, email_leitor, data_para_devolucao)
    VALUES (?, ?, ?);
'''

sql_inserir_dados_lista_emprestimo = '''
    INSERT INTO leitor_emprestimo (id_emprestimo, email_leitor)
    VALUES (?, ?);
'''

dados_Livro = [
    ("abc-001", "Dom Casmurro", 0),
    ("abc-002", "O Cortiço", 1),
    ("abc-003", "Memórias Póstumas de Brás Cubas", 0),
    ("abc-004", "Capitães da Areia", 1),
    ("abc-005", "A Moreninha", 0),
    ("abc-006", "Senhora", 0),
    ("abc-007", "Iracema", 1),
    ("abc-008", "O Primo Basílio", 0),
    ("abc-009", "Vidas Secas", 1),
    ("abc-010", "O Guarani", 0)
]

dados_leitor = [
    ("Ana Silva", "ana.silva@email.com"),
    ("Bruno Souza", "bruno.souza@email.com"),
    ("Carla Pereira", "carla.pereira@email.com"),
    ("Daniel Costa", "daniel.costa@email.com"),
    ("Eduarda Lima", "eduarda.lima@email.com")
]

dados_emprestimos = [
    ("abc-001", "ana.silva@email.com", "2025-09-15"),
    ("abc-002", "bruno.souza@email.com", "2025-09-20"),
    ("abc-003", "carla.pereira@email.com", "2025-09-18"),
    ("abc-004", "daniel.costa@email.com", "2025-09-22"),
    ("abc-005", "eduarda.lima@email.com", "2025-09-25")
]

with sqlite3.connect("Biblioteca.db") as conexao:

    cursor = conexao.cursor()

    cursor.execute(sql_create_table_Livro)
    cursor.execute(sql_create_table_emprestimo)
    cursor.execute(sql_create_table_leitor)
    cursor.execute(sql_create_table_lista_de_emprestimos)

    cursor.executemany(sql_inserir_dados_livro, dados_Livro)
    cursor.executemany(sql_inserir_dados_leitor, dados_leitor)
    cursor.executemany(sql_inserir_dados_emprestimo, dados_emprestimos)

    conexao.commit()


class Biblioteca:

    def emprestar(self, livro, leitor):
        if livro.is_disponivel():
            livro.set_quant(livro.get_quant() - 1)
            self.banco_dados.atualizar_livro(
                "quantidade", livro.get_codigo(), livro.get_quant())
            livro.atualizar_disponivel()
            if livro.disponivel:
                self.banco_dados.atualizar_livro(
                    "disponivel", livro.get_codigo(), 1)
            else:
                self.banco_dados.atualizar_livro(
                    "disponivel", livro.get_codigo(), 0)
            return Emprestimo.Emprestimo(livro, leitor)
        return None

    def devolver(self, emprestimo):
        leitor = emprestimo.get_leitor()
        livro = emprestimo.get_livro()

        devolucao = leitor.remove_emprestimo(emprestimo)
        if devolucao:
            livro.set_quant(livro.get_quant() + 1)
            self.atualizar_livro(
                "quantidade", livro.get_codigo(), livro.get_quant())
            livro.atualizar_disponivel()
            if livro.disponivel:
                self.atualizar_livro.atualizar_livro(
                    "disponivel", livro.get_codigo(), 1)
            else:
                self.atualizar_livro.atualizar_livro(
                    "disponivel", livro.get_codigo(), 0)
            if not self.get_livro_por_cod(livro.get_codigo()):
                self.add_livro(livro)
            return True
        return False

    def add_livro(self, livro):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()
            try:
                cursor.execute(
                    f'INSERT INTO Livro (titulo, autor, genero, quantidade, capa, disponivel) VALUES (?, ?, ?, ?, ?, ?)', (livro.get_titulo(), livro.get_autor(), livro.get_genero(), livro.get_quant(), livro.get_capa_binaria(), livro.is_disponivel()))
                conexao.commit()
                return True
            except Exception as e:
                print("ERRO ao adicionar livro", e)
                return False

    def add_leitor(self, leitor):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()
            try:
                cursor.execute(
                    f'INSERT INTO Leitor (nome, email) VALUES (?, ?)', (leitor.get_nome(), leitor.get_email()))
                conexao.commit()
                return True
            except Exception as e:
                print("ERRO ao adicionar leitor", e)
                return False

    def add_emprestimo(self, emprestimo):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()

            try:
                cursor.execute(
                    f'INSERT INTO Emprestimo (id_livro, email_leitor, data_para_devolucao) VALUES (?, ?, ?)', (int(emprestimo.get_livro().get_codigo()), emprestimo.get_leitor().get_email(), emprestimo.get_data_para_devolucao()))
                conexao.commit()
                return True
            except Exception as e:
                print("ERRO ao adicionar empréstimo", e)
                return False

    def remove_livro(self, cod_livro):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()

            try:
                sql_delete_query = """
                    DELETE FROM Livro
                    WHERE id_livro = ?;
                    """
                cursor.execute(sql_delete_query, (cod_livro,))
                conexao.commit()
                return True
            except Exception as e:
                print("ERRO ao remover livro", e)
                return False

    def remove_leitor(self, email):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()

            try:
                sql_delete_query = """
                    DELETE FROM Leitor
                    WHERE email = ?;
                    """
                cursor.execute(sql_delete_query, (email,))
                conexao.commit()
                return True
            except Exception as e:
                print("ERRO ao remover leitor", e)
                return False

    def remove_emprestimo(self, id_emprestimo):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()

            try:
                sql_delete_query = """
                    DELETE FROM Emprestimo
                    WHERE id_emprestimo = ?;
                    """
                cursor.execute(sql_delete_query, (id_emprestimo,))
                conexao.commit()
                return True
            except Exception as e:
                print("ERRO ao remover empréstimo", e)
                return False

    def get_emprestimo_por_livro(self, cod_livro):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                f'SELECT * FROM Emprestimo WHERE id_livro = ?', (cod_livro,))
            registro = cursor.fetchone()
            if not registro:
                return None
            livro = self.get_livro_por_cod(registro[1])
            leitor = self.get_leitor_por_email(registro[2])
            emprestimo = Emprestimo.Emprestimo(livro, leitor)
            emprestimo.set_id(registro[0])
            emprestimo.set_data_para_devolucao(registro[-1])
            return emprestimo

    def get_emprestimo_por_id(self, id_emprestimo):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                f'SELECT * FROM Emprestimo WHERE id_emprestimo = ?', (id_emprestimo,))
            registro = cursor.fetchone()
            if not registro:
                return None
            livro = self.get_livro_por_cod(registro[1])
            leitor = self.get_leitor_por_email(registro[2])
            emprestimo = Emprestimo.Emprestimo(livro, leitor)
            emprestimo.set_id(registro[0])
            emprestimo.set_data_para_devolucao(registro[-1])
            return emprestimo

    def get_emprestimos_por_leitor(self, email_leitor):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                f'SELECT * FROM Emprestimo WHERE email_leitor = ?', (email_leitor,))
            lista_registros = cursor.fetchall()
            lista_emprestimos = []
            for registro in lista_registros:
                livro = self.get_livro_por_cod(registro[1])
                leitor = self.get_leitor_por_email(registro[2])
                emprestimo = Emprestimo.Emprestimo(livro, leitor)
                emprestimo.set_id(registro[0])
                emprestimo.set_data_para_devolucao(registro[-1])
                lista_emprestimos.append(emprestimo)

            return lista_emprestimos

    def get_lista_emprestimos(self):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()
            lista = []
            cursor.execute("SELECT * FROM Emprestimo")
            resultados = cursor.fetchall()
            for dados in resultados:
                livro = self.get_livro_por_cod(dados[1])
                leitor = self.get_leitor_por_email(dados[2])
                emprestimo = Emprestimo.Emprestimo(livro, leitor)
                emprestimo.set_id(dados[0])
                emprestimo.set_data_para_devolucao(dados[-1])
                lista.append(emprestimo)
            return lista

    def get_lista_Livro(self):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()
            lista = []
            cursor.execute("SELECT * FROM Livro")
            resultados = cursor.fetchall()
            for dados in resultados:
                livro = Livro.Livro(*dados[1:5])
                livro.set_codigo(dados[0])
                livro.set_capa_binaria(dados[5])
                if dados[-1] == 1:
                    livro.set_disponivel(True)
                else:
                    livro.set_disponivel(False)
                lista.append(livro)
            return lista

    def get_lista_leitores(self):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()
            lista = []
            cursor.execute("SELECT * FROM Leitor")
            resultados = cursor.fetchall()
            for dados in resultados:
                lista.append(Leitor.Leitor(*dados))
            return lista

    def get_livro_por_cod(self, cod_livro):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                f'SELECT * FROM Livro WHERE id_livro = ?', (cod_livro,))
            registro = cursor.fetchone()
            if not registro:
                return None
            livro = Livro.Livro(*registro[1:5])
            livro.set_codigo(registro[0])
            livro.set_capa_binaria(registro[5])
            if registro[-1] == 1:
                livro.set_disponivel(True)
            else:
                livro.set_disponivel(False)
            return livro

    def get_leitor_por_email(self, email):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute(f'SELECT * FROM Leitor WHERE email = ?', (email,))
            registro = cursor.fetchone()
            if not registro:
                return None
            return Leitor.Leitor(*registro)

    def atualizar_livro(self, tipo_dado, condicao, novo_valor):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()
            try:
                sql_update_query = f"""
                UPDATE Livro
                SET {tipo_dado} = ?
                WHERE id_livro = ?;
                """
                dados = (novo_valor, condicao)
                cursor.execute(sql_update_query, dados)
                conexao.commit()
                return True
            except Exception as e:
                print("ERRO ao atualizar livro", e)
                return False

    def atualizar_leitor(self, tipo_dado, condicao, novo_valor):
        with sqlite3.connect("Biblioteca.db") as conexao:
            cursor = conexao.cursor()
            try:
                sql_update_query = f"""
                UPDATE Leitor
                SET {tipo_dado} = ?
                WHERE email = ?;
                """
                dados = (novo_valor, condicao)
                cursor.execute(sql_update_query, dados)
                conexao.commit()
                return True
            except Exception as e:
                print("ERRO ao atualizar leitor", e)
                return False


class Leitor:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Livro:

    def __init__(self, titulo, autor, genero, quant):
        self.codigo = 0
        self.capa_binaria = ""
        self.autor = autor
        self.genero = genero
        self.titulo = titulo
        self.quant = quant
        self.disponivel = True

    def is_disponivel(self):
        return self.disponivel

    def set_capa_binaria(self, caminho):
        if type(caminho) == str:
            if "." in caminho or "/" in caminho or "//" in caminho:
                with open(caminho, 'rb') as f:
                    binario_imagem = f.read()
                self.capa_binaria = binario_imagem
        else:
            self.capa_binaria = caminho

    def set_codigo(self, novo_codigo):
        self.codigo = novo_codigo

    def get_codigo(self):
        return self.codigo

    def set_disponivel(self, novo_disponivel):
        self.disponivel = novo_disponivel

    def get_capa_binaria(self):
        return self.capa_binaria

    def get_autor(self):
        return self.autor

    def get_genero(self):
        return self.genero

    def get_titulo(self):
        return self.titulo

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

    def set_capa(self, nova_capa):
        self.capa = nova_capa

    def set_quant(self, novo_quant):
        self.quant = novo_quant

    def atualizar_disponivel(self):
        if self.get_quant() == 0:
            self.disponivel = False
        else:
            self.disponivel = True


class Emprestimo:

    def __init__(self, livro, leitor):
        self.id = 0
        self.livro = livro
        self.leitor = leitor
        self.data_para_devolucao = self.calcular_data_para_devolucao()

    def calcular_data_para_devolucao(self):
        hoje = datetime.date.today()
        prazo = datetime.timedelta(weeks=random.randint(1, 50))
        data_para_devolucao = hoje + prazo
        data_formatada = data_para_devolucao.isoformat()
        return data_formatada


uma_biblioteca = Biblioteca()
# um_leitor = Leitor("Lucas", "LUCAS@EMAIL")
# um_livro = Livro("Dom Quixote", "Fernando Pessoa", "Ação", 2)
# uma_biblioteca.add_leitor(um_leitor)
# uma_biblioteca.add_livro(um_livro)
# um_emprestimo = uma_biblioteca.emprestar(um_livro, um_leitor)

titulo = "Dom"

with sqlite3.connect('Biblioteca.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute(f'''
    SELECT * FROM Livro where titulo LIKE ?;
                   ''', (f'%{titulo}%',))
    registros = cursor.fetchall()
    print(registros)

