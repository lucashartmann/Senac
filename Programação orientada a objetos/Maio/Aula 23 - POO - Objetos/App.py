from Comandante import Comandante
from Vaca import Vaca
from DiscoVoador import DiscoVoador


vaca1 = Vaca("Rosimery")
vaca2 = Vaca("Rosangela")
zorg = Comandante()
zorg.perseguir_ofensivamente(vaca1)
zorg.perseguir_sorrateiramente(vaca2)
zorg.relatorio()
