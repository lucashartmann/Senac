from textual.app import App, ComposeResult
from textual.widgets import Label
from Item import Item


class AppZero(App):

    CSS = '''
        Screen {
            layout: grid;
            grid-size: 4;
            grid-gutter: 5;
            height: auto;
            min-width: 5;
            max-width: 5;
        }
        Label {
            color: pink;
            background: blue;
            padding: 2;
        }
        #lbl_1 {
            background: black;
            color: magenta;
        }
    '''

    def compose(self):
        for i in range(12):
            item = Item()
            yield Label(item.nome)

            
AppZero().run()