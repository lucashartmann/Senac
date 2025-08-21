from textual.screen import Screen
from textual.widgets import Button

class TelaAdmin(Screen):

    # CSS_PATH = "TelaAdmin.tcss"

    def compose(self):
        yield Button("Cadastrar Leitor")
        yield Button("Cadastrar Livro")
        yield Button("Estoque", id="bt_estoque")
        yield Button("Clientela")

    def on_mount(self):
        self.sub_title = "Tela Inicial"

    def on_button_pressed(self, evento: Button.Pressed):
        if evento.button.id == "bt_estoque":
            self.screen.app.switch_screen("tela_estoque")
        