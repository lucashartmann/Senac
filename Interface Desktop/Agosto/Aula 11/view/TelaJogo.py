from textual.widgets import Header, Footer, Static
from textual.screen import Screen
from textual.binding import Binding
from models import Cena


class TelaJogo(Screen):

    CSS_PATH = "css/TelaJogo.tcss"
    SUB_TITLE = ""

    BINDINGS = [
        Binding("up","norte", "Norte"),
        Binding("down","sul", "Sul"),
        Binding("right","leste", "Leste"),
        Binding("left","oeste", "Oeste"),        
    ]

    def action_norte(self):
        pass

    def action_sul(self):
        pass

    def action_leste(self):
        pass

    def action_oeste(self):
        pass

    def compose(self):
        yield Header()
        yield Static(f'Jogador: {Cena.JOGADOR.nome}', id="stt_nome_jogador")
        yield Static(f'Cena: {Cena.CENA_ATUAL.nome}', id="stt_nome_cena_atual")
        yield Footer()

    def on_screen_resume(self):
        stt_nome_jogador = self.query_one("#stt_nome_jogador",Static)
        stt_nome_cena_atual = self.query_one("#stt_nome_cena_atual",Static)
        
        stt_nome_jogador.update(f'Jogador: {Cena.JOGADOR.nome}')
        stt_nome_cena_atual.update(f'Cena: {Cena.CENA_ATUAL.nome}')