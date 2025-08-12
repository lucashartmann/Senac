from textual.widgets import Header, Footer, Static, TextArea, Button
from textual.screen import Screen
from textual.binding import Binding
from textual.message import Message
from textual.app import App


class TextoDeCima(Static):
    def compose(self):
        yield Static("TEXTO DE CIMA")

    def on_click(self):
        self.notify("Clicou em cima")
        self.post_message(self.Clicou())

    class Clicou(Message):
        pass


class TextoBaixo(Static):
    def compose(self):
        yield Static("TEXTO DE BAIXO")

    def on_click(self):
        self.notify("Clicou em baixo")


class App(App):
    CSS = '''
        Static {
            height: 50%;
            content-align: center middle;
        }

        TextoDeCima {
            background: cyan;
        }

        TextoBaixo {
            background: purple;
        }

    '''

    def compose(self):
        yield TextoDeCima()
        yield TextoBaixo()

    def on_texto_de_cima_clicou(self, evento: TextoDeCima.Clicou):
        self.notify("App ouviu")


if __name__ == "__main__":
    app = App()
    app.run()
