class Vaca:
    def __init__(self, nome):
        self.nome = nome

    def mugir(self):
        print(f"{self.nome}: Muuuuuu")

    def __str__(self):
        return f"Nome = {self.nome}"
