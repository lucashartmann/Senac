from textual.widgets import Input, Pretty, TextArea, Button, Footer, Header
from textual.screen import Screen
from textual.containers import HorizontalGroup
from controller import Controller


class TelaClientela(Screen):
    CSS_PATH = "css/TelaClientela.tcss"

    def compose(self):
        yield Header()
        with HorizontalGroup(id="hg_pesquisa"):
            yield Input()
            yield Button("Voltar", id="bt_voltar")
        yield TextArea(disabled=True)
        with HorizontalGroup(id="container"):
            pass
        yield Footer()

    leitores = Controller.get_leitores_biblioteca().values()
    leitores_filtrados = []

    def setup_dados(self):
        if len(self.leitores_filtrados) > 0:
            quant = len(self.leitores_filtrados)
        else:
            quant = len(self.leitores)
        self.query_one(TextArea).text = f"Quantidade de leitores: {quant}"

    def on_mount(self):
        leitores_str = [str(leitor) for leitor in self.leitores]
        self.mount(Pretty(leitores_str))
        self.setup_dados()

    def on_button_pressed(self):
        self.screen.app.switch_screen("tela_admin")

    def on_input_changed(self, evento: Input.Changed):
        texto = evento.value.upper()
        resultado = self.query_one(Pretty)
        palavras = texto.split()

        if len(palavras) > 0:
            self.leitores_filtrados = []

            if "NOME:" in palavras:
                index = palavras.index("NOME:")
                if index + 1 < len(palavras):
                    nome_busca = palavras[index + 1]
                    if len(self.leitores_filtrados) > 0:
                        leitores_temp = []
                        for leitor in self.leitores_filtrados:
                            if leitor.get_nome() == nome_busca:
                                leitores_temp.append(leitor)
                        if len(leitores_temp) > 0:
                            self.leitores_filtrados = leitores_temp
                    else:
                        for leitor in self.leitores:
                            if leitor.get_nome() == nome_busca:
                                self.leitores_filtrados.append(leitor)

            if "EMAIL:" in palavras:
                index = palavras.index("EMAIL:")
                if index + 1 < len(palavras) and len(palavras[index + 1]) > 3:
                    email_busca = palavras[index + 1]
                    if len(self.leitores_filtrados) > 0:
                        leitores_temp = []
                        for leitor in self.leitores_filtrados:
                            if leitor.get_email() == email_busca:
                                leitores_temp.append(leitor)
                        if len(leitores_temp) > 0:
                            self.leitores_filtrados = leitores_temp
                    else:
                        for leitor in self.leitores:
                            if leitor.get_email() == email_busca:
                                self.leitores_filtrados.append(leitor)

            if len(self.leitores_filtrados) > 0:
                leitores_str = [str(leitor)
                                for leitor in self.leitores_filtrados]
                resultado.update(leitores_str)
                self.setup_dados()
            else:
                leitores_str = [str(leitor) for leitor in self.leitores]
                resultado.update(leitores_str)
                self.setup_dados()
        else:
            if len(self.leitores_filtrados) > 0:
                leitores_str = [str(leitor)
                                for leitor in self.leitores_filtrados]
                resultado.update(leitores_str)
                self.setup_dados()
            else:
                leitores_str = [str(leitor) for leitor in self.leitores]
                resultado.update(leitores_str)
                self.setup_dados()
