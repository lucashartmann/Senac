from models.Cena import Cena
from models.Personagem import Mago
from models.Personagem import Guerreiro
from models.Personagem import Personagem
from models.Item import Item
from textual.app import App, ComposeResult
from textual.widgets import Input, Button, TextArea

# python App2.py

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

# python App2.py

class DungeonApp(App):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "enviar":
            comando = self.query_one("#tx_comando", Input).value
            comando = comando.split()
            match comando:
                case ["sair"]:
                    self.exit()
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

                case [outro_comando]:
                    self.query_one("#mensagem", TextArea).text = f"Comando não reconhecido: {outro_comando}"
                    return

        self.query_one("#mensagem", TextArea).text = heroi.__str__()

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Digite um comando", id="tx_comando")
        yield Button("Enviar", id="enviar")
        yield TextArea(id="mensagem")

DungeonApp().run()