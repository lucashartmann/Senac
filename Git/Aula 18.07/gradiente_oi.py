from textual.app import App
from textual import on
from textual.widgets import Header, Label, Button


class AppEstilo(App):

    TITLE = "App com estilo"
    SUB_TITLE = "usando CSS para estilizar a interface"

    def compose(self):
        yield Header()
        yield Button("Clique aqui", id="botao")

    @on(Button.Pressed, '#botao')
    def botao_pressionado(self):
        for verde in range(0, 255, 16):
            label_oi = Label("###############################")
            label_oi.styles.color = f'rgb(255,{verde},255)'
            self.mount(label_oi)


if __name__ == "__main__":
    AppEstilo().run()
