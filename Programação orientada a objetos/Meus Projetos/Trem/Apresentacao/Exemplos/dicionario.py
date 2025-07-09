import asyncio
import httpx
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Input, Static, Label
from textual.reactive import reactive

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

# python dicionario.py

class DefinitionCard(Vertical):
    def __init__(self, word, meanings, **kwargs):
        super().__init__(**kwargs)
        self.word = word
        self.meanings = meanings

    def compose(self) -> ComposeResult:
        yield Static(f"[b]{self.word}[/b]", id="word-card")
        for meaning in self.meanings:
            yield Static(f"[i]{meaning['partOfSpeech']}[/i]", classes="part")
            for d in meaning['definitions']:
                yield Static(f"• {d['definition']}")
            yield Static("", classes="divider")

class DictionaryApp(App):
    CSS = '''
    #searchbox {
        margin: 1 1 1 1;
        height: 3;
        background: #222;
        color: white;
        border: none;
        padding: 0 2;
    }
    #resultbox {
        border: solid #29508a;
        border-title-color: #29508a;
        border-title-align: center;
        margin: 1 1 1 1;
        padding: 1 2;
    }
    #word-card {
        background: #29508a;
        color: white;
        height: 3;
        content-align: center middle;
        margin: 1 0 1 0;
        border: none;
    }
    #part {
        color: #aaa;
        margin: 1 0 0 0;
    }
    #def {
        color: white;
        margin: 0 0 0 2;
    }
    .divider {
        border-bottom: solid #29508a;
        margin: 1 0 1 0;
    }
    '''
    query = reactive("")

    def compose(self) -> ComposeResult:
        yield Input(placeholder="hello", id="searchbox")
        self.resultbox = Vertical(id="resultbox")
        yield self.resultbox

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        word = event.value.strip()
        if not word:
            return
        self.resultbox.remove_children()
        await self.show_loading()
        await self.fetch_and_show(word)

    async def show_loading(self):
        self.resultbox.remove_children()
        self.resultbox.mount(Static("Buscando..."))

    async def fetch_and_show(self, word):
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(API_URL.format(word))
                data = resp.json()
            if isinstance(data, list):
                card = DefinitionCard(data[0]['word'], data[0]['meanings'])
                self.resultbox.remove_children()
                self.resultbox.mount(card)
            else:
                self.resultbox.remove_children()
                self.resultbox.mount(Static("Palavra não encontrada."))
        except Exception as e:
            self.resultbox.remove_children()
            self.resultbox.mount(Static(f"Erro: {e}"))

if __name__ == "__main__":
    DictionaryApp().run()
