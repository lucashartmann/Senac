import shelve
from models import Init


class Cofre:

    def salvar_jogador():
        with shelve.open("data/jogador.db") as db:
            db["jogador"] = Init.JOGADOR
