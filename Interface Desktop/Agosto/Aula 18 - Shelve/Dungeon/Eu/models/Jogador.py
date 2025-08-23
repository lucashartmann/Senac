class Jogador():
    def __init__(self):
        self.inventario = dict()
        self.item_equipado = None
        self.vida = 0
        self.xp = 0
        self.classe = ""
        self.mana = 0
        self.stamina = 0
        self.nome = "sem nome"

    def __str__(self):
        return (
            f"Jogador: {self.nome}\n"
            f"Classe: {self.classe}\n"
            f"Vida: {self.vida}\n"
            f"XP: {self.xp}\n"
            f"Mana: {self.mana}\n"
            f"Stamina: {self.stamina}\n"
            f"Item Equipado: {self.item_equipado}\n"
            f"Inventário: {list(self.inventario.keys())}"
        )
