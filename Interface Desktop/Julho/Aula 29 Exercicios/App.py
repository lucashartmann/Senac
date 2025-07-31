from textual.app import App
from textual.widgets import Static, Button, TextArea
from textual.containers import HorizontalGroup, VerticalGroup


class Tela(App):

    CSS_PATH = "Tela.tcss"

    def compose(self):
        with HorizontalGroup():
            with VerticalGroup():
                    yield Static("texto1")
                    yield Button("Este é o botão1")
                    yield Static("texto2")
                    yield Button("Este é o botão2")
                    yield Static("texto3")
                    yield Button("Este é o botão3")
            yield TextArea(id="ta_log")

    def on_button_pressed(self, evento: Button.Pressed):
        self.query_one(TextArea).text += f"Botão '{evento.button.label}' pressionado\n"


if __name__ == "__main__":
    app = Tela()
    app.run()
