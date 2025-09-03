import sqlite3

# Passo 1: Criar o banco de dados
conexao = sqlite3.connect('meu_banco.db')

# Passo 2: Criar a tabela
cursor = conexao.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')
conexao.commit()

# Passo 3: Inserir registros
dados = [
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Carol', 'carol@example.com'),
    ('David', 'david@example.com'),
    ('Eve', 'eve@example.com'),
    ('Frank', 'frank@example.com'),
    ('Grace', 'grace@example.com'),
    ('Hank', 'hank@example.com'),
    ('Ivy', 'ivy@example.com'),
    ('Jack', 'jack@example.com')
]
cursor.executemany('INSERT INTO usuarios (nome, email) VALUES (?, ?)', dados)
conexao.commit()

# Passo 4: Fechar a conexão
cursor.close()
conexao.close()