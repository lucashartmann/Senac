from textual.widgets import Input, Pretty, TextArea, Button, Footer, Header, Select
from textual.containers import HorizontalGroup, Container
from controller import Controller
from textual import on
from model import Init


class TelaEstoque(Container):
    CSS_PATH = "css/TelaEstoque.tcss"

    def compose(self):
        with HorizontalGroup(id="hg_pesquisa"):
            yield Select([("genero", 'genero')])
            yield Input()
            if Init.usuario_leitor:
                yield Button("Retirar", id="bt_retirar")
            yield Button("Voltar", id="bt_voltar")
        yield TextArea(disabled=True)
        with HorizontalGroup(id="container"):
            pass

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
            if self.filtrou_select == False:
                self.livros_filtrados = []

            for palavra in palavras:
                match palavra:

                    case "GENERO:":  # TODO: Permitir multiplas generos
                        index = palavras.index("GENERO:")
                        if index + 1 < len(palavras):
                            genero_busca = " ".join((palavras[index+1:]))
                            if "," in genero_busca:
                                genero_busca = genero_busca[0:genero_busca.index(
                                    ",")]
                            if len(self.livros_filtrados) > 0:
                                livros_temp = []
                                for livro in self.livros_filtrados:
                                    if genero_busca in livro.get_genero():
                                        livros_temp.append(livro)
                                if len(livros_temp) > 0:
                                    self.livros_filtrados = livros_temp
                            else:
                                for livro in self.livros:
                                    if genero_busca in livro.get_genero():
                                        self.livros_filtrados.append(livro)

                    case  "TITULO:":
                        index = palavras.index("TITULO:")
                        if index + 1 < len(palavras):
                            titulo_busca = " ".join((palavras[index+1:]))
                            if "," in titulo_busca:
                                titulo_busca = titulo_busca[0:titulo_busca.index(
                                    ",")]
                            if len(self.livros_filtrados) > 0:
                                livros_temp = []
                                for livro in self.livros_filtrados:
                                    if titulo_busca in livro.get_titulo():
                                        livros_temp.append(livro)
                                if len(livros_temp) > 0:
                                    self.livros_filtrados = livros_temp
                            else:
                                for livro in self.livros:
                                    if titulo_busca in livro.get_titulo():
                                        self.livros_filtrados.append(livro)

                    case  "QUANTIDADE:":
                        index = palavras.index("QUANTIDADE:")
                        if index + 1 < len(palavras):
                            try:
                                quantidade_busca = int(
                                    " ".join((palavras[index+1:])))
                                if "," in quantidade_busca:
                                    quantidade_busca = quantidade_busca[0:quantidade_busca.index(
                                        ",")]
                                quantidade_busca = int(quantidade_busca)
                                if len(self.livros_filtrados) > 0:
                                    livros_temp = []
                                    for livro in self.livros_filtrados:
                                        if quantidade_busca == livro.get_quant():
                                            livros_temp.append(livro)
                                    if len(livros_temp) > 0:
                                        self.livros_filtrados = livros_temp
                                else:
                                    for livro in self.livros:
                                        if quantidade_busca == livro.get_quant():
                                            self.livros_filtrados.append(livro)
                            except ValueError:
                                self.notify("Valor inválido")

                    case  "AUTOR:":
                        index = palavras.index("AUTOR:")
                        if index + 1 < len(palavras):
                            autor_busca = " ".join((palavras[index+1:]))
                            if "," in autor_busca:
                                autor_busca = autor_busca[0:autor_busca.index(
                                    ",")]
                            if len(self.livros_filtrados) > 0:
                                livros_temp = []
                                for livro in self.livros_filtrados:
                                    if autor_busca in livro.get_autor():
                                        livros_temp.append(livro)
                                if len(livros_temp) > 0:
                                    self.livros_filtrados = livros_temp
                            else:
                                for livro in self.livros:
                                    if autor_busca in livro.get_autor():
                                        self.livros_filtrados.append(livro)

                    case "CODIGO:":
                        index = palavras.index("CODIGO:")
                        if index + 1 < len(palavras):
                            try:
                                codigo_busca = " ".join((palavras[index+1:]))
                                if "," in codigo_busca:
                                    codigo_busca = codigo_busca[0:codigo_busca.index(
                                        ",")]
                                codigo_busca = int(codigo_busca)
                                if len(self.livros_filtrados) > 0:
                                    livros_temp = []
                                    for livro in self.livros_filtrados:
                                        if codigo_busca == livro.get_codigo():
                                            livros_temp.append(livro)
                                    if len(livros_temp) > 0:
                                        self.livros_filtrados = livros_temp
                                else:
                                    for livro in self.livros:
                                        if codigo_busca == livro.get_codigo():
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
