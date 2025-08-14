from textual.widgets import (
    Header, Footer, Static,
)
from textual.screen import Screen
from textual.binding import Binding
from models import CENA_ATUAL, JOGADOR


class TelaJogo(Screen):

    CSS = """"""
    SUB_TITLE = ""

    BINDINGS = [
        Binding("up", "norte", "Norte"),
        Binding("down", "sul", "Sul"),
        Binding("right", "leste", "Leste"),
        Binding("left", "oeste", "Oeste"),
    ]

    def compose(self):
        yield Header()
        yield Static(f'Jogador: {JOGADOR.nome}', id="stt_nome_jogador")
        yield Static(f'Cena: {CENA_ATUAL.nome}', id="stt_nome_cena_atual")
        yield Footer()

    def on_screen_resume(self):
        stt_nome_jogador = self.query_one("#stt_nome_jogador", Static)
        stt_nome_cena_atual = self.query_one("#stt_nome_cena_atual", Static)

        stt_nome_jogador.update(f'Jogador: {JOGADOR.nome}')
        stt_nome_cena_atual.update(f'Cena: {CENA_ATUAL.nome}')

    def action_norte(self):
        if CENA_ATUAL.norte:
            CENA_ATUAL = CENA_ATUAL.norte

    def action_sul(self):
        if CENA_ATUAL.sul:
            CENA_ATUAL = CENA_ATUAL.sul

    def action_leste(self):
        if CENA_ATUAL.leste:
            CENA_ATUAL = CENA_ATUAL.leste

    def action_oeste(self):
        if CENA_ATUAL.oeste:
            CENA_ATUAL = CENA_ATUAL.oeste
