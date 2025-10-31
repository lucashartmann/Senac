import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')

# Criando um cursor
cursor = conn.cursor()

# Consulta SQL para atualizar dados
sql_update_query = """
UPDATE tabela_exemplo
SET coluna1 = ?
WHERE coluna2 = ?;
"""

# Dados para atualização
dados = ('novo_valor', 'condicao')

# Executando a consulta
cursor.execute(sql_update_query, dados)

# Confirmando as alterações
conn.commit()

# Fechando a conexão
conn.close()