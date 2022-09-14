#Resolução do exercicio 2 da lista 2

aprovacao = 6

nota1 = float(input("Digite a nota 1: "))
peso1 = float(input("Digite o peso da nota 1: "))

nota2 = float(input("Digite a nota 2: "))
peso2 = float(input("Digite o peso da nota 2: "))

nota3 = float(input("Digite a nota 3: "))
peso3 = float(input("Digite o peso da nota 3: "))

notaTotal = (nota1*peso1) + (nota2*peso2) + (nota3*peso3)

if notaTotal >= 6:
    print(True)

else:
    print(False)