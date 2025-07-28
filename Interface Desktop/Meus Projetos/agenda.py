from textual.app import App
from textual.widgets import Input, TextArea, Label
from textual.events import Click
from textual.containers import HorizontalGroup, VerticalGroup


class Agenda(App):

    CSS = '''
        #container {
            height: 14;
            width: 50%;
            padding: 1;
            color: white;
            background: black;
            margin-bottom: 3;
        }
        #conteudo {
            height: 14;
            width: 100%;
            padding: 1;
            color: black;
            background: white;
            margin-bottom: 3;
        }
        .contatos {
            margin-bottom: 1;
        }
        #lbl_nome {
            margin-top: 1;
        }
    '''

    lista_nomes = {
        "lucas@email.com": ["lucas", "51000000000", "Avenida Bento Gonçalves 203"],
        "leonardo@email.com": ["leonardo", "51111111111", "Lopo Gonçalves 23"],
        "william@email.com": ["william", "51333333333", "João Portinha 193"],
        "gabriele@email.com": ["gabriele", "51444444444", "Travessa Ferreira de Abreu 94"],
        "yuri@email.com": ["yuri", "51555555555", "Felipe de Oliveira 97"],
        "arthur@email.com": ["arthur", "51666666666", "Zélia Maria Abichequer 400"]
    }

    async def on_input_changed(self, event: Input.Changed):
        vertical = self.query_one("#container", VerticalGroup)
        await vertical.remove_children()
        texto_input = event.value.lower()
        contatos = self.filtrar(texto_input)
        for email, contato in contatos.items():
            vertical.mount(
                Label(f"👤 {contato[0].capitalize()}", name=email, classes="contatos"))

    def filtrar(self, texto_input):
        mapa_contatos = {}
        for email, contato in self.lista_nomes.items():
            if contato[0].startswith(texto_input):
                mapa_contatos[email] = contato
        return mapa_contatos

    def compose(self):
        with HorizontalGroup():
            with VerticalGroup(id="container"):
                for email, contato in self.lista_nomes.items():
                    yield Label(f"👤 {contato[0].capitalize()}", name=email, classes="contatos")
            with HorizontalGroup(id="resultado"):
                pass
        with HorizontalGroup():
            yield Label("Digite o nome:", id="lbl_nome")
            yield Input(placeholder="Digite aqui")

    def on_click(self, evento: Click):
        if isinstance(evento.widget, Label):
            horizontal = self.query_one("#resultado", HorizontalGroup)
            try:
                self.query_one("#conteudo", TextArea).remove()
            except:
                horizontal = self.query_one("#resultado", HorizontalGroup)
                horizontal.mount(TextArea(id="conteudo"))
                dados = self.lista_nomes[evento.widget.name]
                mensagem = f'''📧 {dados[0]}
                
📞 {dados[1]}

🏢 {dados[2]}'''
                self.query_one("#conteudo", TextArea).text = mensagem


Agenda().run()
