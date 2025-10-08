
import tkinter as tk


def exibir_mensagem():
    nome = entry_name.get()
    idade = entry_idade.get()
    if textarea_resultado.get('1.0', 'end'):
        textarea_resultado.delete("1.0", 'end')
    textarea_resultado.insert("1.0", f"Nome: {nome} \nIdade: {idade}")


root = tk.Tk()
root.geometry("800x500+600+200")
root.configure(background="purple")

parent_frame = tk.Frame(root, bg="lightblue", width=300, height=200)
parent_frame.pack(expand=True, fill="both")

janela = tk.Frame(parent_frame,  background="green")
janela.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label_name = tk.Label(janela, text="Nome:", background="yellow")
label_idade = tk.Label(janela, text="Idade:", background="yellow")

entry_name = tk.Entry(janela)
entry_name.insert(0, "Digite o nome aqui")
entry_idade = tk.Entry(janela)
entry_idade.insert(0, "Digite a idade aqui")

button_ok = tk.Button(janela, text="cadastrar", command=exibir_mensagem)

textarea_resultado = tk.Text(janela, width=50, height=10)

label_name.grid(column=0, row=0)
entry_name.grid(column=1, row=0, padx=100)
label_idade.grid(column=0, row=1, padx=100)
entry_idade.grid(column=1, row=1, padx=100)
button_ok.grid(column=2, row=0, ipady=10, padx=100, ipadx=30)
textarea_resultado.grid(column=1, row=3)


root.mainloop()
