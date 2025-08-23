from textual.app import App
from textual.widgets import Static, Label
from textual.screen import Screen


class Cena():
    def __init__(self, nome="Indefinida"):
        self.nome = nome
        self.itens = {}
        self.norte = None
        self.sul = None
        self.leste = None
        self.oeste = None

    def colocar_item(self, um_item):
        self.itens[um_item.nome] = um_item

    def coletar_item(self, nome_item):
        item_coletado = self.itens[nome_item]
        del self.itens[nome_item]
        return item_coletado

    def __str__(self):
        return f'''
[{self.nome}]
Itens: {self.itens}
'''


class CenaTela(Screen):
    def compose(self):
        yield Label("Essa é a segunda tela")
        yield Static("Tela da Cena")


class CenaApp(App):
    def on_mount(self):
        self.install_screen(CenaTela(), name="Tela da Cena")

    def key_left(self):
        self.push_screen("Tela da Cena")


if __name__ == "__main__":
    app = CenaApp()
    app.run()
