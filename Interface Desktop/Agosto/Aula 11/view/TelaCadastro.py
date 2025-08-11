from textual.widgets import Label, Header, Footer, Static, Select, Input
from textual.screen import Screen
from textual.containers import HorizontalGroup
from textual.binding import Binding


class TelaCadastro(Screen):

    CSS_PATH = "css/TelaCadastro.tcss"

    BINDINGS = {
        Binding("ctrl+s", "salvar", "Salvar")
    }

    def action_salvar(self):
        nome = self.query_one("#input_nome", Input).value
        classe = self.query_one("#sl_classe", Select).value
        self.notify(f"{nome} {classe}")

    def on_mount(self):
        self.sub_title = "Tela Cadastro"

    def compose(self):
        yield Header()
        yield Static("Novo Jogador")
        with HorizontalGroup():
            yield Label("Nome:", id="lbl_nome")
            yield Input(placeholder="Digite o nome aqui", id="input_nome")
        yield Select([("Mago", "mago"), ("Caçador", "cacador"), ("Bruxa", "bruxa")], id='sl_classe')
        yield Footer()
