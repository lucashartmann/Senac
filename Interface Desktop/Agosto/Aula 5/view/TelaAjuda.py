from textual.app import App
from textual.widgets import Header, Footer, Button, Static
from textual.screen import Screen
from textual.binding import Binding
from textual.app import App, ComposeResult
from textual.widgets import Sparkline
from view import TelaSecundaria, TelaDashboard, TelaAjuda

class TelaAjuda(Screen):
    def compose(self):
        yield Header(show_clock=True, icon='😉', time_format="%X")
        yield Static("Esta é a tela de ajuda.")
        yield Footer()

    def on_mount(self):
        self.sub_title = "Ajuda"