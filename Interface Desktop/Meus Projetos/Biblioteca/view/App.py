from textual.app import App
from view import TelaCadastroLeitor, TelaEstoque, TelaInicial
from view.TelasLeitor import TelaDevolucao, TelaLeitor
from view.TelasAdmin import TelaAdmin, TelaCadastroLivro, TelaClientela


class App(App):

    SCREENS = {
        "tela_inicial": TelaInicial.TelaInicial,
        "tela_estoque": TelaEstoque.TelaEstoque,
        "tela_clientela": TelaClientela.TelaClientela,
        "tela_devolucao": TelaDevolucao.TelaDevolucao,
        "tela_cadastro_leitor": TelaCadastroLeitor.TelaCadastroLeitor,
        "tela_cadastro_livro": TelaCadastroLivro.TelaCadastroLivro,
        "tela_admin": TelaAdmin.TelaAdmin,
        "tela_leitor": TelaLeitor.TelaLeitor,
    }

    def on_mount(self):
        self.title = "Biblioteca"
        self.push_screen("tela_inicial")
