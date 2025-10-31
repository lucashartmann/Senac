import sqlite3

# Passo 1: Conectar ao banco de dados
conexao = sqlite3.connect('meu_banco.db')

# Passo 2: Criar um cursor
cursor = conexao.cursor()

# Passo 3: Escrever e executar a consulta
email = 'alice@example.com'
cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))

# Passo 4: Obter e exibir o resultado
registro = cursor.fetchone()

if registro:
    print('Registro encontrado:', registro)
else:
    print('Nenhum registro encontrado com o email:', email)

# Passo 5: Fechar a conexão
cursor.close()
conexao.close()