from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Footer, Header, TextArea, Label, Checkbox, Input
import ControllerCMD
from textual.screen import Screen
# python TelaInicial.py


class TelaCadastroLocomotiva(HorizontalGroup):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cadastrar":
            peso = float(self.query_one("#peso_locomotiva", Input).value)
            combustivel = float(self.query_one("#combustivel_locomotiva", Input).value)
            mensagem = ControllerCMD.ControllerCMD.adicionar_locomotiva(combustivel, peso)
            areaTexto = self.screen.query_one("#mensagem", TextArea)
            areaTexto.text = mensagem

        elif event.button.id == "trocar_tela":
            self.screen.app.pop_screen()

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            yield Label("Digite a quantidade de combustível da locomotiva:", id="label_combustivel_locomotiva")
            yield Label("Digite o peso da locomotiva:", id="label_peso_locomotiva")
        with VerticalScroll():
            yield Input("Digite aqui", id="combustivel_locomotiva")
            yield Input("Digite aqui", id="peso_locomotiva")
        yield Button("Cadastrar", id="cadastrar")
        yield Button("Voltar", id="trocar_tela")
        
class Checkboxes(HorizontalGroup):
    def compose(self) -> ComposeResult:
        yield Checkbox("Gasolina", id="gasolina")
        yield Checkbox("Vapor", id="vapor")
        yield Checkbox("Bateria", id="bateria")


class TelaLocomotiva(Screen):

    CSS_PATH = "css/Telas.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalScroll(TelaCadastroLocomotiva(), Checkboxes())
        yield TextArea(id="mensagem", disabled=True)
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
