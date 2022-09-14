#Resolução do exercicio 3 da lista 2

volumeGalao = 3.6
valorGalao = 25.00
areaGalao = 18

areaCliente = int(input("Digite a area a ser pintada: "))

multiplicador = round(areaCliente / areaGalao)
if multiplicador == 0:
    print(f"""
    Área de cobertura: {areaCliente}
    Número de galões: 1, {volumeGalao} litros
    valor a ser pago: R$: {valorGalao}
    """)
else:
    print(f"""
    Área de cobertura: {areaCliente}
    Número de galões: {multiplicador}, {volumeGalao * multiplicador} litros
    valor a ser pago: R$: {valorGalao*multiplicador}
    """)