# Resolução do exercicio 7 da lista 3

comprimento = float(input('Digite o comprimento da mesa(m): '))
largura = float(input('Digite a largura da mesa(m): '))
gavetas = int(input('Digite o numero de gavetas da mesa: '))
madeira = input('Digite o nome da madeira utilizada: ')

metro_quadrado = largura * comprimento

preco_metro = metro_quadrado * 100

preco_metro += 50 if metro_quadrado > 2 else 0

preco_gavetas = gavetas * 30

if madeira == 'mogno':
    preco_madeira = 150

elif madeira == 'carvalho':
    preco_madeira = 125

else:
    preco_madeira = 0

preco_final = preco_metro + preco_gavetas + preco_madeira

preco_final = 200 if preco_final < 200 else preco_final

print('O preço da mesa é: '+str(preco_final))
