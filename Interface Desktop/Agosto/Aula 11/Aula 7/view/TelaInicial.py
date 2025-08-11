from textual.widgets import Header, Footer, Static
from textual.screen import Screen
from textual.containers import VerticalGroup


class TelaInicial(Screen):

    CSS_PATH = "css/TelaInicial.tcss"

    titulo = '''
██████╗░██╗░░░██╗███╗░░██╗░██████╗░███████╗░█████╗░██╗░░░██╗███╗░░██╗
██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝██╔══██╗██║░░░██║████╗░██║
██║░░██║██║░░░██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║██║░░░██║██╔██╗██║
██║░░██║██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║██║░░░██║██║╚████║
██████╔╝╚██████╔╝██║░╚███║╚██████╔╝███████╗╚█████╔╝╚██████╔╝██║░╚███║
╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚══╝'''

    def compose(self):
        yield Header()
        with VerticalGroup():
            yield Static(self.titulo)
            yield Static("𝔘𝔪 𝔡𝔲𝔫𝔤𝔢𝔬𝔫 𝔠𝔯𝔞𝔴𝔩𝔢𝔯 𝔢𝔪 𝔪𝔬𝔡𝔬 𝔱𝔢𝔵𝔱𝔯𝔬")
        yield Footer()

    def on_mount(self):
        self.sub_title = "Tela Inicial"
