from textual.app import App, ComposeResult
from textual.containers import Horizontal, HorizontalGroup, VerticalScroll, Vertical
from textual.widgets import Button, Footer, Header
from telas.TelaVagao import TelaVagao
from telas.TelaLocomotiva import TelaLocomotiva
from telas.TelaTrem import TelaTrem
from telas.TelaDados import TelaDados
from controller.ControllerCMD import ControllerCMD

# python -m telas.TelaInicial


class TelaApp(App):

    CSS_PATH = "../css/Telas.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cadastrar_vagao":
            self.app.push_screen(TelaVagao())
        elif event.button.id == "cadastrar_locomotiva":
            self.app.push_screen(TelaLocomotiva())
        elif event.button.id == "cadastrar_trem":
            self.app.push_screen(TelaTrem())
        elif event.button.id == "sair":
            self.app.exit()
        elif event.button.id == "dados":
            self.app.push_screen(TelaDados())
        elif event.button.id == "theme":
            self.theme = (
                "textual-dark" if self.theme == "textual-light" else "textual-light"
            )

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def compose(self) -> ComposeResult:
        ControllerCMD.init()
        yield VerticalScroll(
            Horizontal(
                Vertical(
                    Button("Cadastrar Vagão", id="cadastrar_vagao"),
                    Button("Cadastrar Locomotiva", id="cadastrar_locomotiva"),
                ),
                Vertical(
                    Button("Cadastrar Trem", id="cadastrar_trem"),
                    Button("Dados", id="dados"),
                ),
            ),
            Button("Sair", id="sair"),
            id="container_inicial",
        )
        yield Button("Theme", id="theme")


if __name__ == "__main__":
    app = TelaApp()
    app.run()
