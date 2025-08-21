from textual.screen import Screen
from textual.widgets import Button


class TelaLeitor(Screen):

    CSS_PATH = "css/TelaLeitor.tcss"

    def compose(self):
        yield Button("Retirar Livro", id="bt_retirada")
        yield Button("Devolver Livro", id="bt_devolucao")
        yield Button("Se Cadastrar", id="bt_cadastro")
        yield Button("Voltar", id="bt_voltar")

    def on_mount(self):
        self.sub_title = "Tela Inicial"

    def on_button_pressed(self, evento: Button.Pressed):
        match evento.button.id:
            case "bt_voltar":
                self.screen.app.switch_screen("tela_inicial")
            case "bt_devolucao":
                self.screen.app.switch_screen("tela_devolucao")
            case "bt_cadastro":
                self.screen.app.switch_screen("tela_cadastro_leitor")
            case "bt_retirada":
                self.screen.app.switch_screen("tela_estoque")
