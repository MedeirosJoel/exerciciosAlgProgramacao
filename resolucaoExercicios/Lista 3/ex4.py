# Resolução do exercicio 4 da lista 3

n1 = float(input('Digite a nota 1'))
n2 = float(input('Digite a nota 2'))
n3 = float(input('Digite a nota 3'))

soma = n1 + n2 + n3
media = soma / 3
conceito = None

# ! Tente refatorar esse codigo e deixa-lo mais legivel

if media > 6:

    if media > 7.5:

        if media > 9:
            conceito = 'Ótimo'

        else:
            conceito = 'Bom'

    else:
        conceito = 'Satisfatorio'

else:
    conceito = 'Insuficiente'
