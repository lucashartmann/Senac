from textual.app import App
from textual.widgets import Label
from textual.screen import Screen
from view import TelaInicial, TelaCadastro
from textual.binding import Binding

class Dungeoun(App):
    
    SCREENS = {
        "tela_inicial": TelaInicial.TelaInicial,
        "tela_cadastro": TelaCadastro.TelaCadastro
    }

    BINDINGS = {
        Binding("n", "switch_screen('tela_cadastro')", "Tela de Cadastro"),
        Binding("escape", "switch_screen('tela_inicial')", "Tela Inicial")
    }


    TITLE = "Dungeon"

    def on_mount(self):
        self.push_screen("tela_inicial")
