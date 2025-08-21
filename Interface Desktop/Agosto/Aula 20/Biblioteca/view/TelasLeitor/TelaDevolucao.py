from textual.widgets import Input, Pretty, TextArea, Button, Checkbox, Footer, Header, Select
from textual.screen import Screen
from textual.containers import HorizontalGroup
from controller import Controller
from textual import on
from model import Init


class TelaDevolucao(Screen):

    CSS_PATH = "css/TelaDevolucao.tcss"

    def compose(self):
        yield Header()
        with HorizontalGroup(id="container"):
            pass
        with HorizontalGroup(id="hg_pesquisa"):
            yield Input(placeholder="cod_livro")
            yield Button("Voltar", id="bt_voltar")
        yield Footer()

    emprestimos = Init.leitor1.get_lista_emprestimos()
    emprestimos_filtrados = []
    filtrou_checkbox = False
    filtrou_select = False
    filtrou_input = False
    select_evento = ""
    checkbox_evento = ""

    # def montar_checkboxes(self):
    #     lista_categorias = []
    #     horizontal = self.query_one("#container", HorizontalGroup)
    #     for produto in self.produtos:
    #         if produto.get_categoria() not in lista_categorias:
    #             horizontal.mount(Checkbox(produto.get_categoria()))
    #             lista_categorias.append(produto.get_categoria())
    #     self.query_one(Select).set_options(
    #         [(categoria, categoria) for categoria in lista_categorias])

    # def setup_dados(self):
    #     if len(self.produtos_filtrados) > 0:
    #         quant = len(self.produtos_filtrados)
    #     else:
    #         quant = len(self.produtos)
    #     self.query_one(TextArea).text = f"Quantidade de produtos: {quant}"

    def on_mount(self):
        produtos_str = [str(emprestimo) for emprestimo in self.emprestimos]
        horizontal = self.query_one("#container", HorizontalGroup)
        horizontal.mount(Pretty(produtos_str))
        # self.montar_checkboxes()
        # self.setup_dados()

    def on_button_pressed(self):
        self.screen.app.switch_screen("tela_inicial")

    # @on(Checkbox.Changed)
    # def checkbox_changed(self, evento: Checkbox.Changed):
    #     valor_checkbox = str(evento.checkbox.label)
    #     if evento.checkbox.value is False:
    #         if self.filtrou_input == False and self.filtrou_select == False and self.filtrou_checkbox:
    #             self.produtos_filtrados = []
    #         produtos_str = [str(produto) for produto in self.produtos]
    #         self.query_one(Pretty).update(produtos_str)
    #         self.setup_dados()
    #         self.filtrou_checkbox = False
    #     else:
    #         if self.filtrou_input == False and self.filtrou_select == False and self.filtrou_checkbox:
    #             self.produtos_filtrados = []
    #         if len(self.produtos_filtrados) == 0:
    #             for produto in self.produtos:
    #                 if produto.get_categoria() == valor_checkbox:
    #                     self.produtos_filtrados.append(produto)
    #         else:
    #             produtos_temp = []
    #             for produto in self.produtos_filtrados:
    #                 if produto.get_categoria() == valor_checkbox:
    #                     produtos_temp.append(produto)
    #             if len(produtos_temp) > 0:
    #                 self.produtos_filtrados = produtos_temp
    #         produtos_str = [str(produto)for produto in self.produtos_filtrados]
    #         self.query_one(Pretty).update(produtos_str)
    #         self.setup_dados()
    #         self.filtrou_checkbox = True
    #         self.checkbox_evento = evento