from textual.widgets import Header, Footer, Static
from textual.screen import Screen


class TelaSecundaria(Screen):
    def compose(self):
        yield Header(show_clock=True, icon='😉', time_format="%X")
        yield Static("Esta é a tela secundária.")
        yield Footer()

    def on_mount(self):
        self.sub_title = "Secundaria"

    def _on_screen_suspend(self):
        pass
