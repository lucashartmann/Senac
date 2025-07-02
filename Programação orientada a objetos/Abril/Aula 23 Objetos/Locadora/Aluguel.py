class Aluguel:

    def __init__(self):
       self.lista_midias = []
       data_retirada = data_retirada
       prazo = prazo
    
    def alugar_filme():
        filmesAlugados = []
        quant = int(input("Quantos filmes voce deseja"))
        # Prazo
        # Data Retirada
       

    def alugar_filme2(lista_midias, data_retirada, prazo):
        for i in range(quant):
            nome = input("Digite o nome dos filmes que deseja: ")
            if(acervo.consultaPorNome(nome)):
                filme = acervo.consultaPorNome(nome)
                filmesAlugados.append(filme)
                acervo.remove(filme)
                i = i + 1
                return True
        return False
