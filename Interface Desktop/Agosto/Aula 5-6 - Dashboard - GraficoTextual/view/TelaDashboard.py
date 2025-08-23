from textual.widgets import Header, Footer, Static
from textual.screen import Screen
from textual.widgets import Sparkline, DataTable, Pretty
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

        yield DataTable(id="tb_vendas")
        yield Pretty("Lucas", id="Lucas")
        yield Static("Dados 1")
        yield Sparkline(Vendas.VENDAS["semana 1"], id="spk_1")
        yield Static("Dados 2")
        yield Sparkline(Vendas.VENDAS["semana 2"])
        yield Static("Dados 3")
        yield Sparkline(Vendas.VENDAS["semana 3"])
        yield Static("Dados 4")
        yield Sparkline(Vendas.VENDAS["semana 4"])

        yield Footer(show_command_palette=False)

    def on_screen_resume(self):
        contador = 1
        for widget in self.query(Sparkline):
            widget.data = Vendas.VENDAS[f"semana {contador}"]
            contador += 1

    def on_mount(self):
        self.sub_title = "Dashboard"
        tabela = self.query_one(DataTable)

        tabela.add_column("Dia")

        for semana in Vendas.VENDAS.keys():
            tabela.add_column(semana)

        dias = ["Segunda", "Terça", "Quarta",
                "Quinta", "Sexta", "Sábado", "Domingo"]
        semana = ["semana 1", "semana 2", "semana 3", "semana 2"]

        for i in range(7):
            linha = [dias[i]]
            for semana in Vendas.VENDAS.values():
                linha.append(semana[i])
            tabela.add_row(*linha)
