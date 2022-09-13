#Resolução do exercicio 9 da lista 1

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (b**2) - 4 * a * c

x1 = (-b + delta ** (1 / 2)) / (2 * a)
x2 = (-b - delta ** (1 / 2)) / (2 * a)
        

print("As raizes da equação são: x1: {}, x2: {}".format(x1, x2))