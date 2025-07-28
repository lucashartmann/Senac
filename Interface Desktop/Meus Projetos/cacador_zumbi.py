from textual.app import App
from textual.widgets import Label
from textual.containers import HorizontalGroup
from textual.events import Key


class Teste(App):
    
    CSS = '''
       #container_cacador{
           align: right middle;
           background: rgb(100,100,100);
           height: 100;
       }
       #container_zumbi {
           align: left middle;
            background: rgb(200,200,200);
            height: 100;
       }
       #cacador {
           align: left middle;
       }
       #zumbi {
           align: right middle;
       }
    '''

    def compose(self):
        with HorizontalGroup():
            with HorizontalGroup(id="container_cacador"):
                yield Label("👨‍✈️", id="cacador")
            with HorizontalGroup(id="container_zumbi"):
                yield Label("🧟", id="zumbi")
                

    cont_cacador_left = 0
    cont_cacador_right = 0
    cont_cacador_up = 0
    cont_cacador_down = 0

    cont_zumbi_left = 0
    cont_zumbi_right = 0
    cont_zumbi_up = 0
    cont_zumbi_down = 0

    def _on_key(self, evento: Key):
        match evento.key:
            case "w":
                lbl = self.query_one("#zumbi")
                if self.cont_zumbi_down > 0:
                    self.cont_zumbi_down -= 1
                    lbl.styles.margin = (
                        self.cont_zumbi_down, self.cont_zumbi_left, self.cont_zumbi_up, self.cont_zumbi_right)
                else:
                    self.cont_zumbi_up += 1
                    lbl.styles.margin = (
                        self.cont_zumbi_down, self.cont_zumbi_left, self.cont_zumbi_up, self.cont_zumbi_right)
            case "s":
                lbl = self.query_one("#zumbi")
                if self.cont_zumbi_up > 0:
                    self.cont_zumbi_up -= 1
                    lbl.styles.margin = (
                        self.cont_zumbi_down, self.cont_zumbi_left, self.cont_zumbi_up, self.cont_zumbi_right)
                else:
                    self.cont_zumbi_down += 1
                    lbl.styles.margin = (
                        self.cont_zumbi_down, self.cont_zumbi_left, self.cont_zumbi_up, self.cont_zumbi_right)
            case "a":
                lbl = self.query_one("#zumbi")
                if self.cont_zumbi_right > 0:
                    self.cont_zumbi_right -= 1
                    lbl.styles.margin = (
                        self.cont_zumbi_down, self.cont_zumbi_left, self.cont_zumbi_up, self.cont_zumbi_right)
                else:
                    self.cont_zumbi_left += 1
                    lbl.styles.margin = (
                        self.cont_zumbi_down, self.cont_zumbi_left, self.cont_zumbi_up, self.cont_zumbi_right)
            case "d":
                lbl = self.query_one("#zumbi")
                if self.cont_zumbi_left > 0:
                    self.cont_zumbi_left -= 1
                    lbl.styles.margin = (
                        self.cont_zumbi_down, self.cont_zumbi_left, self.cont_zumbi_up, self.cont_zumbi_right)
                else:
                    self.cont_zumbi_right += 1
                    lbl.styles.margin = (
                        self.cont_zumbi_down, self.cont_zumbi_left, self.cont_zumbi_up, self.cont_zumbi_right)
                    
                    
            case "left":
                lbl = self.query_one("#cacador")
                if self.cont_cacador_right > 0:
                    self.cont_cacador_right -= 1
                    lbl.styles.margin = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
                else:
                    self.cont_cacador_left += 1
                    lbl.styles.margin = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
            case "right":
                lbl = self.query_one("#cacador")
                if self.cont_cacador_left > 0:
                    self.cont_cacador_left -= 1
                    lbl.styles.margin = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
                else:
                    self.cont_cacador_right += 1
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
    Teste().run()