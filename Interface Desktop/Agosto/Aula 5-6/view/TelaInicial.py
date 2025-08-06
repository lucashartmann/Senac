from textual.app import App
from textual.widgets import Header, Footer, Button, Static
from textual.screen import Screen
from textual.binding import Binding
from view import TelaSecundaria, TelaDashboard, TelaAjuda, TelaCadastro, TelaCadastroSor


class TelaInicial(Screen):
    def compose(self):
        yield Header(show_clock=True, icon='😉', time_format="%X")
        yield Static("Esta é a tela inicial.")
        yield Footer()

    def on_mount(self):
        self.sub_title = "Inicial"


class AppBase(App):

    TITLE = "Nano"
    SUB_TITLE = "Windows"

    BINDINGS = [
        Binding("left", "switch_screen('secundaria')",
                "Ir para tela secundária"),
        Binding("right", "switch_screen('inicial')", "Ir para tela primaria"),
        Binding("down", "switch_screen('ajuda')", "Ir para tela primaria"),
        Binding("up", "switch_screen('dashboard')", "Ir para a dashboard"),
        Binding("z", "switch_screen('vendas')", "Ir para Vendas"),
        Binding("x", "switch_screen('vendasSor')", "Ir para Vendas sor")
    ]

    SCREENS = {
        "inicial": TelaInicial,
        "secundaria": TelaSecundaria.TelaSecundaria,
        "ajuda": TelaAjuda.TelaAjuda,
        "dashboard": TelaDashboard.TelaDashboard,
        "vendas": TelaCadastro.TelaVendas,
        "vendasSor": TelaCadastroSor.TelaVendas
    }

    def on_mount(self):
        self.push_screen("inicial")

    def compose(self):
        yield Header(show_clock=True, icon='😉', time_format="%X")
        yield Static("Pressione o botão abaixo para interagir:")
        yield Button("Clique aqui", id="btn1")
        yield Footer()

    def on_button_pressed(self):
        self.query_one(Static).update("Você clicou no botão!")
