from textual.screen import Screen
from textual.widgets import Button

class TelaLeitor(Screen):

    CSS_PATH = "css/TelaLeitor.tcss"

    def compose(self):
        yield Button("Alugar Livro")
        yield Button("Devolver Livro", id="bt_devolucao")
        yield Button("Voltar")

    def on_mount(self):
        self.sub_title = "Tela Inicial"

    def on_button_pressed(self, evento: Button.Pressed):
        if evento.button.id == "bt_devolucao":
            self.screen.app.switch_screen("tela_devolucao")