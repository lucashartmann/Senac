from textual.app import ComposeResult
from textual.widgets import (
    Header, Footer, Static,
)
from textual.screen import Screen
from textual.containers import VerticalGroup
from models import JOGADOR


class TelaInicial(Screen):

    CSS = """
    #game_title {
        color: magenta;
    }

    Static {
        content-align: center middle;        
        color: cyan;        
    }

    VerticalGroup {
        align: center middle;
        height: 100%;
    }
"""

    def compose(self) -> ComposeResult:
        yield Header()

        yield VerticalGroup(
            Static("𝕯𝖊𝖘𝕶 𝕯𝖚𝖓𝖌𝖊𝖔𝖓", id="game_title"),
            Static(),
            Static("𝓾𝓶 𝓭𝓾𝓷𝓰𝓮𝓸𝓷 𝓬𝓻𝓪𝔀𝓵𝓮𝓻"),
            Static("𝓮𝓶 𝓶𝓸𝓭𝓸 𝓽𝓮𝔁𝓽𝓸")
        )
        yield Footer()

    def on_screen_resume(self):
        if not JOGADOR.nome == "sem nome":
            self.sub_title = f"({JOGADOR.nome})"
