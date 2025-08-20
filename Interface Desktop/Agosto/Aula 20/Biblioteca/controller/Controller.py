from model import Leitor, Livro, Biblioteca, Init


def emprestar(cod_livro, email):
    livro = Init.biblioteca.get_livro_por_cod(cod_livro)
    leitor = Init.biblioteca.get_leitor_por_email(email)

    if not livro:
        return f"Erro, livro {livro.get_codigo()} não existe"

    if not leitor:
        return "Erro, autor não existe"

    emprestimo = Init.biblioteca.emprestar(livro, leitor)

    if emprestimo:
        return f"Livro {livro.get_codigo()} emprestado com sucesso"
    else:
        return f"Erro ao emprestar livro {livro.get_codigo()}"


def devolver(cod_livro, email):
    livro = Init.biblioteca.get_livro_por_cod(cod_livro)
    leitor = Init.biblioteca.get_leitor_por_email(email)

    if not livro:
        return f"Erro, livro {livro.get_codigo()} não existe"

    if not leitor:
        return "Erro, autor não existe"

    devolucao = Init.biblioteca.devolver(livro)

    if devolucao:
        return f"Livro {livro.get_codigo()} devolvido com sucesso"
    else:
        return f"Erro ao devolver livro {livro.get_codigo()}"


def cadastrar_livro(dados):
    titulo = dados[0]
    autor = dados[1]
    genero = dados[2]
    quant = dados[3]

    try:
        quant = int(quant)
    except:
        return f"Erro ao converter {quant}"

    livro = Livro.Livro(titulo, autor, genero, quant)

    if not Livro:
        return "ERRO ao criar livro"

    cadastro = Init.biblioteca.add_livro(livro)

    if cadastro:
        return f"Livro cadastrado com sucesso\n{livro}"
    return "ERRO ao cadastrar livro"

def cadastrar_leitor(dados):
    nome = dados[0]
    email = dados[1]

    leitor = Leitor.Leitor(nome, email)

    if not leitor:
        return "ERRO ao criar leitor"

    cadastro = Init.biblioteca.add_leitor(leitor)

    if cadastro:
        return f"Leitor cadastrado com sucesso\n{leitor}"
    return "ERRO ao cadastrar leitor"


def excluir_livro(cod_livro):
    livro = Init.biblioteca.get_livro_por_cod(cod_livro)

    if not livro:
        return f"Erro, não existe livro com código {cod_livro}"

    Init.biblioteca.remove_livro(livro)

    return "Livro removido com sucesso!"


def excluir_leitor(email):
    leitor = Init.biblioteca.get_leitor_por_email(email)

    if not leitor:
        return "Erro, leitor não existe"

    remocao = Init.biblioteca.remove_leitor(leitor)

    return "Autor removido com sucesso"


def editar_leitor(email, dados):
    leitor = Init.biblioteca.get_leitor_por_email(email)

    if not leitor:
        return "Erro, leitor não existe"
    
    mensagem = ""

    novo_nome = dados[0]
    novo_email = dados[1]

    if novo_nome != "":
        leitor.set_nome(novo_nome)
        mensagem += f"Nome editado {novo_nome}\n"
    if novo_email != "":
        if Init.biblioteca.get_leitor_por_email(novo_email):
            mensagem += f"Erro, email já cadastrado"
        else:
            Init.biblioteca.remove_leitor(email)
            # Tem que apagar a chave e criar uma nova
            leitor.set_email(novo_email)
            mensagem += f"Email editado {novo_email}\n"
    return mensagem


def editar_livro(cod_livro, dados):

    livro = Init.biblioteca.get_livro_por_cod(cod_livro)

    if not livro:
        return f"Erro, não existe livro com código {cod_livro}"

    mensagem = ""

    titulo = dados[0]
    autor = dados[1]
    genero = dados[2]
    quant = dados[3]

    if titulo != "":
        livro.set_nome(titulo)
        mensagem += f"Titulo editado {titulo}\n"
    if autor != "":
        livro.set_autor(autor)
        mensagem += f"Autor editado {autor}\n"
    if genero != "":
        livro.set_genero(genero)
        mensagem += f"Genero editado {genero}\n"
    if quant != "":
        try:
            quant = int(quant)
            livro.set_quant(quant)
            mensagem += f"Quant editado {quant}\n"
        except:
            mensagem += f"Erro ao converter {quant}\n"

    return mensagem
