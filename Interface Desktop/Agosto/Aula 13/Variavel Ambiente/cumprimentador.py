import os

nome = os.getenv("NOME") 
print(f"Olá, {nome}")
os.environ['CUMPRIMENTOU'] = True
