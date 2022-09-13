#Resolução do exercicio 7 da lista 1

capital = float(input("Digite o valor investido: "))
meses = int(input("Digite a quantidade de meses: "))
taxa = float(input("Digite a taxa: "))

taxa = taxa/100

resultante = capital*(1+taxa)**meses

print(resultante)