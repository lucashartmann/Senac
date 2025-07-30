from textual.app import App 
from textual.widgets import Static, Button, Input
from textual.containers import HorizontalGroup, VerticalGroup
from datetime import datetime

class Tela(App):

    CSS_PATH = "Tela.tcss"

    dinheiro = 0

    def compose(self):
        with HorizontalGroup(id="container"):
            with VerticalGroup():
                yield Static(f"{datetime.now().time():%T}", id="relogio")
                yield Button("Atualizar relógio", id="bt_relogio")
            with VerticalGroup():
                yield Static(f"Saldo: ${self.dinheiro}", id="stc_dinheiro")
                yield Button("Fique rico", id="bt_dinheiro")
            with VerticalGroup():
                yield Static()
                yield Input()
                yield Button("Enviar")

    def atualiza_relogio(self):
        relogio = datetime.now().time()
        self.query_one("#relogio", Static).update(f"{relogio:%T}")

    def on_button_pressed(self, evento: Button.Pressed):
        match evento.button.id:
            case  "bt_dinheiro":
                match self.dinheiro:
                    case self.dinheiro if self.dinheiro < 500:
                        self.dinheiro += 50
                    case self.dinheiro if self.dinheiro < 1001:
                        self.dinheiro += 100
                    case self.dinheiro if self.dinheiro < 2001:
                        self.dinheiro += 1000
                        self.query_one("#stc_dinheiro", Static).update(f"Saldo: ${self.dinheiro}\n\n 🚲")
                        return
                    case self.dinheiro if self.dinheiro < 30001:
                        self.dinheiro += 10000
                        self.query_one("#stc_dinheiro", Static).update(f"Saldo: ${self.dinheiro}\n\n 🚗")
                        return
                    case self.dinheiro if self.dinheiro < 1000001:
                        self.dinheiro += 10000
                        self.query_one("#stc_dinheiro", Static).update(f"Saldo: ${self.dinheiro}\n\n 🏠")
                        return
                self.query_one("#stc_dinheiro", Static).update(f"Saldo: ${self.dinheiro}")
            case "bt_relogio":
                self.atualiza_relogio()


if __name__ == "__main__":
    app = Tela()
    app.run()