def desenhar_mapa(x, y):
    x = int(x / 2) + (x % 2)
    y = int(y / 2) + (y % 2)
    for i in range(y):
        for l in range(x):
            print("[#][ ]", end="")
            l = l + 1
        print()
        for j in range(x):
            print("[ ][#]", end="")
            j = j + 1
        print("", end="\n")
        i = i + 1


def desenhar_mapa2(x, y):
    x = int(x / 2) + (x % 2) 
    x2 = x - 1
    y = int(y/2) + (y % 2)
    for i in range(y):
        for l in range(x):
            print("[#] ", end="  ")
            l = l + 1
        print()
        for j in range(x2):
            print("   [#]", end="")
            j = j + 1
        print("", end="\n")
        i = i + 1
       

desenhar_mapa2(9, 7)