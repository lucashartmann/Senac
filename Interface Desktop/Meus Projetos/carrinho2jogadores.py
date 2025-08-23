from textual.app import App
from textual.widgets import Label
from textual.events import Key
from asyncio import sleep
from textual import work


class Teste(App):

    CSS = '''
        #carrinho {
            align: center middle;
        }
        #carrinho2 {
            align: center middle;
        }
        #txa_caminho {
            height: 5;
            width: 100;
        }
    '''

    caminho = '''
    
    🚦--🌳---------🌳----🌳---🌳-🌳--🌳-----'''

    relogio = 0

    @work
    async def espera(self):
        await sleep(5)
        self.caminho = self.caminho.replace("🚦", "🟢 ")
        self.desenhar_caminho()

    def compose(self):
        yield Label("🚗", id="carrinho")
        yield Label(id="txa_caminho")
        yield Label("🏎️", id="carrinho2")

    def on_mount(self):
        self.desenhar_caminho()
        self.espera()

    def desenhar_caminho(self):
        self.query_one("#txa_caminho", Label).update(self.caminho)

    cont_carrinho_left = 0
    cont_carrinho_right = 0

    cont_carrinho2_left = 0
    cont_carrinho2_right = 0

    pode_andar = True
    mostrou_bandeira = False

    def resultado(self):
        if self.cont_carrinho_right == 66:
            self.notify(f'Carro ganhou!')
        else:
            self.notify(f'Fórmula 1 ganhou!')

    def _on_key(self, evento: Key):

        right_antigo = 0

        if self.cont_carrinho2_right > right_antigo or self.cont_carrinho_right > right_antigo:
            right_antigo += 1
            if self.cont_carrinho_right == 15 or self.cont_carrinho2_right == 15 and not self.mostrou_bandeira:
                self.mostrou_bandeira = True
                self.caminho += "🏁"
            if self.cont_carrinho_right == 66 or self.cont_carrinho2_right == 66:
                self.pode_andar = False
                self.resultado()
            if self.caminho[-1] != "🏁":
                if self.caminho[-1] == "🌳":
                    self.caminho += "-"
                else:
                    self.caminho += "🌳"
            self.desenhar_caminho()

        if "🟢 " in self.caminho and self.pode_andar:
            match evento.key:
                case "a":
                    lbl = self.query_one("#carrinho2")
                    if self.cont_carrinho2_right > 0:
                        self.cont_carrinho2_right -= 1
                        lbl.styles.margin = (
                            0, self.cont_carrinho2_left, 0, self.cont_carrinho2_right)
                    else:
                        self.cont_carrinho2_left += 1
                        lbl.styles.margin = (
                            0, self.cont_carrinho2_left, 0, self.cont_carrinho2_right)
                case "d":
                    lbl = self.query_one("#carrinho2")
                    if self.cont_carrinho2_left > 0:
                        self.cont_carrinho2_left -= 1
                        lbl.styles.margin = (
                            0, self.cont_carrinho2_left, 0, self.cont_carrinho2_right)
                    else:
                        self.cont_carrinho2_right += 1
                        lbl.styles.margin = (
                            0, self.cont_carrinho2_left, 0, self.cont_carrinho2_right)
                case "left":
                    lbl = self.query_one("#carrinho")
                    if self.cont_carrinho_right > 0:
                        self.cont_carrinho_right -= 1
                        lbl.styles.margin = (
                            0, self.cont_carrinho_left, 0, self.cont_carrinho_right)
                    else:
                        self.cont_carrinho_left += 1
                        lbl.styles.margin = (
                            0, self.cont_carrinho_left, 0, self.cont_carrinho_right)
                case "right":
                    lbl = self.query_one("#carrinho")
                    if self.cont_carrinho_left > 0:
                        self.cont_carrinho_left -= 1
                        lbl.styles.margin = (
                            0, self.cont_carrinho_left, 0, self.cont_carrinho_right)
                    else:
                        self.cont_carrinho_right += 1
                        lbl.styles.margin = (
                            0, self.cont_carrinho_left, 0, self.cont_carrinho_right)


if __name__ == "__main__":
    Teste().run()
