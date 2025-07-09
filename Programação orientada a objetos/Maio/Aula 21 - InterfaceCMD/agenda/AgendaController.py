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


def test_ctrl_atualizar():
    email = 'srz@email.com'
    nome = 'Senhor Ze'
    idade = 31
    endereco = 'Rua do sr. Z'
    atualizar = AgendaModel.atualizar(
        AgendaModel.minha_agenda, email, nome, idade, endereco)
    if atualizar:
        print(f'{email} atualizado com sucesso')
        dados = AgendaModel.consultar(AgendaModel.minha_agenda, email)
        AgendaView.imprimir_um((email, dados))
    else:
        print(f'{email} não existe na agenda')
