from textual.widgets import Label, Header, Footer, Static, Select, Input
from textual.screen import Screen
from textual.containers import HorizontalGroup
from textual.binding import Binding
from models import Cena, Item


class TelaCadastro(Screen):

    CSS_PATH = "css/TelaCadastro.tcss"

    BINDINGS = {
        Binding("ctrl+s", "salvar", "Salvar"),
        Binding("ctrl+n", "novo_item", "Novo Item")
    }

    def action_salvar(self):
        nome = self.query_one("#input_nome", Input).value
        classe = self.query_one("#sl_classe", Select).value
        Cena.JOGADOR.nome = nome
        Cena.JOGADOR.classe = classe
        self.notify(
            f"Nome: {Cena.JOGADOR.nome}, Classe: {Cena.JOGADOR.classe}")

    def action_novo_item(self):
        Cena.JOGADOR.item_equipado = Item.Item()
        stt_item = self.query_one("#stt_item_equipado", Static)
        stt_item.update(
            f"Item equipado: {Cena.JOGADOR.item_equipado.get_nome()}")

    def on_mount(self):
        self.sub_title = "Tela Cadastro"

    def compose(self):
        yield Header()
        yield Static("Novo Jogador")
        with HorizontalGroup():
            yield Label("Nome:", id="lbl_nome")
            yield Input(placeholder="Digite o nome aqui", id="input_nome")
        with HorizontalGroup():
            yield Label("Classe: ")
            yield Select([("Mago", "mago"), ("Caçador", "cacador"), ("Bruxa", "bruxa")], id='sl_classe')
        yield Static(f"Item equipado: ", id="stt_item_equipado")
        yield Footer()
