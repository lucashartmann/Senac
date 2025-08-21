from textual.app import App
from view import TelaInicial
from view.TelasLeitor import TelaDevolucao, TelaEmprestimo, TelaLeitor
from view.TelasAdmin import TelaAdmin, TelaCadastroLeitor, TelaCadastroLivro, TelaClientela, TelaEstoque


class App(App):

    SCREENS = {
        "tela_inicial": TelaInicial.TelaInicial,
        "tela_estoque": TelaEstoque.TelaEstoque,
        "tela_clientela": TelaClientela.TelaClientela,
        "tela_devolucao": TelaDevolucao.TelaDevolucao,
        "tela_emprestimo": TelaEmprestimo.TelaEmprestimo,
        "tela_cadastro_leitor": TelaCadastroLeitor.TelaCadastroLeitor,
        "tela_cadastro_livro": TelaCadastroLivro.TelaCadastroLivro,
        "tela_admin": TelaAdmin.TelaAdmin,
        "tela_leitor": TelaLeitor.TelaLeitor,
    }

    def on_mount(self):
        self.title = "Biblioteca"
        self.push_screen("tela_inicial")
