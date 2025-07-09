from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Footer, Header, TextArea, Label, Input
from controller.ControllerCMD import ControllerCMD
from textual.screen import Screen
from textual.events import Focus

class InputEvento(Input):
    def on_focus(self, event: Focus) -> None:
        self.value = ""
        
    def _on_blur(self, event):
        if not self.value:
            self.value = "Veiculo"  
        
class InputEventoTrem(Input):
    def on_focus(self, event: Focus) -> None:
        self.value = ""
        
    def _on_blur(self, event):
        if not self.value:
            self.value = "Trem"

class TelaTrem(Screen):
    CSS_PATH = "../css/Telas.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "engatar":
            idTrem = int(self.query_one("#input_trem_veiculo", Input).value)
            idVeiculo = int(self.query_one("#input_trem", Input).value)
            areaTexto = self.query_one("#textArea_engatar", TextArea)
            engatar = ControllerCMD.engatar(idTrem, idVeiculo)
            areaTexto.text = engatar
            self.on_mount()
            
        if event.button.id == "desengatar":
            idTrem = int(self.query_one("#input_trem_veiculo", Input).value)
            idVeiculo = int(self.query_one("#input_trem", Input).value)
            areaTexto = self.query_one("#textArea_engatar", TextArea)
            desengatar = ControllerCMD.desengatar(idTrem, idVeiculo)
            areaTexto.text = desengatar
            self.on_mount()
            
        if event.button.id == "cadastrar":
            cadastrar = ControllerCMD.adicionar_trem()
            areaTexto = self.query_one("#textArea_engatar", TextArea)
            areaTexto.text = cadastrar
            self.on_mount()

        if event.button.id == "trocar_tela":
            self.app.pop_screen()

    def definir_locomotivas(self):
        lista_locomotivas = ControllerCMD.listar_locomotivas_garagem()
        areaLocomotivas = self.query_one(
            "#textArea_trem_locomotivas", TextArea)
        areaLocomotivas.text = lista_locomotivas

    def definir_vagoes(self):
        lista_vagoes = ControllerCMD.listar_vagoes_garagem()
        areaVagoes = self.query_one("#textArea_trem_vagoes", TextArea)
        areaVagoes.text = lista_vagoes

    def definir_trens(self):
        lista_trens = ControllerCMD.listar_trens_garagem()
        areaTrens = self.query_one("#textArea_trem_trens", TextArea)
        areaTrens.text = lista_trens

    def compose(self) -> ComposeResult:
        yield HorizontalGroup(
            Button("Criar Trem", id="cadastrar"),
            Button("Voltar", id="trocar_tela"),
            id="container_engatar",
        )
        yield HorizontalGroup(
            Label("Digite aqui o id do: "),
            InputEventoTrem("Trem", id="input_trem_veiculo"),
            InputEvento("Veiculo", id="input_trem"),
            Button("Engatar no Trem", id="engatar"),
            Button("Desengatar", id="desengatar"),
            id="container_engatar2",
        )
        yield TextArea(disabled=True, id="textArea_engatar")
        yield HorizontalGroup(
            TextArea(id="textArea_trem_locomotivas", disabled=True),
            TextArea(id="textArea_trem_vagoes", disabled=True),
            TextArea(id="textArea_trem_trens", disabled=True),
        )
        yield Button("Theme", id="theme")

    def on_mount(self) -> None:
        self.definir_locomotivas()
        self.definir_vagoes()
        self.definir_trens()
