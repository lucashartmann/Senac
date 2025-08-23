from textual.app import App, ComposeResult
from textual.widgets import Label, Button

# python questions01.py

class QuestionApp(App[str]):
    def compose(self):
        yield Label("Você está gostando do Textual?")
        yield Button("Sim", id="yes", variant="primary")
        yield Button("Não", id="no", variant="error")

    def on_button_pressed(self, evento: Button.Pressed):
        self.exit(evento.button.id)


if __name__ == "__main__":
    app = QuestionApp()
    reply = app.run()
    print(reply)