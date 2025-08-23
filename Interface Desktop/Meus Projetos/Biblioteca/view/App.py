from textual.app import App
from view import TelaInicial, TelaEstoqueCapas
from view.TelasLeitor import TelaLeitor
from view.TelasAdmin import TelaAdmin

class App(App):

    SCREENS = {
        "tela_inicial": TelaInicial.TelaInicial,
        "tela_admin": TelaAdmin.TelaAdmin,
        "tela_leitor": TelaLeitor.TelaLeitor,
        "tela_estoque": TelaEstoqueCapas.TelaEstoqueCapas
    }

    def on_mount(self):
        self.title = "Biblioteca"
        self.push_screen("tela_inicial")
