from textual.app import App
from textual.widgets import Label, Input, Button, Pretty
from textual.widget import Widget
from textual.containers import HorizontalGroup
from textual.reactive import reactive


class ListaProdutos(Widget):
    produtos = reactive({
        "produto1": {
            "nome": "sapato",
            "preco": 240.00,
            "quantidade": 20
        }
    })

    def render(self):
        return Pretty(self.produtos).render()
        
    # def render(self):
    #     listagem = str()
    #     for cod, dados in self.produtos.items():
    #         listagem = f"{cod}: {dados['nome']}, {dados['preco']}, {dados['quantidade']} \n"
    #     return listagem


class App(App):
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
        yield Button("Cadastrar", id='bt_cadastrar')
        yield ListaProdutos(id="lst_produtos")

    def limpar_inputs(self):
        for input in self.query(Input):
            input.value = ""

    def on_button_pressed(self, evento=Button.Pressed):
        if evento.button.id == "bt_cadastrar":
            codigo = self.query_one("#tx_codigo", Input).value
            nome = self.query_one('#tx_nome', Input).value
            preco = float(self.query_one('#tx_preco', Input).value)
            quantidade = int(self.query_one('#tx_quantidade', Input).value)

            lista = self.query_one("#lst_produtos")

            produtos_atualizados = lista.produtos.copy()

            self.limpar_inputs()

            produtos_atualizados[codigo] = {
                "nome": nome, "preco": preco, "quantidade": quantidade}

            lista.produtos = produtos_atualizados

            self.query_one("#tx_codigo", Input).focus()


if __name__ == '__main__':
    app = App()
    app.run()
