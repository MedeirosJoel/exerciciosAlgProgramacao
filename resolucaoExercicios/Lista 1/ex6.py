#Resolução do exercicio 6 da lista 1

prestracao = float(input("Digite o valor da prestração: "))
taxaMensal = float(input("Digite a taxa mensal: "))
qtdPrestracoes = int(input("Digite a quantidade de prestrações: "))

#para transformar uma porcentagem em decimal multiplo se divide a porcentagem por 100
taxaMensal = taxaMensal/100

# Em operações muito complexas você pode separar partes das contas em grandezas
linha1 = (1+taxaMensal)**qtdPrestracoes - 1
linha2 = taxaMensal*(1+taxaMensal)**qtdPrestracoes


valorPresente = prestracao * (linha1/linha2)
print(valorPresente)