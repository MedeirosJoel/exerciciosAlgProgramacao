#Resolução do exercicio 8 da lista 2

preco_km = 0.5
preco_diaria = 45

km_rodados = input('Digite a quantidade de Km rodados: ')
diarias = input('Digite a quantidade de dias de locação: ')

preco_final = float(km_rodados) * preco_km + float(diarias) * preco_diaria

print(f'O preço final da locação é: R$ {preco_final}')