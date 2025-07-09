import shelve 

meus_dados = shelve.open('dados', writeback=True)

meus_dados["compras"] = []

meus_dados["compras"]

meus_dados["compras"].append("maça")

meus_dados["compras"].append("laranja")

meus_dados["compras"]

meus_dados.close()
