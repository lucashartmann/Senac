from textual.widgets import Label, Header, Footer, Static, Select, Input, Pretty, TextArea
from textual.screen import Screen
from textual.containers import HorizontalGroup
from textual.binding import Binding
from models import Item, Init, Cofre


class TelaCadastro(Screen):

    CSS_PATH = "css/TelaCadastro.tcss"

    BINDINGS = {
        Binding("ctrl+s", "salvar", "Salvar"),
        Binding("ctrl+n", "novo_item", "Novo Item")
    }

    def action_salvar(self):
        nome = self.query_one("#input_nome", Input).value
        classe = self.query_one("#sl_classe", Select).value
        Init.JOGADOR.nome = nome
        Init.JOGADOR.classe = classe
        Cofre.Cofre.salvar_jogador()
        self.notify(
            f"Nome: {Init.JOGADOR.nome}, Classe: {Init.JOGADOR.classe}")

    def action_novo_item(self):
        Init.JOGADOR.item_equipado = Item.Item()
        self.atualizar_view()

    def atualizar_view(self):
        self.query_one(TextArea).text = Init.JOGADOR.__str__()

    def on_mount(self):
        self.sub_title = "Tela Cadastro"

    def atualizar_select(self):
        if Init.JOGADOR.classe:
            return Init.JOGADOR.classe
        else:
            Select.value = ""  # Arrumar, não ta dando para selecionar as opções

    def compose(self):
        yield Header()
        yield Static("Novo Jogador")
        with HorizontalGroup():
            yield Label("Nome:", id="lbl_nome")
            yield Input(placeholder="Digite o nome aqui", id="input_nome")
        with HorizontalGroup():
            yield Label("Classe: ")
            yield Select([("Mago", "mago"), ("Caçador", "cacador"), ("Bruxa", "bruxa")], id='sl_classe', value=self.atualizar_select())
        yield TextArea(Init.JOGADOR.__str__())
        yield Footer()
