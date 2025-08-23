from textual.widgets import Header, Footer, Button, Label, Input, Select
from textual.screen import Screen
from textual.containers import HorizontalGroup
from models.Vendas import Vendas
from textual import on


class TelaVendas(Screen):
    def compose(self):
        yield Header(show_clock=True, icon='😉', time_format="%X")
        
        yield Select((line, line) for line in Vendas.VENDAS.keys())

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
        yield Footer()

    def on_mount(self):
        self.sub_title = "Cadastro de Vendas"

    @on(Select.Changed)
    def select_changed(self, evento: Select.Changed):
        self.valor_select = str(evento.value)

    def on_button_pressed(self, evento: Button.Pressed):
        if evento.button.id == "bt_cadastrar":
            segunda = int(self.query_one("#segunda", Input).value)
            terca = int(self.query_one("#terca", Input).value)
            quarta = int(self.query_one("#quarta", Input).value)
            quinta = int(self.query_one("#quinta", Input).value)
            sexta = int(self.query_one("#sexta", Input).value)
            sabado = int(self.query_one("#sabado", Input).value)
            domingo = int(self.query_one("#domingo", Input).value)

            match self.valor_select:
                case "semana 1":
                    Vendas.VENDAS["semana 1"] = [segunda, terca,
                                                 quarta, quinta, sexta, sabado, domingo]
                case "semana 2":
                    Vendas.VENDAS["semana 2"] = [segunda, terca,
                                                 quarta, quinta, sexta, sabado, domingo]
                case "semana 3":
                    Vendas.VENDAS["semana 3"] = [segunda, terca,
                                                 quarta, quinta, sexta, sabado, domingo]
                case "semana 4":
                    Vendas.VENDAS["semana 4"] = [segunda, terca,
                                                 quarta, quinta, sexta, sabado, domingo]

        if evento.button.id == "bt_limpar":
            for widget in self.query(Input):
                widget.value = ""
