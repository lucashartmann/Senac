from textual.app import App
from textual.widgets import Label
from textual.containers import Center

class Teste(App):

    def compose(self):
        with Center():
            yield Label("🚗", id="carrinho") 

    cont_left = 0
    count_right = 0

    def key_left(self):
        lbl = self.query_one("#carrinho")
        self.cont_left += 1
        lbl.styles.margin = (0, self.cont_left, 0, self.count_right) 

    def key_right(self):
        lbl = self.query_one("#carrinho")
        self.count_right += 1
        lbl.styles.margin = (0, self.cont_left, 0, self.count_right)

if __name__ == "__main__":
    Teste().run()
