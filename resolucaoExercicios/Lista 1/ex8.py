#Resolução do exercicio 8 da lista 1

salarioBase = 2500
maxHoras = 200
salarioHora = salarioBase / maxHoras
horaExtra = 20 /100
salarioHoraAdicional = salarioHora + salarioHora * horaExtra
qtdHoras = float(input("Digite a quantidade de horas trabalhadas: "))


if qtdHoras <= 200:
    salarioBruto = salarioHora * qtdHoras
    impostoRenda = salarioBruto * 0.13
    inss = salarioBruto * 0.09
    salarioLiquido = salarioBruto - impostoRenda - inss

else:
    salarioBruto = salarioHora * 200
    qtdHoras -= 200
    salarioBruto = salarioBruto + (salarioHoraAdicional * qtdHoras)
    impostoRenda = salarioBruto * 0.13
    inss = salarioBruto * 0.09
    salarioLiquido = salarioBruto - impostoRenda - inss

print(f"""
Salario Bruto: {salarioBruto}
Imposto de Renda(13%): {impostoRenda}
INSS(9%): {inss}
Salario Liquido: {salarioLiquido}
""")