#Resolução do exercicio 5 da lista 1

raio = float(input("Digite o raio do Circulo: "))
#DICA - é possivel importar o pi diretamente da biblioteca math do python
#from math import pi, a linha abaixo não seria necessaria 
pi = 3.1415926535898

area = pi * (raio ** 2)

print(f"A area do circulo que tem raio de {raio} é de: {area}")