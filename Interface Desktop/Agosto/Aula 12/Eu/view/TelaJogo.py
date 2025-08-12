from textual.widgets import Header, Footer, Static, TextArea
from textual.screen import Screen
from textual.binding import Binding
from models import Cena


class TelaJogo(Screen):

    CSS_PATH = "css/TelaJogo.tcss"
    SUB_TITLE = ""

    BINDINGS = [
        Binding("up", "anda('norte')", "Norte"),
        Binding("down", "anda('sul')", "Sul"),
        Binding("right", "anda('leste')", "Leste"),
        Binding("left", "anda('oeste')", "Oeste"),
        Binding("c", "inventario", "Inventário")
    ]

    inventario_aberto = False

    def compose(self):
        yield Header()
        yield Static(f'Jogador: {Cena.JOGADOR.nome}', id="stt_jogador")
        yield Static(f'Cena: {Cena.CENA_ATUAL.nome}', id="stt_cena_atual")
        yield Static(f"Items da sala: {"\n".join(item for item in Cena.CENA_ATUAL.itens.keys())}", id="stt_items_cena") # Arrumar depois, pegar do controller
        yield Footer()

    def action_anda(self, direcao):
        match direcao:
            case "norte" if Cena.CENA_ATUAL.norte:
                Cena.CENA_ATUAL = Cena.CENA_ATUAL.norte
            case "sul" if Cena.CENA_ATUAL.sul:
                Cena.CENA_ATUAL = Cena.CENA_ATUAL.sul
            case "leste" if Cena.CENA_ATUAL.leste:
                Cena.CENA_ATUAL = Cena.CENA_ATUAL.leste
            case "oeste" if Cena.CENA_ATUAL.oeste:
                Cena.CENA_ATUAL = Cena.CENA_ATUAL.oeste
        self.on_screen_resume()

    def action_inventario(self):
        if self.inventario_aberto:
            self.query_one("#tx_inventario", TextArea).remove()
            self.inventario_aberto = False
        else:
            self.mount(TextArea(f"".join(item for item in Cena.JOGADOR.inventario.keys()), id="tx_inventario", disabled=True))
            self.inventario_aberto = True

    def on_screen_resume(self):
        stt_jogador = self.query_one("#stt_jogador", Static)
        stt_cena_atual = self.query_one("#stt_cena_atual", Static)
        stt_items = self.query_one("#stt_items_cena", Static)

        stt_items.update(f"Items da sala: {"\n".join(item for item in Cena.CENA_ATUAL.itens.keys())}")
        stt_jogador.update(f'Jogador: {Cena.JOGADOR.nome}')
        stt_cena_atual.update(f'Cena: {Cena.CENA_ATUAL.nome}')
