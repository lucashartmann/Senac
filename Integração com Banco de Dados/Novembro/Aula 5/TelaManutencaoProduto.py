import tkinter as tk
from tkinter import ttk, messagebox
from decimal import Decimal
from Estoque import Estoque
from Produto import Produto


class TelaManutencaoProduto():
    def __init__(self, root):
        self.root = root
        self.root.title("Manutenção de Produtos")
        self.root.geometry("600x200")

        self.tree = ttk.Treeview(self.root, columns=(
            'nome', 'valor', 'quantidade'), show='headings')

        self.tree.heading('nome', text='Nome')
        self.tree.heading('valor', text='Valor')
        self.tree.heading('quantidade', text='Quantidade')

        self.tree.pack(fill='both', expand=True)
        
        self.btn_excluir = tk.Button(self.root, text="Deletar", command=self.excluir_produto_selecionado)
        
        self.btn_excluir.pack()

        self.estoque = Estoque()
        self.preencher_tabela()

    def preencher_tabela(self):
        try:
            produtos = self.estoque.buscar_produtos()
            print(produtos)
            if produtos:
                for produto in produtos:
                    self.tree.insert("", "end", values=(
                        produto.nome, produto.valor, produto.quantidade))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao preencher a tablela: {e}")
            return

    def excluir_produto_selecionado(self):
        item_selecionado = self.tree.selection()

        if not item_selecionado:
            messagebox.showwarning("Aviso", "Selecione o produto para excluir")
            return
        
        id_produto = self.tree.item(item_selecionado, 'tags')[0]
        nome_produto = self.tree.item(item_selecionado, 'values')[0]


        if messagebox.askyesno("Confirmação", f"Deseja realmente excluir o produto? '{nome_produto}'?"):
            if self.estoque.excluir_produto(id_produto):
                messagebox.showinfo("Sucesso", "Produto excluido com sucesso.")
                self.atualizar_tabela()
                
    def atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        self.preencher_tabela()

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaManutencaoProduto(root)
    root.mainloop()
