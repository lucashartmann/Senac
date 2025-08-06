from textual.widgets import Header, Footer, Static
from textual.screen import Screen
from textual.widgets import Sparkline
from models.Vendas import Vendas


class TelaDashboard(Screen):
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
        yield Sparkline(Vendas.VENDAS["semana 1"], id="spk_1")
        yield Static("Dados 2")
        yield Sparkline(Vendas.VENDAS["semana 2"])
        yield Static("Dados 3")
        yield Sparkline(Vendas.VENDAS["semana 3"])
        yield Footer(show_command_palette=False)
    
    def on_screen_resume(self):
        self.query_one("#spk_1", Sparkline).data = Vendas.VENDAS["semana 1"]

    
    def on_mount(self):
        self.sub_title = "Dashboard"
