from textual.widgets import Header, Footer, Static
from textual.screen import Screen
from textual.widgets import Sparkline
from models.Vendas import Vendas


class TelaDashboard(Screen):
    data = [1, 2, 2, 1, 1, 4, 3, 1, 1, 8, 8, 2]

    CSS = """
        TelaDashboard {
            align: center middle;
        }

        Sparkline {
            width: 30%;  
            margin: 2;
        }
    """

    def compose(self):
        yield Header(show_clock=True, icon='😉', time_format="%X")
        yield Static("Dados 1")
        yield Sparkline(Vendas.VENDAS["semana 1"])
        yield Static("Dados 2")
        yield Sparkline(Vendas.VENDAS["semana 2"])
        yield Static("Dados 3")
        yield Sparkline(Vendas.VENDAS["semana 3"])
        yield Footer(show_command_palette=False)

    def on_mount(self):
        self.sub_title = "Dashboard"
