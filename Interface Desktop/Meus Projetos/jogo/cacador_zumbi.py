from textual.app import App
from textual.widgets import Label, Static
from textual.containers import HorizontalGroup
from textual.events import Key
from asyncio import sleep
from textual import work


class Jogo(App):

    CSS_PATH = "cacador_zumbi.tcss"

    def compose(self):
        # Cada sala pode ter itens diferentes
        with HorizontalGroup():
            yield Label("🗝️", id="chave")
            yield Label("🧟", id="zumbi")
            yield Label("🚪", id="porta")
        yield Label("👮", id="cacador")

    cont_cacador_left = 0
    cont_cacador_right = 0
    cont_cacador_up = 0
    cont_cacador_down = 0
    zumbi_morto = False
    pode_movimentar = True

    # padding = (top (vai para baixo), right (vai para a esquerda), bottom (vai para cima), left (vai para a direita))

    def movimentacao(self, evento):
        lbl = self.query_one("#cacador")

        match evento.key:
            case "left":
                if self.cont_cacador_right > 0:
                    self.cont_cacador_right -= 1
                    lbl.styles.padding = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
                else:
                    self.cont_zumbi_right += 1
                    lbl.styles.padding = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)

            case "right":
                if self.cont_cacador_left > 0:
                    self.cont_cacador_left -= 1
                    lbl.styles.padding = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
                else:
                    self.cont_cacador_right += 1
                    lbl.styles.padding = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)

            case "up":

                if self.cont_cacador_down > 0:
                    self.cont_cacador_down -= 1
                    lbl.styles.padding = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
                else:
                    self.cont_cacador_up += 1
                    lbl.styles.padding = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)

            case "down":
                if self.cont_cacador_up > 0:
                    self.cont_cacador_up -= 1
                    lbl.styles.padding = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)
                else:
                    self.cont_cacador_down += 1

                    lbl.styles.padding = (
                        self.cont_cacador_down, self.cont_cacador_left, self.cont_cacador_up, self.cont_cacador_right)

    @work
    async def combate(self):
        # Fazer a classe do personagem com vida e dano. Implementar o dano da arma equipada e etc.
        self.notify("Dano 5 no zumbi")
        await sleep(2)
        self.notify("Dano 5 no caçador")
        await sleep(2)
        self.notify("Dano 5 no zumbi")
        await sleep(2)
        self.notify("Zumbi morreu")
        await self.query("#zumbi").remove()
        self.pode_movimentar = True
        self.zumbi_morto = True

    @work
    async def _on_key(self, evento: Key):
        if self.pode_movimentar:
            self.movimentacao(evento)

        if self.cont_cacador_up == 0 and self.cont_cacador_right == 62 and self.cont_cacador_down == 0 and self.cont_cacador_left == 0:
            # self.notify("Clique Up para iniciar combate")
            # if evento.key == "up": self.combate()
            self.pode_movimentar = False
            self.notify("Zumbi encontrado")
            await sleep(2)
            self.combate()

        if self.zumbi_morto == False:
            if self.cont_cacador_up == 0 and self.cont_cacador_right == 114 and self.cont_cacador_down == 0 and self.cont_cacador_left == 0:
                # self.notify("Clique Up para entrar na porta")
                # Depois que entrar na porta muda de sala (switch screen)
                # Precisa ter a chave equipada para abrir a porta
                self.notify("Porta encontrada")
        else:
            if self.cont_cacador_up == 0 and self.cont_cacador_right == 72 and self.cont_cacador_down == 0 and self.cont_cacador_left == 0:
                self.notify("Porta encontrada")

        if self.cont_cacador_up == 0 and self.cont_cacador_right == 20 and self.cont_cacador_down == 0 and self.cont_cacador_left == 0:
            # pega a chave, adiciona ela ao personagem e remove ela da tela
            self.notify("Chave encontrado")


if __name__ == "__main__":
    Jogo().run()
