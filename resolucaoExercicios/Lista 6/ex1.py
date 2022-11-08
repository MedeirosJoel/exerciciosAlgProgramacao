# Resolução do exercicio 1 da lista 6

n = int(input())

anterior = 1
atual = None
for numero in range(1, n):
    
    if atual == None:
        atual = 1
    else:
        temp = atual
        atual = atual +anterior
        anterior = temp
    
    #Esse print serve para visualizar os passos de fibonacci
    #print(f'Atual {atual}, Anterior {anterior}')

print(atual)
