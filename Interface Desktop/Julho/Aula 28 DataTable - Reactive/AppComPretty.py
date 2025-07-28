from textual.app import App
from textual.widgets import Label, Input, Pretty, Button
from textual.containers import HorizontalGroup

class Agenda(App):
    produtos = {
        "produto1": {
            "nome": "sapato", 
            "preco": 240.00,
            "quantidade": 20
        }
    }

    def on_mount(self):
        try:
            self.get_child_by_type(Pretty).remove()
            self.mount(Pretty(self.produtos))
        except:
            self.mount(Pretty(self.produtos))

    def listagem(self):
        mensagem = ""
        for nome, dados in self.produtos.items():
            mensagem += f"\nChave: {nome}\n"
            for chave, dado2 in dados.items():      
                    if type(dado2) == float:
                        mensagem = mensagem + " " + f"{chave.capitalize()}: R$" + str(dado2) + "\n"
                    else:
                        mensagem = mensagem + " " + f"{chave.capitalize()}: " + str(dado2) + "\n"
        return mensagem
    
    def compose(self):
        with HorizontalGroup():
            yield Label("Digite o codigo")
            yield Input(id='tx_codigo')
        with HorizontalGroup():
            yield Label("Digite o nome")
            yield Input(id='tx_nome')
        with HorizontalGroup():
            yield Label("Digite o preço")
            yield Input(id='tx_preco')
        with HorizontalGroup():
            yield Label("Digite a quantidade")
            yield Input(id='tx_quantidade')
        yield Button("Cadastrar", id='bt_CadastrarProduto')

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == 'bt_CadastrarProduto':
            codigo = self.query_one("#tx_codigo", Input).value
            nome = self.query_one('#tx_nome', Input).value
            preco = float(self.query_one('#tx_preco', Input).value)
            quantidade = int(self.query_one('#tx_quantidade', Input).value)

            self.produtos[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}
            self.on_mount()
            mensagem = f"{nome.capitalize()} cadastrado!"
            self.notify(mensagem)

if __name__ == '__main__':
    app = Agenda()
    app.run()