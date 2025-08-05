from textual.app import App
from textual.widgets import Label, Static, Footer, TextArea
from textual.containers import HorizontalGroup
from textual.events import Key
from asyncio import sleep
from textual import work
from models.Personagem import Personagem
from textual.screen import Screen
from textual.binding import Binding
from view.TelaLoja import TelaLoja, Loja
from models.Item import Item
from models.Cena import Cena

class TelaInicial(Screen):
    CSS_PATH = "css/TelaInicial.tcss"
    
    sala_inicial = Cena("Sala Inicial")

    
    cacador = Personagem()
    cacador.sala = sala_inicial

    
    chave = Item()
    chave.set_nome("chave")
    chave.set_categoria("item_comum")
    chave.set_icon("🗝️")
    chave.set_dano(0)
    chave.set_protecao(0)
    chave.set_genero_objeto("feminino")
    chave.set_quant(1)
    
    sala_inicial.colocar_item(chave)
    
    espada = Item()
    espada.set_nome("espada")
    espada.set_categoria("arma")
    espada.set_icon("🗡️")
    espada.set_dano(5)
    espada.set_protecao(0)
    espada.set_genero_objeto("feminino")
    espada.set_quant(1)
    
    sala_inicial.colocar_item(espada)
    
    cacador_margin = [0, 0, 0, 0]  


    def compose(self):
        with HorizontalGroup():
            yield Label(self.chave.get_icon(), id=f"{self.chave.get_nome()}")
            yield Label("🧟", id="zumbi")
            yield Label("🚪", id="porta")
            yield Label(self.espada.get_icon(), id=f"{self.espada.get_nome()}")
        yield Label("👮", id="cacador")
        yield Footer(show_command_palette=False)

    zumbi_morto = False
    pode_movimentar = True
    pode_agir = False
    objeto_iteracao = ""
    

    # padding = (top (vai para baixo), right (vai para a esquerda), bottom (vai para cima), left (vai para a direita))


    def abrir_inventario(self):
        inventario = "Inventário: ".join(
            str(nome, item) for nome, item in self.cacador.inventario.items())
        self.mount(TextArea(inventario))

    @work
    async def acoes(self, evento):
        match evento.key:
            case "z":
                if self.objeto_iteracao != "":
                    self.pode_movimentar = False
                    match self.objeto_iteracao:
                        case "zumbi":
                            if self.cacador.item_equipado.get_categoria() == "arma":
                                await sleep(2)
                                self.notify("Entrando em combate com o zumbi")
                                self.combate()
                            else:
                                self.notify("Você precisa de uma arma para iniciar o combate")
                        case "porta":
                            if self.cacador.item_equipado:
                                if self.cacador.item_equipado.get_nome() == "chave":
                                    self.app.switch_screen("tela_loja")
                                else:
                                    self.notify("Você precisa da chave para abrir a porta")
                            else:
                                self.notify("Você precisa de um item equipado para abrir a porta")
                        case "chave" | "espada":
                            if self.pode_agir:
                                self.notify(f"{self.objeto_iteracao.capitalize()} coletada")
                                self.cacador.coletar_item(self.objeto_iteracao)
                                self.query_one(f"#{self.objeto_iteracao}").remove()
                    self.pode_movimentar = True
            case "x":
                if self.cacador.inventario:
                    contador = 0
                    lista_items = list(self.cacador.inventario.keys())
                    self.cacador.equipar_item(lista_items[contador])
                    self.notify(f"Item equipado: {self.cacador.item_equipado}")
                    contador += 1
                    if contador == len(lista_items):
                        contador = 0
                else:
                    self.notify("Inventário vazio")
            case "c":
                self.abrir_inventario()

    @work
    async def combate(self):
        # Fazer a classe do personagem com vida e dano. Implementar o dano da arma equipada e etc.
        self.notify(f"Dano {self.cacador.item_equipado.get_dano()} no zumbi")
        await sleep(2)
        self.notify("Dano 5 no caçador")
        await sleep(2)
        self.notify(f"Dano {self.cacador.item_equipado.get_dano()} no zumbi")
        await sleep(2)
        self.notify("Zumbi morreu")
        await self.query("#zumbi").remove()
        self.pode_movimentar = True
        self.zumbi_morto = True
        

    @work
    async def _on_key(self, evento: Key):
        self.objeto_iteracao = ""
        self.pode_agir = False
        lbl = self.query_one("#cacador")
        self.acoes(evento)
    
        if self.pode_movimentar:
            self.screen.app.movimentacao(evento, lbl, self.cacador_margin)
        
        if "chave" not in self.cacador.inventario:
            if self.cacador_margin == [0, 0, 0, 62]:
                self.notify("Zumbi encontrado")    
                self.pode_agir = True   
                self.objeto_iteracao = "zumbi"
        else:
            if self.cacador_margin == [0, 0, 0, 41]:
                self.notify("Zumbi encontrado")    
                self.pode_agir = True   
                self.objeto_iteracao = "zumbi"
      
        if self.zumbi_morto == False and "chave" not in self.cacador.inventario:
            if self.cacador_margin == [0, 0, 0, 114]:
                self.objeto_iteracao = "porta"
                self.pode_agir = True
                self.notify("Porta encontrada")                   
        elif self.zumbi_morto == True:
            if self.cacador_margin == [0, 0, 0, 72]:
                self.objeto_iteracao = "porta"
                self.pode_agir = True
                self.notify("Porta encontrada")
        elif "chave" in self.cacador.inventario:
            if self.cacador_margin == [0, 0, 0, 92]:
                self.objeto_iteracao = "porta"
                self.pode_agir = True
                self.notify("Porta encontrada")
                
        for lbl in self.query("Label"):
            if lbl.id == "chave":
                if self.cacador_margin == [0, 0, 0, 20]:
                    self.objeto_iteracao = "chave"
                    self.pode_agir = True
                    self.notify("Chave encontrada")
            
        for lbl in self.query("Label"):
            if lbl.id == "espada":
                if "chave" not in self.cacador.inventario:
                    if self.cacador_margin == [0, 0, 0, 142]:
                        self.notify("Espada encontrada")
                        self.pode_agir = True
                        self.objeto_iteracao = "espada"
                else:
                    if self.cacador_margin == [0, 0, 0, 123]:
                        self.notify("Espada encontrada")
                        self.pode_agir = True
                        self.objeto_iteracao = "espada"


class Jogo(App):
    
    BINDINGS = [
        Binding("z", "a1", "Interagir"),
        Binding("left", "a2", "Andar para a esquerda"),
        Binding("right", "a3", "Andar para a direita"),
        Binding("up", "a4", "Andar para cima"),
        Binding("down", "a5", "Andar para baixo"),
        Binding("c", "a6", "Abrir inventário"),
        Binding("x", "a7", "Equipar item"),
    ]
    
    def movimentacao(self, evento, label, cacador_margin):

        match evento.key:
            case "left":
                if cacador_margin[3] > 0:
                    cacador_margin[3] -= 1
                else:
                    cacador_margin[1] += 1
            case "right":
                if cacador_margin[1] > 0:
                    cacador_margin[1] -= 1
                else:
                    cacador_margin[3] += 1
                
            case "up":
                if cacador_margin[0] > 0:
                    cacador_margin[0] -= 1
                else:
                    cacador_margin[2] += 1

            case "down":
                if cacador_margin[2] > 0:
                    cacador_margin[2] -= 1
                else:
                    cacador_margin[0] += 1
            case _:
               return 
           
        label.styles.padding = (
                        cacador_margin[0], cacador_margin[1], cacador_margin[2], cacador_margin[3])
    
    SCREENS = {
        "tela_inicial": TelaInicial,
        "tela_loja": TelaLoja,
        "loja": Loja
    }
          
    def on_mount(self):
        self.push_screen("tela_inicial")