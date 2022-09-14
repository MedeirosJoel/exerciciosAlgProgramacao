#Resolução do exercicio 5 da lista 2

xAtual = int(input("Digite o X atual: "))
yAtual = int(input("Digite o Y atual: "))
xPretendido = int(input("Digite o X pretendido: "))
yPretendido = int(input("Digite o Y pretendido: "))

if (
    ((xPretendido == xAtual+1 or xPretendido == xAtual-1) and 
    (yPretendido == yAtual+2 or yPretendido == yAtual-2)) 
    or
    ((xPretendido == xAtual+2 or xPretendido == xAtual-2) and
    (yPretendido == yAtual+1 or yPretendido == yAtual-1))
    and 
    xPretendido <=8 and yPretendido<=8):
    
    print(True)

else:
    print(False)
