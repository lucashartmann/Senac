import tkinter as tk
from tkinter import messagebox
from decimal import Decimal
from Produto import Produto

class TelaCadastroProdutos():
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")
        self.root.geometry("400x300")
        self.root.configure(bg="lightgreen")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TelaCadastroProdutos(root)
    root.mainloop()