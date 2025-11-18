import tkinter as tk
from view import TelaLogin, TelaCadastroProduto, TelaManutencaoProduto, TelaMenu

if __name__ == "__main__":
    janela = tk.Tk()
    # app = TelaLogin.TelaLogin(janela)
    # app = TelaCadastroProduto.TelaCadastroProduto(janela)
    # app = TelaManutencaoProduto.TelaManutencaoProduto(janela)
    app = TelaMenu.TelaMenu()
    app.mainloop()
