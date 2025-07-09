def imprimir(registros):
    for email, dados in registros:
        print(f'''e-mail: {email}
    Nome: {dados[0]}        
    Endereço: {dados[2]}
    Idade: {dados[1]}
    Favorito: {dados[3]}        
    ''')


def imprimir_um(registro):
    email, dados = registro
    print(f'''e-mail: {email}
    Nome: {dados[0]}        
    Endereço: {dados[2]}
    Idade: {dados[1]}
    Favorito: {dados[3]}        
    ''')


def imprimir_ajuda():
    ajuda = '''
Comandos: 
ajuda
listar
    '''
    print(ajuda)
