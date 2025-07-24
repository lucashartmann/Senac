from textual.app import App
from textual.widgets import Label, Input, Button, Static, Pretty
from textual.screen import Screen


class TelaListagem(Screen):
    def on_mount(self):
        self.styles.layout = "vertical"

    def on_button_pressed(self, evento: Button.Pressed):
        self.screen.app.pop_screen()

    def compose(self):
        yield Pretty(Agenda.AGENDA)
        yield Button("Voltar", id="bt_voltar")


class Agenda(App):

    AGENDA = {
        "nome@email.com": {"nome": "Nome da pessoa", "telefone": "51 999999"},
        "nome2@email.com": {"nome": "Nome da pessoa", "telefone": "51 999999"}
    }

    CSS_PATH = 'Agenda.tcss'

    def compose(self):
        self.styles.layout = "grid"
        yield Static(
            """
-----------------
XP Agenda
-----------------

            """)
        yield Static('[i]versão 0.0.1[/]')
        yield Label("Nome: ")
        yield Input(id='input_nome')

        yield Label("E-mail: ")
        yield Input(id='input_email')

        yield Label("Telefone: ")
        yield Input(id='input_fone')

        yield Button("Limpar", id='bt_limpar')
        yield Button("Cadastrar", id='bt_cadastrar')
        yield Button("Agenda de contatos", id='bt_listar')

    def limpar_formulario(self):
        for input in self.query(Input):
            input.value = ''

    def on_button_pressed(self, evento: Button.Pressed):
        if evento.button.id == "bt_listar":
            self.push_screen(TelaListagem())

        if evento.button.id == 'bt_limpar':
            self.limpar_formulario()

        if evento.button.id == 'bt_cadastrar':
            nome = self.query_one('#input_nome', Input).value
            email = self.query_one('#input_email', Input).value
            fone = self.query_one('#input_fone', Input).value

            Agenda.AGENDA[email] = {"nome": nome, "fone": fone}

            self.limpar_formulario()
            self.notify(f'{Agenda.AGENDA[email]} cadastrado!')


if __name__ == '__main__':
    app = Agenda()
    app.run()
