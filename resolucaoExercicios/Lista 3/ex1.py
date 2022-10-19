#Resolução do exercicio 1 da lista 3

msg = "digite o lado do triangulo: "
l1 = input(msg)
l2 = input(msg)
l3 = input(msg)

equilatero = l1 == l2 == l3
isoceles = (l1 == l2 != l3) or (l2 == l3 != l1) or (l1 == l3 != l2)
escaleno = l1 != l2 != l3

if equilatero:
    print('Esse é um triangulo equilátero')
elif isoceles:
    print('Esse é um triangulo isósceles')
elif escaleno:
    print('Esse é um triangulo escaleno ')

