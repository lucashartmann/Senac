from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Header, Footer, TextArea
from textual.screen import Screen
from controller.ControllerCMD import ControllerCMD

# python -m telas.TelaInicial


class TelaDados(Screen):

    CSS_PATH = "../css/Telas.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def on_button_pressed(self, event: Button.Pressed):
        areaTexto = self.screen.query_one("#resultado", TextArea)
        str_lista = ""
        str_quant = ""
        match event.button.id:
            case "locomotivas_garagem":
                str_lista = ControllerCMD.listar_locomotivas_garagem()
                str_quant = ControllerCMD.get_quant_locomotivas_garagem()
            case "vagoes_garagem":
                str_lista = ControllerCMD.listar_vagoes_garagem()
                str_quant = ControllerCMD.get_quant_vagoes_garagem()
            case "trens_garagem":
                str_lista = ControllerCMD.listar_trens_garagem()
                str_quant = ControllerCMD.get_quant_trens_garagem()
            case "veiculos_garagem":
                str_lista = ControllerCMD.listar_veiculos_garagem()
                str_quant = ControllerCMD.get_quant_veiculos_garagem()
            case "trocar_tela":
                self.screen.app.pop_screen()
        str_final = str_quant + "\n" + str_lista
        areaTexto.text = str_final

    def compose(self) -> ComposeResult:
        yield HorizontalGroup(
            Button("Locomotivas na garagem", id="locomotivas_garagem"),
            Button("Vagões na garagem", id="vagoes_garagem"),
            Button("Trens na garagem", id="trens_garagem"),
            Button("Todos os veiculos na garagem", id="veiculos_garagem"),
            Button("Voltar", id="trocar_tela"),
        )
        yield TextArea(id="resultado", disabled=True)
