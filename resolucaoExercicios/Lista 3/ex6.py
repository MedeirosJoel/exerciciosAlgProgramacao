# Resolução do exercicio 6 da lista 3

num1 = input('Digite o numero 1: ')
num2 = input('Digite o numero 2: ')
num3 = input('Digite o numero 3: ')

if num1 > num2 and num1 > num3:
    print('o numero', num1, 'é o maior numero')

else:

    if num2 > num1 and num2 > num3:
        print('o numero', num2, 'é o maior numero')

    else:
        if num3 > num1 and num3 > num2:
            print('o numero', num3, 'é o maior numero')

        else:
            print('erro!')
