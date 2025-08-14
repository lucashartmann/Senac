from textual.widgets import (
    Header, Footer, Label, Input, Static, Select
)
from textual.screen import Screen
from textual.binding import Binding
from models import JOGADOR, Item


class TelaNovoJogador(Screen):

    CSS = '''
    Static {
        content-align: center middle;
        color: cyan;
        padding: 1;
    }
'''
    BINDINGS = [
        Binding("ctrl+s", "salvar", "Salvar"),
        Binding("ctrl+n", "novo_item", "Novo Item")
    ]

    def compose(self):
        yield Header()
        yield Static("𝕹𝖔𝖛𝖔 𝕵𝖔𝖌𝖆𝖉𝖔𝖗")
        yield Label("Nome")
        yield Input(id="tx_nome")
        yield Label("Classe")
        yield Select([
            ("Mago", "mago"),
            ("Cavaleiro", "cavaleiro"),
            ("Assassina", "assassina")], id="sl_classe")
        yield Static(f"Item equipado: {JOGADOR.item_equipado.get_nome()}", id="stt_item_equipado")
        yield Footer()

    def action_novo_item(self):
        # Atualiza Model
        JOGADOR.item_equipado = Item.Item()
        # Atualiza View
        stt_item = self.query_one("#stt_item_equipado", Static)
        stt_item.update(
            f"Item equipado: {JOGADOR.item_equipado.get_nome()}")

    def action_salvar(self):
        nome = self.query_one("#tx_nome", Input).value
        classe = self.query_one("#sl_classe", Select).value
        # Atualizamos a model
        JOGADOR.nome = nome
        JOGADOR.classe = classe
        self.notify("Jogador salvo")
