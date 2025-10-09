import tkinter as tk
from tkinter import messagebox

# Criando a janela principal
janela = tk.Tk()
janela.title("Interatividade com Widgets")
janela.geometry("320x200+400+300")

rotulo = tk.Label(janela, text="Digite seu nome:")
rotulo.pack()

entrada = tk.Entry(janela)
entrada.pack()

def exibir_mensagem():
    nome = entrada.get()
    if nome:
        messagebox.showinfo("Saudação", f"Olá, {nome}!")
    else:
        messagebox.showwarning("Aviso", "Por favor, insira seu nome.")

botao = tk.Button(janela, text="Enviar", command=exibir_mensagem)
botao.pack()

janela.mainloop()