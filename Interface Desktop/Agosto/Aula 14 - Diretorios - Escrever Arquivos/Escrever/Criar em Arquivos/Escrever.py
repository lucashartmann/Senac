with open('exemplo.txt', 'w') as arquivo:
    arquivo.write('Primeira linha\n')
    arquivo.write('Segunda linha\n')

with open('exemplo.txt', 'a') as arquivo:
    arquivo.write('Primeira linha\n')
    arquivo.write('Segunda linha\n')
