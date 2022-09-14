#Resolução do exercicio 6 da lista 2

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if (a < b + c and b < a + c and c < b + c):
    print(True)

else:
    print(False)
