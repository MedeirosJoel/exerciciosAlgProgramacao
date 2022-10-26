import os

qtdExercicios = [9, 8, 15, 4, 15, 1, 7, 1, 2, 11]

os.mkdir('./resolucaoExercicios/')

for lista in range(0,10):
    os.mkdir(f'./resolucaoExercicios/Lista {lista+1}')
    
    for exercicio in range(qtdExercicios[lista]):
        filepatch = f'./resolucaoExercicios/Lista {lista+1}/ex{exercicio+1}.py'
        file = open(filepatch, 'w+', encoding='UTF8')
        file.write(f'# Resolução do exercicio {exercicio+1} da lista {lista+1}')
        file.close()

