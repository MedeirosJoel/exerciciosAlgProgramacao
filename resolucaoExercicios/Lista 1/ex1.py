# Resolução do exercicio 1 da lista 1

from datetime import datetime


anoAtual = 2022

#DICA - é possivel usar o datetime para adquirir a data atual, tire o comentario das linhas abaixo para sobrescrever

#from datetime import datetime
#anoAtual = datetime.today().year

diaNascimento = int(input("Digite o dia em que você nasceu: "))
mesNascimento = int(input("Digite o mês do seu nascimento: "))
anoNascimento = int(input("Digite o ano em que nasceu: "))

print("a sua idade é de: ", anoAtual-anoNascimento)
