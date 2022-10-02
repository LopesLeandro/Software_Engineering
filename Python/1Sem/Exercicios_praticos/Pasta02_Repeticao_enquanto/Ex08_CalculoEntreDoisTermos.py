#REPENQ8) Faça um algoritmo que leia o número de termos, determine e mostre os valores de acordo com a série abaixo:
#Série = 2,7,3,4,21,12,8,63,48,16,189,192,32,567,768,64,...

#2 3 4
cont = 0
termoa = 2
termob = 7
termoc = 3

while cont != 50:
    termoa = termoa * 2
    termob = termob * 3
    termoc = termoc * 4
    cont += 1
    print(termoa, termob, termoc)