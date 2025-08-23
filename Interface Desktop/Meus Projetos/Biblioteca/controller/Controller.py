from model import Leitor, Livro, Init
from rich_pixels import Pixels
from PIL import Image
import os


def get_capa(cod_livro):
    try:
        cod_livro = int(cod_livro)
    except:
        return f"ERRO ao converter {cod_livro}"

    livro = Init.biblioteca.get_livro_por_cod(cod_livro)
    if livro.get_capa():
        return livro.get_capa()
    else:
        return None


def resize(caminho, tamanho):
    size = tamanho, tamanho

    if not os.path.exists(caminho):
        print(f"Imagem não encontrada: {caminho}")
        return False, ""

    try:
        im = Image.open(caminho)
        im.thumbnail(size, Image.Resampling.LANCZOS)
        novo_caminho = f"{caminho.split('.')[0]}copia.{caminho.split('.')[1]}"
        if os.path.exists(novo_caminho):
            os.remove(novo_caminho)
        im.save(novo_caminho)
    except ValueError:
        print(caminho)
        print(novo_caminho)
        return False, ""
    return True, novo_caminho


def gerar_pixel(caminho, tamanho):
    if tamanho:
        bool, novo_caminho = resize(caminho, tamanho)
    else:
        im = Image.open(caminho)
        novo_caminho = f"{caminho.split('.')[0]}copia.{caminho.split('.')[1]}"
        if os.path.exists(novo_caminho):
            os.remove(novo_caminho)
        im.save(novo_caminho)
        bool = True
    if bool:
        try:
            pixels = Pixels.from_image_path(novo_caminho)
            if os.path.exists(novo_caminho):
                os.remove(novo_caminho)
            return pixels
        except Exception:
            print(f"Erro ao gerar pixels")
            return None
    return None


def get_livros_biblioteca():
    return Init.biblioteca.get_lista_livros()


def get_leitores_biblioteca():
    return Init.biblioteca.get_lista_leitores()


def emprestar(cod_livro, email):
    try:
        cod_livro = int(cod_livro)
    except:
        return f"ERRO ao converter {cod_livro}"

    livro = Init.biblioteca.get_livro_por_cod(cod_livro)
    leitor = Init.biblioteca.get_leitor_por_email(email)

    if not livro:
        return f"Erro, livro '{livro.get_codigo()}' não existe"

    if not leitor:
        return f"Erro, leitor '{leitor.get_email()}' não existe"

    emprestimo = Init.biblioteca.emprestar(livro, leitor)

    if emprestimo:
        adicao = leitor.add_emprestimo(emprestimo)
        if adicao:
            return f"Livro '{livro.get_titulo()}' emprestado com sucesso"
        else:
            "Erro ao adicionar emprestimo ao leitor"
    else:
        return f"Erro ao emprestar livro '{livro.get_titulo()}', livro não está disponivel"


def devolver(cod_livro, email):
    try:
        cod_livro = int(cod_livro)
    except:
        return f"ERRO ao converter {cod_livro}"

    livro = Init.biblioteca.get_livro_por_cod(cod_livro)
    leitor = Init.biblioteca.get_leitor_por_email(email)

    if not livro:
        return f"Erro, livro '{livro.get_codigo()}' não existe"

    if not leitor:
        return f"Erro, leitor '{leitor.get_email()}' não existe"

    emprestimo = leitor.get_emprestimo_por_livro(cod_livro)

    if not emprestimo:
        return f"Erro, empréstimo não existe"

    devolucao = Init.biblioteca.devolver(emprestimo)

    if devolucao:
        return f"Livro '{livro.get_titulo()}' devolvido com sucesso"
    else:
        return f"Erro ao devolver livro '{livro.get_titulo()}'"


def cadastrar_livro(dados):
    titulo = dados[0]
    autor = dados[1]
    quant = dados[2]
    genero = dados[3]

    if titulo == "":
        return "Erro, titulo vazio"

    if autor == "":
        return "Erro, autor vazio"

    if genero == "":
        return "Erro, genero vazio"

    if quant == "":
        return "Erro, quant vazio"

    try:
        quant = int(quant)
    except:
        return f"Erro ao converter '{quant}'"

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

    if nome == "":
        return "Erro, nome vazio"

    if email == "":
        return "Erro, email vazio"

    leitor = Leitor.Leitor(nome, email)

    if not leitor:
        return "ERRO ao criar leitor"

    cadastro = Init.biblioteca.add_leitor(leitor)

    if cadastro:
        Init.leitor1 = leitor
        return f"Leitor cadastrado com sucesso\n{leitor}"
    return "ERRO ao cadastrar leitor"


def excluir_livro(cod_livro):
    try:
        cod_livro = int(cod_livro)
    except:
        return f"ERRO ao converter '{cod_livro}'"

    remocao = Init.biblioteca.remove_livro(cod_livro)

    if remocao:
        return f"Livro '{cod_livro}' removido com sucesso!"
    else:
        return f"Erro, não existe livro com código '{cod_livro}'"


def excluir_leitor(email):
    remocao = Init.biblioteca.remove_leitor(email)

    if remocao:
        return f"Leitor '{email}' removido com sucesso"
    else:
        return f"Erro, leitor '{email}' não existe"


def editar_leitor(email, dados):
    leitor = Init.biblioteca.get_leitor_por_email(email)

    if not leitor:
        return f"Erro, leitor '{leitor.get_email()}' não existe"

    mensagem = ""

    novo_nome = dados[0]
    novo_email = dados[1]

    if novo_nome != "":
        leitor.set_nome(novo_nome)
        mensagem += f"Nome editado '{novo_nome}'\n"
    if novo_email != "":
        if Init.biblioteca.get_leitor_por_email(novo_email):
            mensagem += f"Erro, '{novo_email}' já cadastrado"
        else:
            Init.biblioteca.remove_leitor(email)
            leitor.set_email(novo_email)
            Init.biblioteca.add_leitor(leitor)
            mensagem += f"Email editado '{novo_email}'"
    return mensagem


def editar_livro(cod_livro, dados):
    try:
        cod_livro = int(cod_livro)
    except:
        return f"ERRO ao converter '{cod_livro}'"

    livro = Init.biblioteca.get_livro_por_cod(cod_livro)

    if not livro:
        return f"Erro, não existe livro com código '{cod_livro}'"

    mensagem = ""

    titulo = dados[0]
    autor = dados[1]
    quant = dados[2]
    caminho_capa = dados[3]
    tamanho_capa = dados[4]
    genero = dados[5]

    if titulo != "":
        livro.set_titulo(titulo)
        mensagem += f"Titulo editado '{titulo}'\n"
    if autor != "":
        livro.set_autor(autor)
        mensagem += f"Autor editado '{autor}'\n"
    if genero != "":
        livro.set_genero(genero)
        mensagem += f"Genero editado '{genero}'\n"
    if quant != "":
        try:
            quant = int(quant)
            livro.set_quant(quant)
            mensagem += f"Quant editado '{quant}'"
        except:
            mensagem += f"Erro ao converter '{quant}'"

    if caminho_capa != "" and tamanho_capa != "":
        try:
            tamanho_capa = int(tamanho_capa)
            gerar_capa = gerar_pixel(caminho_capa, tamanho_capa)
            if gerar_capa:
                livro.set_capa(gerar_capa)
                mensagem += f"Capa editada\n"
            else:
                mensagem += "Erro ao gerar capa"
        except:
            mensagem += f"Erro ao converter '{tamanho_capa}'"

    if caminho_capa != "" and tamanho_capa == "":
        gerar_capa = gerar_pixel(caminho_capa, tamanho_capa)
        if gerar_capa:
            livro.set_capa(gerar_capa)
            mensagem += f"Caminho editado\n"
        else:
            mensagem += "Erro ao gerar capa"

    if caminho_capa == "" and tamanho_capa != "":
        if livro.get_caminho_capa():
            gerar_capa = gerar_pixel(livro.get_caminho_capa(), tamanho_capa)
            if gerar_capa:
                livro.set_capa(gerar_capa)
                livro.set_tamanho_capa(tamanho_capa)
                mensagem += f"Tamanho editado\n"
            else:
                mensagem += "Erro ao gerar capa"
        else:
            mensagem += "Capa precisa ter um caminho"

    return mensagem
