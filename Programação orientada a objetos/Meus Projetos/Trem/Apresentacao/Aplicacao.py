from textual.app import App
from textual.widgets import Button, Input
from textual.containers import Horizontal

# python Aplicacao.py

class Tela(App):
    
    CSS = '''
    Input {
        width: 80%;
    }
    Button {
        color: pink;
        background: green;
    }
    Horizontal {
        align: center middle;
    }
    '''
    
    def compose(self):
        yield Horizontal(
            Input("Digite o seu nome"), 
            Button("Cadastrar"),
        )
        
Tela().run()

#python Aplicacao.py