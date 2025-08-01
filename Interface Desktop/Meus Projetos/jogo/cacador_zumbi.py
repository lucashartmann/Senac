from textual.app import App
from textual.widgets import Label, Static
from textual.containers import HorizontalGroup
from textual.events import Key


class Jogo(App):

    CSS_PATH = "cacador_zumbi.tcss"

    def compose(self):
        with HorizontalGroup(id="container"):
            yield Label("🗝️", id="chave")
            yield Label("👮", id="cacador")
            yield Label("🧟", id="zumbi")
            yield Label("🚪", id="porta")
            

    cont_cacador_left = 0
    cont_cacador_right = 10
    cont_cacador_up = 0
    cont_cacador_down = 8

    cont_porta_left = 0
    cont_porta_right = 10
    cont_porta_up = 0
    cont_porta_down = 0

    cont_zumbi_left = 0
    cont_zumbi_right = 10
    cont_zumbi_up = 0
    cont_zumbi_down = 5

    # margin = (top (vai para baixo), right (vai para a esquerda), bottom (vai para cima), left (vai para a direita))

    def _on_key(self, evento: Key):
        match evento.key:

            case "left":
                lbl = self.query_one("#cacador")
                lbl_zumbi = self.query_one("#zumbi")
                lbl_porta = self.query_one("#porta")

                if self.cont_cacador_right > 0:
                    self.cont_cacador_right -= 1

                    lbl.styles.margin = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
                else:
                    self.cont_zumbi_right += 1
                    self.cont_porta_right += 1

                    lbl_zumbi.styles.margin = (self.cont_zumbi_down, self.cont_zumbi_left, self.cont_zumbi_up, self.cont_zumbi_right)

                    lbl_porta.styles.margin = (self.cont_porta_down, self.cont_porta_left, self.cont_porta_up, self.cont_porta_right)

                    self.cont_cacador_left += 1

                    lbl.styles.margin = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
                    
            case "right":
                lbl = self.query_one("#cacador")
                lbl_zumbi = self.query_one("#zumbi")
                lbl_porta = self.query_one("#porta")

                if self.cont_cacador_left > 0:
                    self.cont_cacador_left -= 1
                    lbl.styles.margin = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
                else:
                    self.cont_zumbi_right -= 1
                    self.cont_porta_right -= 1
                    self.cont_cacador_right += 1
                    lbl_zumbi.styles.margin = (self.cont_zumbi_down, self.cont_zumbi_left, self.cont_zumbi_up, self.cont_zumbi_right)
                    lbl_porta.styles.margin = (self.cont_porta_down, self.cont_porta_left, self.cont_porta_up, self.cont_porta_right)
                    lbl.styles.margin = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
                    
            case "up":
                lbl = self.query_one("#cacador")
                if self.cont_cacador_down > 0:
                    self.cont_cacador_down -= 1
                    lbl.styles.margin = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
                else:
                    self.cont_cacador_up += 1
                    lbl.styles.margin = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
            case "down":
                lbl = self.query_one("#cacador")
                if self.cont_cacador_up > 0:
                    self.cont_cacador_up -= 1
                    lbl.styles.margin = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
                else:
                    self.cont_cacador_down += 1
                    lbl.styles.margin = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)


if __name__ == "__main__":
    Jogo().run()
