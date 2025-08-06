from textual.widgets import Header, Footer, Button, Label, Input, TabbedContent, TabPane
from textual.screen import Screen
from textual.containers import HorizontalGroup, VerticalGroup, VerticalScroll
from models.Vendas import Vendas
from textual import on


class WidgetCadastro(VerticalGroup):
    def __init__(self, id_semana):
        super().__init__()
        self.id_semana = id_semana

    def compose(self):
        with HorizontalGroup():
            yield Label("Segunda")
            yield Input(id="segunda")
        with HorizontalGroup():
            yield Label("Terça")
            yield Input(id="terca")
        with HorizontalGroup():
            yield Label("Quarta")
            yield Input(id="quarta")
        with HorizontalGroup():
            yield Label("Quinta")
            yield Input(id="quinta")
        with HorizontalGroup():
            yield Label("Sexta")
            yield Input(id="sexta")
        with HorizontalGroup():
            yield Label("Sabado")
            yield Input(id="sabado")
        with HorizontalGroup():
            yield Label("Domingo")
            yield Input(id="domingo")
        yield Button("Limpar", id="bt_limpar")
        yield Button("Cadastrar", id="bt_cadastrar")


class TelaVendas(Screen):
    def compose(self):
        yield Header(show_clock=True, icon='😉', time_format="%X")
        with TabbedContent():
            with TabPane("Semana 1"):
                yield WidgetCadastro("semana 1")
            with TabPane("Semana 2"):
                yield WidgetCadastro("semana 2")
            with TabPane("Semana 3"):
                yield WidgetCadastro("semana 3")
            with TabPane("Semana 4"):
                yield WidgetCadastro("semana 4")
        yield Footer()

    def on_mount(self):
        self.sub_title = "Cadastro de Vendas"

    def on_button_pressed(self, evento: Button.Pressed):
        if evento.button.id == "bt_cadastrar":
            segunda = int(self.query_one("#segunda", Input).value)
            terca = int(self.query_one("#terca", Input).value)
            quarta = int(self.query_one("#quarta", Input).value)
            quinta = int(self.query_one("#quinta", Input).value)
            sexta = int(self.query_one("#sexta", Input).value)
            sabado = int(self.query_one("#sabado", Input).value)
            domingo = int(self.query_one("#domingo", Input).value)

            Vendas.VENDAS[self.id_semana] = [segunda, terca,
                                             quarta, quinta, sexta, sabado, domingo]

        if evento.button.id == "bt_limpar":
            for widget in self.query(Input):
                widget.value = ""
