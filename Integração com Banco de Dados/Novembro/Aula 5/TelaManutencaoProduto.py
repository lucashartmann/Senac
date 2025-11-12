import tkinter as tk
from tkinter import ttk, messagebox
from decimal import Decimal
from Estoque import Estoque
from Produto import Produto


class TelaManutencaoProduto():
    def __init__(self, root):
        self.root = root
        self.root.title("Manutenção de Produtos")
        self.root.geometry("1000x600")
        self.root.configure(bg="brown")
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="green", 
                fieldbackground="brown", foreground="white")
        style.configure('My.TFrame', background='green')

        self.frame_tabela = ttk.Frame(self.root, style='My.TFrame')
        
        self.tree = ttk.Treeview(self.root, columns=(
            'nome', 'valor', 'quantidade'), show='headings', style="Treeview")

        self.tree.heading('nome', text='Nome')
        self.tree.column("nome", width=250)

        self.tree.heading('valor', text='Valor')
        self.tree.column("valor", width=100, anchor=tk.E)

        self.tree.heading('quantidade', text='Quantidade')
        self.tree.column("quantidade", width=250, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeViewSelect>>", self.selecionar_produto)
        
        frame_campos = ttk.LabelFrame(self.root, text="Dados do Produto Selecionado", style='My.TFrame')
        frame_campos.pack(pady=10, padx=10, fill=tk.X)
        
        tk.Label(frame_campos, text="Nome: ").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nome = tk.Entry(frame_campos, width=30)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_campos, text="Valor: ").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.entry_valor = tk.Entry(frame_campos, width=15)
        self.entry_valor.grid(row=0, column=3, padx=5, pady=5)
        
        tk.Label(frame_campos, text="Quantidade: ").grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)
        self.entry_quantidade = tk.Entry(frame_campos, width=30)
        self.entry_quantidade.grid(row=0, column=5, padx=5, pady=5)
        
        self.id_produto_selecionado = None
        
        self.frame_botoes = ttk.Frame(self.root, style='My.TFrame')
        
        self.frame_botoes.pack(pady=10)
        
        self.btn_alterar = tk.Button(self.frame_botoes, text="Alterar Produto", command=self.alterar_produto)
        self.btn_alterar.pack(side=tk.LEFT, padx=10)
        
        self.btn_excluir = tk.Button(self.frame_botoes, text="Deletar Produto", command=self.excluir_produto_selecionado)
        self.btn_excluir.pack(side=tk.RIGHT, padx=10)
        
        self.btn_limpar = tk.Button(self.frame_botoes, text="Limpar Campos", command=self.limpar_entrys)
        self.btn_limpar.pack(side=tk.RIGHT, padx=10)

        self.estoque = Estoque()
        self.preencher_tabela()
        
    def alterar_produto(self):
        if not self.id_produto_selecionado:
            messagebox.showwarning("Aviso", "Selecione um produto na tabela para alterar")
        try:
            
            nome = self.entry_nome.get().strip()
            valor = self.entry_valor.get().strip()
            quantidade = self.entry_quantidade.get().strip()
            
            if not valor or not nome or not quantidade:
                raise Exception("Preencha todos os campos!")
            
            valor = float(self.entry_valor.get().strip())
            quantidade = int(self.entry_quantidade.get().strip())
            
        except Exception as e:
            print(e)
            messagebox.showerror("ERRO!", e)
            
        produto = Produto(nome, valor, quantidade)
        produto.set_id(self.id_produto_selecionado)
        
        alteracao = self.estoque.alterar_produto(produto)
        
        if alteracao:
            messagebox.showinfo("Sucesso", f"Produto {nome} alterado!")
        else:
            messagebox.showerror("Erro!", f"Produto {nome} não pode ser alterado")
            
            
        
    def selecionar_produto(self):
        self.limpar_entrys()
        item_selecionado = self.tree.focus()
        if item_selecionado:
            valores = self.tree.item(item_selecionado, "values")
            if valores:
                self.id_produto_selecionado = int(valores[0])
                self.entry_nome.insert(0, valores[1])
                self.entry_valor.insert(0, valores[2])
                self.entry_quantidade.insert(0, valores[3])
                
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
        
    def limpar_entrys(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.id_produto_selecionado = None


if __name__ == "__main__":
    root = tk.Tk()
    app = TelaManutencaoProduto(root)
    root.mainloop()


