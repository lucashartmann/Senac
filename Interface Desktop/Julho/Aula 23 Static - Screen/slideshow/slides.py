from textual.app import App
from textual.widgets import Static
from textual.screen import Screen


class Slides(App):

    CSS = '''
        Slide01 {background: red;}
        Slide02 {background: blue;}
        Slide03 {background: green;}
    '''

    sequencia_slides = ['slide01', 'slide02', 'slide03']

    slide_atual = 1

    def key_1(self):
        self.proximo_slide()

    def proximo_slide(self):
        if self.slide_atual < len(self.sequencia_slides):
            self.push_screen(self.sequencia_slides[self.slide_atual])
            self.slide_atual += 1
        else:
            self.push_screen(self.sequencia_slides[0])
            self.slide_atual += 1

    def on_mount(self) -> None:
        self.install_screen(Slide01(), name="slide01")
        self.install_screen(Slide02(), name="slide02")
        self.install_screen(Slide03(), name="slide03")


class SlideMestre(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]


class Slide01(SlideMestre):
    def compose(self):
        yield Static("Essa é tela 1")


class Slide02(SlideMestre):
    def compose(self):
        yield Static("Essa é tela 2")


class Slide03(SlideMestre):
    def compose(self):
        yield Static("Essa é tela 3")


if __name__ == "__main__":
    app = Slides()
    app.run()
