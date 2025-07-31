from textual.app import App
from textual.widgets import Static, Button, TextArea
from textual.containers import HorizontalGroup, VerticalGroup
from textual.color import Color

class Tela(App):

    CSS_PATH = "Tela.tcss"

    def compose(self):
        with HorizontalGroup():
            with VerticalGroup():
                    yield Static("texto1", id="texto1")
                    yield Static("texto2", id="texto2")
                    yield Static("texto3", id="texto3")
                    yield Button("Fazer mudanças")
            yield TextArea(id="ta_log")
            
    contador = 10

    def on_button_pressed(self, evento: Button.Pressed):
        areaTexto = self.query_one(TextArea)
        
        areaTexto.text += f"Botão '{evento.button.label}' pressionado\n"
        
        self.contador += 10
        
        static1 = self.query_one("#texto1", Static)
        static1.styles.width = self.contador
        areaTexto.text += f"{static1._content} teve sua altura alterada para {self.contador}\n"
        
        static2 = self.query_one("#texto2", Static)
        static2.styles.height = self.contador
        areaTexto.text += f"{static2._content} teve sua largura alterada para {self.contador}\n"
        
        static3 = self.query_one("#texto3", Static)
        static3.styles.color += Color(190, 160, 34)
        areaTexto.text +=  f"{static3._content} teve sua cor alterada para (0, 10, 34)\n"
        
        for widget in self.query(Static):
            widget.styles.background = Color(100, 200, self.contador)
            areaTexto.text += f"{widget._content} teve sua background color alterada para (100, 200, {self.contador})\n"
            
        if self.contador == 40:
            for widget in self.query(Static):
                widget.remove()
                areaTexto.text += f"{widget._content} foi apagado!\n"


if __name__ == "__main__":
    app = Tela()
    app.run()
