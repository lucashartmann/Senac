from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll, Horizontal
from textual.widgets import Button, Footer, Header, TextArea, Label, Input
from controller.ControllerCMD import ControllerCMD
from textual.screen import Screen
from textual.events import InputEvent, Focus

# python -m telas.TelaInicial

class InputPesoVagao(Input):
    def on_focus(self, event: Focus) -> None:
        self.value = ""

    def _on_blur(self, event):
        if not self.value:
            self.value = "Digite aqui"

class TelaVagao(Screen):

    CSS_PATH = "../css/Telas.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cadastrar":
            peso = float(self.query_one("#input_peso_vagao", Input).value)
            mensagem = ControllerCMD.adicionar_vagao(peso)
            areaTexto = self.screen.query_one("#mensagem", TextArea)
            areaTexto.text = mensagem

        elif event.button.id == "trocar_tela":
            self.screen.app.pop_screen()
                
    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            Horizontal(
                Label("Digite o peso do vagão:", id="label_peso_vagao"),
                InputPesoVagao("Digite aqui", id="input_peso_vagao"),
                Button("Cadastrar", id="cadastrar"),
                Button("Voltar", id="trocar_tela"),
                id="container_inicial",
            ),
        )
        yield TextArea(id="mensagem", disabled=True)
        yield Button("Theme", id="theme")
        


    def _on_mount(self, event):
        acao = Input.on_event.value = "Digite aqui"