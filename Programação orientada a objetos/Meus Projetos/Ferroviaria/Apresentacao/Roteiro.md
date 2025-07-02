## Passos

- Primeiro passo: pip install textual
- Segundo passo: criar programa.py
- Terceiro passo: importar biblioteca 


- Abrir cmd, copiando path ou digitando CMD no caminho da pasta
- python AppTela.py


## Explicação:

- compose(self) -> ComposeResult: Método responsável por montar a interface da tela. Nele, você define quais widgets (botões, textos, etc.) vão aparecer.

- yield: Palavra-chave do Python usada para "entregar" cada widget para a tela, um de cada vez, dentro do método compose

- on_button_pressed: Método chamado automaticamente quando um botão é pressionado. É nele que você coloca o que deve acontecer após o clique, como abrir outra tela ou mostrar uma mensagem.

- from textual.app import App: Importa a classe principal do Textual, usada para criar o aplicativo.

- from textual.widgets import Button, Header, Footer: Importa widgets prontos do Textual, como botão, cabeçalho e rodapé, para usar na interface.

- from textual.screen import Screen: Importa a classe usada para criar novas telas (ou páginas) dentro do aplicativo.


def on_key(self, event):
    if event.key == "space":
        # Sua ação aqui
        print("Barra de espaço pressionada!")