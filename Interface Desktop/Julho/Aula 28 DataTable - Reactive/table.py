from textual.app import App
from textual.widgets import Label, Input, Button, Pretty, DataTable
from textual.widget import Widget
from textual.containers import HorizontalGroup
from textual.reactive import reactive


class Table(App):

    produtos = {
        "produto1": {
            "nome": "sapato",
            "preco": 240.00,
            "quantidade": 20
        }
    }

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
        yield DataTable()

    def limpar_inputs(self):
        for input in self.query(Input):
            input.value = ""

    def on_button_pressed(self, evento=Button.Pressed):
        if evento.button.id == "bt_cadastrar":
            codigo = self.query_one("#tx_codigo", Input).value
            nome = self.query_one('#tx_nome', Input).value
            preco = float(self.query_one('#tx_preco', Input).value)
            quantidade = int(self.query_one('#tx_quantidade', Input).value)

            self.limpar_inputs()

            table = self.query_one(DataTable)

            table.add_row(codigo, nome, preco, quantidade)

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("codigo", "nome", "preço", "quantidade")

        lista = list()
        for dados in self.produtos.values():
            for dado2 in dados.values():
                    lista.append(dado2)
        table.add_row(*lista)

        # for coluna in self.colunas[1:]:
        #     styled_row = [
        #         Text(str(cell), style="italic #03AC13", justify="right") for cell in coluna
        #     ]


if __name__ == '__main__':
    app = Table()
    app.run()
