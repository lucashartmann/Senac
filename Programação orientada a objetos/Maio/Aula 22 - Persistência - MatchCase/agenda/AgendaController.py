import AgendaModel
import AgendaView


def ctrl_listar():
    registros = AgendaModel.listagem(AgendaModel.minha_agenda)
    if registros:
        AgendaView.imprimir(registros)
    else:
        print("Erro")


def ctrl_ajuda():
    AgendaView.imprimir_ajuda()


def ctrl_consultar(email):
    registros = AgendaModel.consultar(AgendaModel.minha_agenda, email)
    if registros:
        AgendaView.imprimir_um((email, registros))
    else:
        print("Registro não encontrado")


def ctrl_apagar(email):
    sucesso = AgendaModel.apagar(AgendaModel.minha_agenda, email)
    if sucesso:
        print(email, "excluído")
    else:
        print("Registro inexistente")


def ctrl_favoritar(email):
    favoritar = AgendaModel.favoritar(
        AgendaModel.minha_agenda, email)
    if favoritar:
        print(f'{email} favoritado!')
    else:
        print(f"{email} inexistente")


def ctrl_cadastrar(email, nome, idade, endereco, favorito):
    cadastrar = AgendaModel.cadastrar(
        AgendaModel.minha_agenda, email, nome, idade, endereco, favorito)
    if cadastrar:
        print(f'{email} cadastrado com sucesso')
    else:
        print(f'Não cadastrado: {email} já existe na agenda')


def ctrl_atualizar(email, nome, idade, endereco, favorito):
    atualizar = AgendaModel.atualizar(
        AgendaModel.minha_agenda, email, nome, idade, endereco, favorito)
    if atualizar:
        print(f'{email} atualizado com sucesso')
    else:
        print(f'{email} não existe na agenda')


def ctrl_atualizar_nome(email, novo_nome):
    favoritar = AgendaModel.atualizar_nome(
        AgendaModel.minha_agenda, email, novo_nome)
    if favoritar:
        print(f'Nome alterado com sucesso: {novo_nome}')
    else:
        print("Erro ao alterar nome")
