import os
import sys
import venv
import subprocess

try:
    nome_diretorio = sys.argv[1]  # python .\Setup.py [nome_do_diretorio]
except IndexError:
    print("Faltou parâmetros [python .\\Setup.py [nome_diretorio]]")
    nome_diretorio = input("Digite o nome da pasta: ")

try:
    os.mkdir(nome_diretorio)
    venv.create(f"{nome_diretorio}/.venv", with_pip=True)
    pip_path = os.path.join(nome_diretorio, ".venv", "Scripts", "python.exe")
    subprocess.run([
        pip_path, "-m", "pip", "install", "textual"
    ], check=True)

except FileExistsError:
    print("Diretorio já existe")
