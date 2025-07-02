from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Vertical, Horizontal
from textual.reactive import reactive
import random, string, datetime

# python animacoes.py

# Bolinhas pulando (loading)
class BolinhasLoading(Static):
    frame = reactive(0)
    bolas = ["   ", ".  ", ".. ", "...", " ..", "  ."]
    async def on_mount(self):
        self.set_interval(0.2, self.animate)
    def animate(self):
        self.frame = (self.frame + 1) % len(self.bolas)
        self.refresh()
    def render(self) -> str:
        return f"Carregando{self.bolas[self.frame]}"

# Quadrado se movendo
class QuadradoMovendo(Static):
    x = reactive(0)
    dx = 1
    width = 20
    async def on_mount(self):
        self.set_interval(0.05, self.move)
    def move(self):
        self.x += self.dx
        if self.x >= self.width - 2 or self.x <= 0:
            self.dx *= -1
        self.refresh()
    def render(self) -> str:
        linha = [" "] * self.width
        linha[self.x] = "■"
        return "".join(linha)

# Transição de cores
CORES = ["red", "yellow", "green", "cyan", "blue", "magenta"]
class BlocoColorido(Static):
    cor = reactive(0)
    async def on_mount(self):
        self.set_interval(0.3, self.troca_cor)
    def troca_cor(self):
        self.cor = (self.cor + 1) % len(CORES)
        self.refresh()
    def render(self) -> str:
        return " BLOCO COLORIDO "
    def watch_cor(self, cor):
        self.styles.background = CORES[cor]
        self.styles.color = "black" if CORES[cor] in ["yellow", "cyan"] else "white"

# Gráfico animado
class GraficoAnimado(Static):
    barras = reactive([])
    n_barras = 10
    altura_max = 10
    async def on_mount(self):
        self.barras = [random.randint(1, self.altura_max) for _ in range(self.n_barras)]
        self.set_interval(0.5, self.atualiza_grafico)
    def atualiza_grafico(self):
        self.barras = [random.randint(1, self.altura_max) for _ in range(self.n_barras)]
        self.refresh()
    def render(self) -> str:
        linhas = []
        for h in range(self.altura_max, 0, -1):
            linha = ""
            for b in self.barras:
                linha += "█" if b >= h else " "
            linhas.append(linha)
        return "\n".join(linhas)

# Relógio digital
class Relogio(Static):
    hora = reactive("")
    async def on_mount(self):
        self.atualiza_hora()
        self.set_interval(1, self.atualiza_hora)
    def atualiza_hora(self):
        agora = datetime.datetime.now().strftime("%H:%M:%S")
        self.hora = agora
        self.refresh()
    def render(self) -> str:
        return f"\n    {self.hora}    \n"

# Letras caindo
class LetrasCaindo(Static):
    letras = reactive([])
    width = 40
    height = 10
    density = 0.08
    async def on_mount(self):
        self.letras = []
        self.set_interval(0.1, self.animate_letras)
    def animate_letras(self):
        self.update_letras()
        self.refresh()
    def update_letras(self):
        self.letras = [(x, y+1, ch) for (x, y, ch) in self.letras if y+1 < self.height]
        for x in range(self.width):
            if random.random() < self.density:
                ch = random.choice(string.ascii_uppercase)
                self.letras.append((x, 0, ch))
    def render(self) -> str:
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for x, y, ch in self.letras:
            grid[y][x] = ch
        return '\n'.join(''.join(row) for row in grid)

# Neve caindo
class Neve(Static):
    drops = reactive([])
    width = 40
    height = 10
    density = 0.05
    async def on_mount(self):
        self.drops = []
        self.set_interval(0.1, self.animate_rain)
    def animate_rain(self):
        self.update_rain()
        self.refresh()
    def update_rain(self):
        self.drops = [(x, y+1) for (x, y) in self.drops if y+1 < self.height]
        for x in range(self.width):
            if random.random() < self.density:
                self.drops.append((x, 0))
    def render(self) -> str:
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for x, y in self.drops:
            grid[y][x] = '❄'
        return '\n'.join(''.join(row) for row in grid)

class AnimacoesApp(App):
    CSS = """
    BolinhasLoading, QuadradoMovendo, BlocoColorido, GraficoAnimado, Relogio, LetrasCaindo, Neve {
        border: round white;
        margin: 1 2;
    }
    BolinhasLoading {
        width: 20;
        height: 3;
        color: magenta;
    }
    QuadradoMovendo {
        width: 20;
        height: 3;
        color: yellow;
    }
    BlocoColorido {
        width: 20;
        height: 3;
    }
    GraficoAnimado {
        width: 20;
        height: 12;
        color: green;
    }
    Relogio {
        width: 20;
        height: 5;
        color: cyan;
        background: black;
        border: round yellow;
    }
    LetrasCaindo, Neve {
        width: 40;
        height: 10;
    }
    """
    def compose(self) -> ComposeResult:
        yield Vertical(
            Horizontal(BolinhasLoading(), QuadradoMovendo(), BlocoColorido()),
            Horizontal(GraficoAnimado(), Relogio()),
            Horizontal(LetrasCaindo(), Neve()),
        )

if __name__ == "__main__":
    AnimacoesApp().run()
