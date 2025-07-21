from os import system

from textual import on
from textual.app import App
from textual.widgets import Button


class SuspendingApp(App[None]):

    def compose(self):
        yield Button("Open the editor", id="edit")

    @on(Button.Pressed, "#edit")
    def run_external_editor(self) -> None:
        with self.suspend():
            system("vim")


if __name__ == "__main__":
    SuspendingApp().run()
