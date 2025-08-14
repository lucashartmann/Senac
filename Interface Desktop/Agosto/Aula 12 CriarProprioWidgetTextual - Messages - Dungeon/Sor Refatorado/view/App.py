from textual.app import App
from textual.binding import Binding
from view import (TelaInicial, TelaNovoJogador, TelaJogo)


class DeskDungeon(App):
    TITLE = "Desk Dungeon"
    SUB_TITLE = "um dungeon crawler modo texto"
    SCREENS = {
        "inicial": TelaInicial.TelaInicial,
        "novo_jogador": TelaNovoJogador.TelaNovoJogador,
        "tela_jogo": TelaJogo.TelaJogo,
    }

    BINDINGS = [
        Binding("n", "novo_jogador", "Novo Jogador"),
        Binding("j", "tela_jogo", "Jogo"),
        Binding("escape", "tela_inicial", "Início"),
    ]

    def on_mount(self):
        self.push_screen("inicial")

    def action_tela_jogo(self):
        self.switch_screen("tela_jogo")

    def action_tela_inicial(self):
        self.switch_screen("inicial")

    def action_novo_jogador(self):
        self.switch_screen("novo_jogador")
