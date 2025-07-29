class Empresa():
    def __init__(self):
        self.clientes = []

    def cadastrar(self, cliente):
        if cliente not in self.clientes:
            self.clientes.append(cliente)
            return True
        return False
        
    def get_lista_clientes(self):
        if len(self.clientes) > 0:
            return self.clientes
        return None

class Cliente():
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def __str__(self):
        return f"Cliente[nome = {self.nome}]"

    
class Controller():
    empresa1 = Empresa()

    def cadastro(nome):
        novo_cliente = Cliente(nome)
        condicao = Controller.empresa1.cadastrar(novo_cliente)
        if condicao:
            return "Cliente cadastrado na empresa com sucesso!"
        else:
            return "ERRO. Cadastro não realizado"
        
    def ver_clientes():
        lista_clientes = Controller.empresa1.get_lista_clientes()
        if lista_clientes:
            return "\n".join(str(cliente) for cliente in lista_clientes)
        else: 
            return "Não há clientes cadastrados"
        


from textual.app import App 
from textual.widgets import Static, Button, TextArea, Input
from textual.containers import HorizontalGroup

class Tela(App):

    CSS_PATH = "Tela.tcss"

    def compose(self):
        with HorizontalGroup(id="container"):
            yield Static("Digite seu nome", id="static1")
            yield Input()
            yield Button("Cadastrar", id="btn_cadastro")
        yield TextArea()

    def on_button_pressed(self, evento: Button.Pressed):
        nome = self.query_one(Input).value
        resultado_cadastro = Controller.cadastro(nome)
        resultado_consulta = Controller.ver_clientes()
        self.query_one(TextArea).text = f"{resultado_cadastro}\n{resultado_consulta}" 

        

if __name__ == "__main__":
    app = Tela()
    app.run()