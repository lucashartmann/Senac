from textual.app import App, ComposeResult
from textual.widgets import Label, ListItem, ListView, Footer, Header, TextArea
from Item import Item
from textual.events import Load
from textual import on
from textual.containers import HorizontalGroup


class AppZero2(App):

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

    CSS = """
    ListView {
        layout: grid;
        grid-size: 3;
        grid-gutter: 1;
        background: rgb(100, 100, 100);
    }
    ListItem {
        width: 70%;
        text-align: center;
        background: rgb(255, 255, 255);
        height: 99%;
        align: center middle;
        margin: 1;
        margin-left: 11;
        color: green;
    }
    
    .item{
        width: 85%;
        max-width: 85%;
    }
    
    #tx_bemvindo {  
        border: round rgb(255, 255, 255) 50%;
        width: 20;
        min-height: 4;
        max-height: 4;
    }
    
    #ctn_bemvindo{
        align: center middle;
    }
    
    #tx_dot2{
        border: round rgb(255, 255, 255) 50%;
        width: 1;
        min-height: 3;
        max-height: 3;
    }
    
    #tx_dot1{
        border: round rgb(255, 255, 255) 50%;
        width: 1;
        min-height: 1;
        max-height: 1;
    }
    """

    @on(Load)
    def inicializaçao(self):
        self.lista_items = list()
        for i in range(12):
            self.lista_items.append(Item())

    def on_mount(self):
        list_view = self.query_one("#lst_item", ListView)
        for item in self.lista_items:
            list_view.append(
                ListItem(Label(item.nome.capitalize(), classes="item")))

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
        nome_item = self.lista_items[lista.index].nome.capitalize()
        if nome_item.split()[0] in self.descricoes.keys():
            info.update(
                f"{nome_item}: {self.descricoes[nome_item.split()[0]]}")
        else:
            info.update(f"{nome_item}")


if __name__ == "__main__":
    app = AppZero2()
    app.run()
