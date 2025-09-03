import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')

# Criando um cursor
cursor = conn.cursor()

# Consulta SQL para excluir dados
sql_delete_query = """
DELETE FROM tabela_exemplo
WHERE coluna1 = ?;
"""

# Condição para exclusão
dados = ('valor_a_excluir',)

# Executando a consulta
cursor.execute(sql_delete_query, dados)

# Confirmando as alterações
conn.commit()

# Fechando a conexão
conn.close()