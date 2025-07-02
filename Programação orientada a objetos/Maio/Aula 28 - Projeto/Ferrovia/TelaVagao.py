from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Footer, Header, TextArea, Label, Input
import ControllerCMD
from textual.screen import Screen
# python TelaInicial.py


class TelaCadastroVagao(HorizontalGroup):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cadastrar":
            peso = float(self.query_one("#peso_vagao", Input).value)
            mensagem = ControllerCMD.ControllerCMD.adicionar_vagao(peso)
            areaTexto = self.screen.query_one("#mensagem", TextArea)
            areaTexto.text = mensagem

        elif event.button.id == "trocar_tela":
            self.screen.app.pop_screen()

    def compose(self) -> ComposeResult:
        yield Label("Digite o peso do vagão:", id="label_peso_vagao")
        yield Input("Digite aqui", id="peso_vagao")
        yield Button("Cadastrar", id="cadastrar")
        yield Button("Voltar", id="trocar_tela")


class TelaVagao(Screen):

    CSS_PATH = "css/Telas.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalScroll(TelaCadastroVagao())
        yield TextArea(id="mensagem", disabled=True)
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
