from textual.app import App, ComposeResult
from textual.widgets import Label, ListItem, ListView, Footer, Header, TextArea
from models.Item import Item
from textual.events import Load
from textual import on
from textual.containers import HorizontalGroup
from textual.screen import Screen
from textual.events import Key


class TelaLoja(Screen):
    CSS_PATH = "css/TelaLoja.tcss"

    cacador_margin = [0, 0, 0, 0]
    
    menu = f'''
    🧱🧱🧱🧱🧱🧱🧱
    🧱🪟 🪟 🧱🪟 🪟 🧱
    🧱🪟 🪟 🧱🪟 🪟 🧱
    🧱🧱🧱🧱🧱🧱🧱
    🧱🧱🚪🧱🚪🧱🧱
        '''

    caminho = f'''____🌳______🌳____🐓__🌳___🦃_
    '''
    
    sol = f"☀️"
    
    def compose(self):
        with HorizontalGroup():
            yield Label("🧝", id="elfo")
            yield Label(self.menu)
            yield Label(self.caminho, id="caminho")
            yield Label(self.sol, id="sol")
        yield Label("👮", id="cacador")


    def on_key(self, evento: Key):
        lbl = self.query_one("#cacador")
        self.screen.app.movimentacao(evento, lbl, self.cacador_margin)
       
        if evento.key == "z":
            self.app.switch_screen("loja")


class Loja(Screen):

    CSS_PATH = "css/TelaLoja.tcss"

    descricoes = {
        "Rocha": "Uma simples rocha, útil para arremessar ou bloquear caminhos.",
        "Espada": "Uma espada afiada, perfeita para combates corpo a corpo.",
        "Capa": "Uma capa leve, protege do frio e do vento.",
        "Foice": "Uma foice curva, ideal para colher ou lutar.",
        "Capacete": "Um capacete resistente, protege a cabeça de impactos.",
        "Peitoral": "Um peitoral de armadura, oferece grande proteção ao torso.",
        "Calça": "Uma calça reforçada, protege as pernas durante batalhas.",
        "Picareta": "Uma picareta robusta, essencial para minerar pedras e metais.",
        "Machado": "Um machado pesado, ótimo para cortar madeira ou lutar.",
        "Cenoura": "Uma cenoura fresca, pode ser comida para recuperar energia.",
        "Gema": "Uma gema brilhante, valiosa e rara.",
        "Moeda": "Uma moeda de ouro, usada para comprar itens na loja.",
        "Lira": "Uma lira musical, perfeita para encantar e entreter."
    }

    TITLE = "🧝 Loja do Elfo"

    lista_items = []

    def on_mount(self):
        for i in range(12):
            self.lista_items.append(Item())
        list_view = self.query_one("#lst_item", ListView)
        for item in self.lista_items:
            list_view.append(
                ListItem(Label(item.get_nome().capitalize(), classes="item")))

    def compose(self) -> ComposeResult:
        yield Header()
        with HorizontalGroup(id="ctn_bemvindo"):
            yield Label("🧝")
            yield Label(id="tx_dot1")
            yield Label(id="tx_dot2")
            yield Label("Bem vindo!", id="tx_bemvindo")
        yield ListView(id="lst_item")
        yield Label("item", id="tx_info")
        yield Footer()

    @on(ListView.Highlighted, "#lst_item")
    def item_selecionado(self) -> None:
        lista = self.query_one("#lst_item", ListView)
        info = self.query_one("#tx_info", Label)
        nome_item = self.lista_items[lista.index].get_nome().capitalize()
        if self.lista_items[lista.index].get_icon() != "":
            if nome_item.split()[1].capitalize() in self.descricoes.keys():
                info.update(
                    f"{nome_item}: {self.descricoes[nome_item.split()[1].capitalize()]}")
            else:
                info.update(f"{nome_item}")
        else:
            if nome_item.split()[0] in self.descricoes.keys():
                info.update(
                    f"{nome_item}: {self.descricoes[nome_item.split()[0]]}")
            else:
                info.update(f"{nome_item}")
