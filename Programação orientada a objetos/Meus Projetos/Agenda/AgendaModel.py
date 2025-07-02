import shelve

minha_agenda = shelve.open("agenda.db", writeback=True)


def cadastrar(agenda, email, nome, idade, endereco, favorito=False):
    if not email in agenda.keys():
        agenda[email] = [nome, idade, endereco, favorito]
        return agenda[email]
    return None


def atualizar(agenda, email, nome, idade, endereco, favorito=False):
    try:
        agenda[email] = [nome, idade, endereco, favorito]
        return agenda[email]
    except KeyError:
        return None


def atualizar_nome(agenda, email, nome):
    try:
        agenda[email][0] = nome
        return True
    except KeyError:
        return False


def favoritar(agenda, email):
    try:
        agenda[email][3] = True
        return True
    except KeyError:
        return False


def apagar(agenda, email):
    try:
        del agenda[email]
        return True
    except KeyError:
        return False


def consultar(agenda, email):
    dados = []
    try:
        dados = agenda[email]
        return dados
    except KeyError:
        return None


def listagem(agenda):
    if len(agenda.items()) > 0:
        return agenda.items()
    return None
