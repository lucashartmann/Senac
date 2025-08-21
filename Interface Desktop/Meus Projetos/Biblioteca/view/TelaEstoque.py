from textual.widgets import Input, Pretty, TextArea, Button, Checkbox, Footer, Header, Select
from textual.screen import Screen
from textual.containers import HorizontalGroup
from controller import Controller
from textual import on
from model import Init


class TelaEstoque(Screen):
    CSS_PATH = "css/TelaEstoque.tcss"

    def compose(self):
        yield Header()
        with HorizontalGroup(id="hg_pesquisa"):
            yield Select([("genero", 'genero')])
            yield Input()
            if Init.usuario_leitor:
                yield Button("Retirar", id="bt_retirar")
            yield Button("Voltar", id="bt_voltar")
        yield TextArea(disabled=True)
        with HorizontalGroup(id="container"):
            pass
        yield Footer()

    livros = Controller.get_livros_biblioteca().values()
    livros_filtrados = []
    filtrou_checkbox = False
    filtrou_select = False
    filtrou_input = False
    select_evento = ""

    def setup_dados(self):
        if len(self.livros_filtrados) > 0:
            quant = len(self.livros_filtrados)
        else:
            quant = len(self.livros)
        self.query_one(TextArea).text = f"Quantidade de livros: {quant}"

    def on_mount(self):
        if Init.usuario_leitor:
            livros_str = []
            for livro in self.livros:
                if livro.is_disponivel():
                    livro.__str__ = livro.__str__().split(",")[:-1]
                    livros_str.append(livro.__str__)
        else:
            livros_str = [str(livro) for livro in self.livros]
        self.mount(Pretty(livros_str))
        self.setup_dados()

    def _on_screen_resume(self):
        lista_categorias = []
        for livro in self.livros:
            if livro.get_genero() not in lista_categorias:
                lista_categorias.append(livro.get_genero())
        self.query_one(Select).set_options(
            [(categoria, categoria) for categoria in lista_categorias])

    def on_button_pressed(self, evento: Button.Pressed):
        match evento.button.id:
            case "bt_voltar":
                if not Init.usuario_leitor:
                    self.screen.app.switch_screen("tela_admin")
                else:
                    self.screen.app.switch_screen("tela_leitor")
            case "bt_retirar":
                cod_livro = self.query_one(Input).value
                retirada = Controller.emprestar(
                    cod_livro, Init.leitor1.get_email())
                self.notify(retirada)

    @on(Select.Changed)
    def select_changed(self, evento: Select.Changed):
        if evento.select.is_blank():
            if self.filtrou_input == False and self.filtrou_select:
                self.livros_filtrados = []
            livros_str = [str(livro) for livro in self.livros]
            self.query_one(Pretty).update(livros_str)
            self.setup_dados()
            self.filtrou_select = False
        else:
            valor_select = str(evento.value)
            valor_antigo = ""
            if valor_select != valor_antigo and self.filtrou_input == False and self.filtrou_select:
                self.livros_filtrados = []
                valor_antigo = valor_select
            if len(self.livros_filtrados) == 0:
                for livro in self.livros:
                    if livro.get_genero() == valor_select:
                        self.livros_filtrados.append(livro)
            else:
                livros_temp = []
                for livro in self.livros_filtrados:
                    if livro.get_genero() == valor_select:
                        livros_temp.append(livro)
                if len(livros_temp) > 0:
                    self.livros_filtrados = livros_temp

            livros_str = [str(livro)for livro in self.livros_filtrados]
            self.query_one(Pretty).update(livros_str)
            self.setup_dados()
            self.filtrou_select = True
            self.select_evento = evento

    def on_input_changed(self, evento: Input.Changed):
        texto = evento.value.upper()
        resultado = self.query_one(Pretty)
        palavras = texto.split()

        if len(palavras) > 0:
            if self.filtrou_select == False and self.filtrou_checkbox == False:
                self.livros_filtrados = []

            if "GENERO:" in palavras:  # TODO: Permitir multiplas generos
                index = palavras.index("GENERO:")
                if index + 1 < len(palavras):
                    genero_busca = palavras[index + 1]
                    if len(self.livros_filtrados) > 0:
                        livros_temp = []
                        for livro in self.livros_filtrados:
                            if livro.get_genero() == genero_busca:
                                livros_temp.append(livro)
                        if len(livros_temp) > 0:
                            self.livros_filtrados = livros_temp
                    else:
                        for livro in self.livros:
                            if livro.get_genero() == genero_busca:
                                self.livros_filtrados.append(livro)

            if "TITULO:" in palavras:
                index = palavras.index("TITULO:")
                if index + 1 < len(palavras):
                    titulo_busca = palavras[index + 1]
                    if len(self.livros_filtrados) > 0:
                        livros_temp = []
                        for livro in self.livros_filtrados:
                            if livro.get_titulo() == titulo_busca:
                                livros_temp.append(livro)
                        if len(livros_temp) > 0:
                            self.livros_filtrados = livros_temp
                    else:
                        for livro in self.livros:
                            if livro.get_titulo() == titulo_busca:
                                self.livros_filtrados.append(livro)

            if "QUANTIDADE:" in palavras:
                index = palavras.index("QUANTIDADE:")
                if index + 1 < len(palavras):
                    try:
                        quantidade_busca = int(palavras[index + 1])
                        if len(self.livros_filtrados) > 0:
                            livros_temp = []
                            for livro in self.livros_filtrados:
                                if livro.get_quant() == quantidade_busca:
                                    livros_temp.append(livro)
                            if len(livros_temp) > 0:
                                self.livros_filtrados = livros_temp
                        else:
                            for livro in self.livros:
                                if livro.get_quant() == quantidade_busca:
                                    self.livros_filtrados.append(livro)
                    except ValueError:
                        self.notify("Valor inválido")

            if "AUTOR:" in palavras:
                index = palavras.index("AUTOR:")
                if index + 1 < len(palavras):
                    autor_busca = palavras[index + 1].upper()
                    if len(self.livros_filtrados) > 0:
                        livros_temp = []
                        for livro in self.livros_filtrados:
                            if livro.get_autor() == autor_busca:
                                livros_temp.append(livro)
                        if len(livros_temp) > 0:
                            self.livros_filtrados = livros_temp
                    else:
                        for livro in self.livros:
                            if livro.get_autor() == autor_busca:
                                self.livros_filtrados.append(livro)

            if "CODIGO:" in palavras:
                index = palavras.index("CODIGO:")
                if index + 1 < len(palavras):
                    try:
                        codigo_busca = int(palavras[index + 1])
                        if len(self.livros_filtrados) > 0:
                            livros_temp = []
                            for livro in self.livros_filtrados:
                                if livro.get_codigo() == codigo_busca:
                                    livros_temp.append(livro)
                            if len(livros_temp) > 0:
                                self.livros_filtrados = livros_temp
                        else:
                            for livro in self.livros:
                                if livro.get_codigo() == codigo_busca:
                                    self.livros_filtrados.append(livro)
                    except ValueError:
                        self.notify("Valor inválido")

            if len(self.livros_filtrados) > 0:
                livros_str = [str(livro)
                              for livro in self.livros_filtrados]
                resultado.update(livros_str)
                self.setup_dados()
            else:
                livros_str = [str(livro) for livro in self.livros]
                resultado.update(livros_str)
                self.setup_dados()
        else:
            if len(self.livros_filtrados) > 0 and self.filtrou_select == False:
                livros_str = [str(livro)
                              for livro in self.livros_filtrados]
                resultado.update(livros_str)
                self.setup_dados()
            elif self.filtrou_select:
                self.select_changed(self.select_evento)
            else:
                livros_str = [str(livro) for livro in self.livros]
                resultado.update(livros_str)
                self.setup_dados()
