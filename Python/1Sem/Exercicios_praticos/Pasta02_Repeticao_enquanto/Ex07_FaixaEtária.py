#REPENQ7) Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:
#- A quantidade de pessoas em cada faixa etária
#- A percentagem de pessoas em cada uma das faixas etárias, com relação ao total de pessoas, de acordo com a tabela abaixo:
#Faixa Etária	Idade
#1	Até 15 anos
#2	De 16 a 30 anos
#3	De 31 a 45 anos
#4	De 46 a 60 anos
#5	Acima de 61 anos

faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0
faixainv = 0
pessoa = 0
total = 15

for pessoa in range(15):
    idade = int(input("Qual a sua idade:"))
    if idade <= 15:
        faixa1 += 1
        percentual1 = (faixa1 / total)*100
    else:
        if idade > 15 and idade <= 30:
            faixa2 += 1
            percentual2 = (faixa2 / total) * 100
        else:
            if idade > 30 and idade <=45:
                faixa3 += 1
                percentual3 = (faixa3 / total) * 100
            else:
                if idade > 45 and idade <=60:
                    faixa4 += 1
                    percentual4 = (faixa4 / total) * 100
                else:
                    if idade > 60 and idade < 150:
                        faixa5 += 1
                        percentual5 = (faixa5 / total) * 100
                    else:
                        print("Idade inválida")
                        faixainv += 1

#imprime a tabela
print("Faixa etária 1:", faixa1, " pessoas, no qual representa %.0f" %percentual1, "%.")
print("Faixa etária 2:", faixa2, " pessoas, no qual representa %.0f" %percentual2, "%.")
print("Faixa etária 3:", faixa3, " pessoas, no qual representa %.0f" %percentual3, "%.")
print("Faixa etária 4:", faixa4, " pessoas, no qual representa %.0f" %percentual4, "%.")
print("Faixa etária 5:", faixa5, " pessoas, no qual representa %.0f" %percentual5, "%.")
print("Foram registrados ", faixainv, " idades inválidas, no qual representa %.0f" %percentual5, "%.")


# SOLUÇÃO DO PROFESSOR
#contaf1 = 0
#contaf2 = 0
#contaf3 = 0
#contaf4 = 0
#contaf5 = 0
#for pessoa in range(15):
#    print("Pessoa ", pessoa+1)
#    print("Digite a idade")
#    idade = int(input())
#    if idade <= 15:
#        contaf1 += 1 #contaf1 = contaf1 + 1
#    else:
#        if idade >= 16 and idade <= 30:
#            contaf2 += 1
#        else:
#            if idade >= 31 and idade <= 45:
#                contaf3 += 1
#            else:
#                if idade >= 46 and idade <= 60:
#                    contaf4 += 1
#                else:
#                    contaf5+=1
#fim for 15
#  15      100%
# contaf1   perc
#percf1 = contaf1 * 100 / 15
#print("Qtd faixa 1 ", contaf1, " com perc de ", percf1)
#percf2 = contaf2 * 100 / 15
#print("Qtd faixa 2 ", contaf2, " com perc de ", percf2)
#percf3 = contaf3 * 100 / 15
#print("Qtd faixa 3 ", contaf3, " com perc de ", percf3)
#percf4 = contaf4 * 100 / 15
#print("Qtd faixa 4 ", contaf4, " com perc de ", percf4)
#percf5 = contaf5 * 100 / 15
#print("Qtd faixa 5 ", contaf5, " com perc de ", percf5)
