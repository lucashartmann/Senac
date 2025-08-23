from textual.screen import Screen
from textual.widgets import Button
from model import Init


class TelaInicial(Screen):

    CSS_PATH = "css/TelaInicial.tcss"

    def compose(self):
        yield Button("Leitor", id="bt_leitor")
        yield Button("Admin", id="bt_admin")
        yield Button("Encerrar", id="bt_sair")

    def on_mount(self):
        self.sub_title = "Tela Inicial"

    def on_button_pressed(self, evento: Button.Pressed):
        match evento.button.id:
            case "bt_leitor":
                self.screen.app.switch_screen("tela_leitor")
                Init.usuario_leitor = True
            case "bt_admin":
                self.screen.app.switch_screen("tela_admin")
                Init.usuario_leitor = False
            case "bt_sair":
                self.screen.app.exit()
