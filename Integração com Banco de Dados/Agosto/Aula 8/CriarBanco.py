import sqlite3

conexao = sqlite3.connect("Banco.db")


sql = '''
CREATE TABLE IF NOT EXISTS personagem (
id, 
nome,
classe
);

'''

sql_insert = '''
INSERT INTO personagem (nome, classe)
VALUES (?, ?);
'''

personagens = [
    ('Pedroso', 'Guerreiro'),
    ('Joana', 'Princesa')
]


conexao.execute(sql)
conexao.execute(sql_insert, ('misterioso', 'rogue'))
conexao.executemany(sql_insert, personagens)
conexao.commit()

conexao.close()
