from textual.app import App
from textual import events
from textual.widgets import Welcome

# python app_intro.py


class AppIntro(App):

    lista_cores = [
        "white"
    ]

    def compose(self):
        yield Welcome()

    def on_button_pressed(self) -> None:
        self.exit()

    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue"

    def on_key(self, evento: events.Key) -> None:
        self.screen.styles.background = self.lista_cores[int(evento.key)]


if __name__ == "__main__":
    app = AppIntro()
    app.run()
