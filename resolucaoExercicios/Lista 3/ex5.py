# Resolução do exercicio 5 da lista 3

salario_bruto = input('Digite o valor do salario bruto: ')

salario_bruto = float(salario_bruto)

if salario_bruto <= 720.00:
    valor_inss = salario_bruto * 0.0765

elif salario_bruto <= 1200.00:
    valor_inss = salario_bruto * 0.09

elif salario_bruto <= 2400.00:
    valor_inss = salario_bruto * 0.11

elif salario_bruto >= 2400.00:
    valor_inss = 2400.00 * 0.11

# Você sabia que utilizar a barra ao contrario \
# permite que você quebre um comando em mais de uma linha

print(f'O seu salario bruto é: {salario_bruto}, \
e o valor da seguiridade é: {valor_inss}')
