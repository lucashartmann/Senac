def put_item(item, coluna, linha):
    mapa[linha-1][coluna-1] = item
    return True


def get_item(coluna, linha):
    return mapa[linha-1][coluna-1]


def criar_mapa(x, y):

    mapa = []

    linha = ["#", "x", "#"]
    linha2 = ["x", "#", "x"]

    if len(linha) < x:
        for tamanho_lista in range(x):
            tamanho_lista = len(linha)
            quant_elementos_faltantes = x - tamanho_lista
            linha += linha[0:quant_elementos_faltantes]
            linha2 += linha2[0:quant_elementos_faltantes]
            if tamanho_lista == x:
                break

    elif len(linha) > x:
        linha = linha[0:x]
        linha2 = linha2[0:x]

    for i in range(y):
        if i % 2 == 0:
            mapa.append(linha)
        else:
            mapa.append(linha2)

    for linha in mapa:
        for valor in linha:
            print(valor, end=" ")
        print()


x = 6
y = 4

criar_mapa(x, y)


# put_item("@", 3, 1)
# imprimir_tabuleiro()
