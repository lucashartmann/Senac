from textual.app import App
from textual import on
from textual.widgets import Header, Label, Button


class AppEstilo(App):

    TITLE = "App com estilo"
    SUB_TITLE = "usando CSS para estilizar a interface"

    CSS_PATH = "app_estilo.css"

    def compose(self):
        yield Header()
        yield Label("Um texto aqui...", id="texto")
        yield Label("Oi, oi, oi")
        yield Label("Hello, hello, hello")
        yield Button("Clique aqui", id="botao")

    @on(Button.Pressed, '#botao')
    def botao_pressionado(self):
        lbl_texto = self.query_one("#texto", Label)
        lbl_texto.styles.color = "white"


if __name__ == "__main__":
    AppEstilo().run()
