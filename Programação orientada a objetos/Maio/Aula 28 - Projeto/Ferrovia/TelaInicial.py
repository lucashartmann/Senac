from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Footer, Header
import TelaVagao
import TelaLocomotiva
import TelaTrem
# python TelaInicial.py


class TelaInicial(HorizontalGroup):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cadastrar_vagao":
            self.app.push_screen(TelaVagao.TelaVagao())
        elif event.button.id == "cadastrar_locomotiva":
            self.app.push_screen(TelaLocomotiva.TelaLocomotiva())
        elif event.button.id == "cadastrar_trem":
            self.app.push_screen(TelaTrem.TelaTrem())
        elif event.button.id == "sair":
            self.app.exit()

    def compose(self) -> ComposeResult:
        self.add_class("tela_inicial")
        with VerticalScroll():
            yield Button("Cadastrar Vagão", id="cadastrar_vagao")
            yield Button("Cadastrar Locomotiva", id="cadastrar_locomotiva")
        with VerticalScroll():
            yield Button("Cadastrar Trem", id="cadastrar_trem")
            yield Button("Sair", id="sair")


class TelaApp(App):

    CSS_PATH = "css/Telas.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield VerticalScroll(TelaInicial())

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = TelaApp()
    app.run()
