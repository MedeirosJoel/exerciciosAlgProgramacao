#Resolução do exercicio 4 da lista 2

ano = int(input("Digite o ano: "))

if ano%400 == 0 or (ano%4 == 0 and ano%100 != 0):
    print(True)

else:
    print(False)