from textual.app import App
from textual.screen import Screen
from textual.widgets import Static

textoDeErro = """
Ocorreu um erro. Para continuar:

Pressione Enter para retornar ao Windows ou

Pressione CTRL+ALT+DEL para reiniciar o computador. Se fizer isso,
você perderá todas as informações não salvas em todos os aplicativos abertos.

Erro: 0E : 016F : BFF9B3D4
"""


class BSOD(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self):
        yield Static(" Windows ", id="title")
        yield Static(textoDeErro)
        yield Static("Pressione qualquer tecla para continuar [blink]_[/]", id="any-key")


class BSODApp(App):
    BINDINGS = [("b", "push_screen('bsod')", "BSOD")]

    CSS_PATH = "bsod.tcss"

    def on_mount(self) -> None:
        self.install_screen(BSOD(), name="bsod")


if __name__ == "__main__":
    app = BSODApp()
    app.run()
