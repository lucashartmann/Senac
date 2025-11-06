import tkinter as tk
from tkinter import messagebox
from decimal import Decimal
from Estoque import Estoque

class TelaCadastroProdutos():
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")
        self.root.geometry("400x300")
        self.root.configure(bg="lightgreen")
        
        tk.Label(self.root, text="Nome: ").grid(row=0, column=0)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)
        
        tk.Label(self.root, text="Valor: ").grid(row=1, column=0)
        self.entry_valor = tk.Entry(self.root)
        self.entry_valor.grid(row=1, column=1)
        
        tk.Label(self.root, text="Quantidade: ").grid(row=2, column=0)
        self.entry_quantidade = tk.Entry(self.root)
        self.entry_quantidade.grid(row=2, column=1)
        
        btn_salvar = tk.Button(self.root, text="Salvar", command=self.salvar_produtos)
        btn_salvar.grid(row=3, column=1, pady=10)
        
        btn_limpar = tk.Button(self.root, text="Limpar", command=self.limpar_entrys)
        btn_limpar.grid(row=3, column=2, padx=10)
        
    def salvar_produtos(self):
        pass
    
    def limpar_entrys(self):
        self.entry_name.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TelaCadastroProdutos(root)
    root.mainloop()