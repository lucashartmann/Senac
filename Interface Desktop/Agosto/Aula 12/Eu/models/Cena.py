from models import Item, Jogador


class Cena():
    def __init__(self, nome="Indefinida"):
        self.nome = nome
        self.itens = dict()
        self.norte = None
        self.sul = None
        self.leste = None
        self.oeste = None


# MAPA DO JOGO
hall = Cena("Hall")
sala = Cena("Sala")
calabouco1 = Cena("Calabouço 1")

item1 = Item.Item()
calabouco1.itens[item1.get_nome()] = item1

item2 = Item.Item()
calabouco1.itens[item2.get_nome()] = item2

cela1 = Cena("Cela 1")
calabouco2 = Cena("Calabouço 2")
cela2 = Cena("Cela 2")
patio = Cena("Patio")

# Conectamos as CENAS

hall.leste = sala

sala.sul = calabouco1
sala.oeste = hall

calabouco1.leste = cela1
calabouco1.norte = sala
calabouco1.sul = calabouco2

cela1.oeste = calabouco1
cela1.sul = cela2

calabouco2.norte = calabouco1
calabouco2.leste = cela2

cela2.norte = cela1
cela2.oeste = calabouco2
cela2.leste = patio

patio.oeste = cela2


# ESTADO DO JOGO
JOGADOR = Jogador.Jogador()
CENA_ATUAL = hall
