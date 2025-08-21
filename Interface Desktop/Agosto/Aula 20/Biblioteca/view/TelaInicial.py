from textual.screen import Screen
from textual.widgets import Button

class TelaInicial(Screen):

    CSS_PATH = "css/TelaInicial.tcss"

    def compose(self):
        yield Button("Leitor", id="bt_leitor")
        yield Button("Admin", id="bt_admin")

    def on_mount(self):
        self.sub_title = "Tela Inicial"

    def on_button_pressed(self, evento: Button.Pressed):
        if evento.button.id == "bt_leitor":
            self.screen.app.switch_screen("tela_leitor")
        if evento.button.id == "bt_admin":
            self.screen.app.switch_screen("tela_admin")