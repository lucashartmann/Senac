from textual.widgets import Header, Footer, Static
from textual.screen import Screen


class TelaAjuda(Screen):
    def compose(self):
        yield Header(show_clock=True, icon='😉', time_format="%X")
        yield Static("Esta é a tela de ajuda.")
        yield Footer()

    def on_mount(self):
        self.sub_title = "Ajuda"
