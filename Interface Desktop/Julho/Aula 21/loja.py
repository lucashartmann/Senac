from textual.app import App, ComposeResult
from textual.widgets import Label, ListItem, ListView, Footer, Header, TextArea
from Item import Item
from textual.events import Load
from textual import on

class AppZero(App):

    TITLE = "Loja"
    
  
    @on(Load)
    def inicializaçao(self):
        self.lista_items = list()
        for i in range(12):
            self.lista_items.append(Item())
            
    def on_mount(self):
        list_view = self.query_one("#lst_item", ListView)
        for item in self.lista_items:
            list_view.append(ListItem(Label(item.nome)))
        
        
    def compose(self) -> ComposeResult:
        yield Header()
        yield ListView(id="lst_item")
        yield Label("item", id="tx_info")
        yield Footer()

    @on(ListView.Highlighted, "#lst_item")
    def item_selecionado(self) -> None:
        lista = self.query_one("#lst_item", ListView)
        info = self.query_one("#tx_info", Label)
        info.update(self.lista_items[lista.index].nome)

if __name__ == "__main__":
    app = AppZero()
    app.run()