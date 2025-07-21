from textual.app import App, ComposeResult
from textual.widgets import Label, ListItem, ListView, Footer, Header, TextArea
from Item import Item
from textual.events import Load
from textual import on

class AppZero(App):

    TITLE = "Loja"

    items = list()

    for i in range(12):
        items.append(Item())

    def compose(self) -> ComposeResult:
        yield Header()
        # yield ListView()
        # for i in range(len(self.lista_items)):
        #     self.query_one(ListView)._add_child(ListItem(Label(self.lista_items[i].nome)))
        yield ListView(
            ListItem(Label(Item().nome)),
            ListItem(Label(Item().nome)),
                     id="lst_item")
        yield Label("item", id="tx_info")
        yield Footer()

    @on(ListView.Highlighted, "#lst_item")
    def item_selecionado(self) -> None:
        lista = self.query_one("#lst_item", ListView)
        info = self.query_one("#tx_info", Label)
        info.update(self.items[lista.index].nome)

if __name__ == "__main__":
    app = AppZero()
    app.run()