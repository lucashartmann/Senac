from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Footer, Header, TextArea, Label
import ControllerCMD
from textual.screen import Screen
# python TelaInicial.py


class TelaCadastroTrem(HorizontalGroup):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cadastrar":
            mensagem = ControllerCMD.ControllerCMD.adicionar_trem()
            areaTexto = self.screen.query_one("#mensagem", TextArea)
            areaTexto.text = mensagem

        if event.button.id == "trocar_tela":
            self.screen.app.pop_screen()

    def compose(self) -> ComposeResult:
        yield Button("Criar Trem", id="cadastrar")
        yield Button("Engatar no Trem", id="engatar")
        yield Button("Voltar", id="trocar_tela")


class TelaTrem(Screen):

    CSS_PATH = "css/Telas.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalScroll(TelaCadastroTrem())
        yield TextArea(id="mensagem", disabled=True)
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
