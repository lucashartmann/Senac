from Comandante import Comandante
from Vaca import Vaca
cena = {}
zorg = Comandante()
comando = ""
while comando != "sair":
    comando = input("Comando: ").split
    match comando:
        case ["criar vaca", nome]:
            vaca = Vaca(nome)
            cena[nome] = vaca
        case ["comandante", "perseguir", "ofensivamente", nome_vaca]:
            zorg.perseguir_ofensivamente(cena[nome_vaca])
        case ["comandante", "perseguir", "sorrateiramente", nome_vaca]:
            zorg.perseguir_sorrateiramente(cena[nome_vaca])
        case ["comandante", 'relatorio']:
            zorg.relatorio()
        case ['sair']:
            comando = "sair"
