@echo off
python agenda.py cadastrar srx@email.com "Senhor Xis" 20, "Rua do srx"
python agenda.py cadastrar srb@email.com "Senhor B" 21, "Rua do srb"
python agenda.py cadastrar srz@email.com "Senhor Z" 22, "Rua do srz"
python agenda.py cadastrar sra@email.com "Senhora A" 23, "Rua do sra"

python agenda.py listar
python agenda.py consultar srx@email.com
python agenda.py favoritar sry@email.com