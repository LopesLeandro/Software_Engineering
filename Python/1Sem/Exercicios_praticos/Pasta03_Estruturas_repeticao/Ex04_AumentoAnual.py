#4) Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que:
#a) esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#b) em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#c) a partir de 1997 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
#Faça um programa que determine o salário atual desse funcionário.

salario = 1000.00
percentual = 0.015
i = 1995

for i in range(1995,2023):
    if i == 1995:
        print("Ano: ", i, "Salário inicial: ", salario)
    else:
        salario = (salario * percentual) + salario
        print("Ano: ", i, "Percentual: %.2f" % percentual, "Salário: %.2f" % salario)
        percentual = percentual * 2