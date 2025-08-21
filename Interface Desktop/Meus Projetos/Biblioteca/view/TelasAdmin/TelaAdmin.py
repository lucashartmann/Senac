from textual.screen import Screen
from textual.widgets import Button


class TelaAdmin(Screen):

    CSS_PATH = "css/TelaAdmin.tcss"

    def compose(self):
        yield Button("Cadastrar Leitor", id="bt_cadastro_leitor")
        yield Button("Cadastrar Livro", id="bt_cadastro_livro")
        yield Button("Estoque", id="bt_estoque")
        yield Button("Clientela", id="bt_clientela")
        yield Button("Voltar", id="bt_voltar")

    def on_mount(self):
        self.sub_title = "Tela Inicial"

    def on_button_pressed(self, evento: Button.Pressed):
        match evento.button.id:
            case "bt_voltar":
                self.screen.app.switch_screen("tela_inicial")
            case "bt_estoque":
                self.screen.app.switch_screen("tela_estoque")
            case "bt_cadastro_leitor":
                self.screen.app.switch_screen("tela_cadastro_leitor")
            case "bt_cadastro_livro":
                self.screen.app.switch_screen("tela_cadastro_livro")
            case "bt_clientela":
                self.screen.app.switch_screen("tela_clientela")
