import sqlite3

sql_create_table_livros = '''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY NOT NULL,
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
    FOREIGN KEY (id_livro) REFERENCES livros(id),
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
    INSERT INTO livros (codigo, titulo, emprestado)
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

dados_livros = [
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

    cursor.execute(sql_create_table_livros)
    cursor.execute(sql_create_table_emprestimo)
    cursor.execute(sql_create_table_leitor)
    cursor.execute(sql_create_table_lista_de_emprestimos)

    cursor.executemany(sql_inserir_dados_livro, dados_livros)
    cursor.executemany(sql_inserir_dados_leitor, dados_leitor)
    cursor.executemany(sql_inserir_dados_emprestimo, dados_emprestimos)
    
    conexao.commit()
