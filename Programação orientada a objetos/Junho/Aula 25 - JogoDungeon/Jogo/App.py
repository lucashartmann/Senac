from models.Cena import Cena
from models.Personagem import Mago
from models.Personagem import Guerreiro
from models.Personagem import Personagem
from models.Item import Item
from textual.app import App, ComposeResult
from textual.widgets import Input, Button, TextArea

# python App.py

hall = Cena("Hall")
sala = Cena("Sala")
calabouco1 = Cena("Calabouço 1")
cela1 = Cena("Cela 1")
calabouco2 = Cena("Calabouço 2")
cela2 = Cena("Cela 2")
patio = Cena("Patio")
heroi = Mago()

heroi.sala = hall

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


hall.colocar_item(Item())
sala.colocar_item(Item())
calabouco1.colocar_item(Item())
cela1.colocar_item(Item())
calabouco2.colocar_item(Item())
cela2.colocar_item(Item())
patio.colocar_item(Item())


comando = str()
print(heroi)

while comando != "sair":
    comando = input(": ").split()
    print(heroi)

    match comando:
        
        case ["sair"]:
            exit(0)
            
        case ["andar", direcao]:
            match direcao:
                case 'norte':
                    heroi.andar_norte()
                case 'sul':
                    heroi.andar_sul()
                case 'leste':
                    heroi.andar_leste()
                case 'oeste':
                    heroi.andar_oeste()
        case ["coletar", nome_item]:
            heroi.coletar_item(nome_item)
        case ["soltar", nome_item]:
            heroi.soltar_item(nome_item)
        case ["equipar", nome_item]:
            heroi.equipar_item(nome_item)
        case ["atacar"]:
            heroi.atacar()
