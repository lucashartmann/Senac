import shelve 

dados = shelve.open("dados")
print(dados["compras"])

