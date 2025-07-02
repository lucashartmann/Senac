class Tabuleiro:
    def __init__(self, linhas, colunas):
        self.tabuleiro = Tabuleiro.gerar_tabuleiro(self, linhas, colunas)

    def gerar_tabuleiro(self, linhas, colunas):
        tabuleiro = []
        for numero_linha in range(linhas):
            l = ['#' for i in range(colunas)]
            if numero_linha %2 == 0:
                for index in range(0,len(l),2):
                    l[index] = ' '       
            else:
                for index in range(1,len(l),2):
                    l[index] = ' '
            tabuleiro.append(l)
        return tabuleiro

    def posicionar_peca(self, peca, linha, coluna):
        self.tabuleiro[linha-1][coluna-1] = peca
        return True
    
    def mover_peca(self):
        pass

    def get_peca(self, linha, coluna):
        posicao = self.tabuleiro[linha-1][coluna-1]
        if posicao:
            return posicao
        return None

    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            for valor in linha:
                print(valor, end=" ")
            print()

tabuleiro1 = Tabuleiro(5, 5)
tabuleiro1.posicionar_peca("@", 1, 3)
print(tabuleiro1.get_peca(1, 3))
tabuleiro1.imprimir_tabuleiro()