import tkinter as tk
from view.TelaCadastroProduto import TelaCadastroProduto
from view.TelaManutencaoProduto import TelaManutencaoProduto


class TelaMenu(tk.Tk):
    def __init__(self):
        super().__init__()  # Inicializa a classe base tk.Tk

        self.title("Sistema de Gerenciamento de Cadastro")
        self.geometry("450x400")

        menu_principal = tk.Menu(self)
        self.config(menu=menu_principal)

        menu_arq = tk.Menu(menu_principal)
        menu_principal.add_cascade(label="Cadastro", menu=menu_arq)
        self.configure(bg="lightblue")

        menu_arq.add_command(label="Clientes")
        menu_arq.add_command(label="Colaboradores")
        menu_arq.add_command(label="Fornecedores")
        menu_arq.add_separator()
        menu_arq.add_command(
            label="Produtos", command=self.abrir_cadastro_produtos)

        menu_manutencao = tk.Menu(menu_principal)
        menu_principal.add_cascade(label="Manutenção", menu=menu_manutencao)

        menu_manutencao.add_command(label="Clientes")
        menu_manutencao.add_command(label="Colaboradores")
        menu_manutencao.add_command(label="Fornecedores")
        menu_manutencao.add_separator()
        menu_manutencao.add_command(
            label="Produtos", command=self.abrir_manutencao_produtos)

        menu_principal.add_cascade(label="Sair", command=self.destroy)

    def abrir_cadastro_produtos(self):
        menu_windows = tk.Toplevel(self)
        TelaCadastroProduto(menu_windows)

    def abrir_manutencao_produtos(self):
        menu_windows = tk.Toplevel(self)
        TelaManutencaoProduto(menu_windows)


if __name__ == "__main__":
    app = TelaMenu()
    app.mainloop()
