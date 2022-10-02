#PROVA LEANDRO LOPES EM 26/05/2022

linhas = 3
turnos = 2
totalprod = 0
maior = 0
linhamaior = 0
totalturno1 = 0
totalturno2 = 0

for lin in range(linhas):
    print("Linha:", lin+1)
    for turno in range(turnos+1):
        print("Turno:", turno)
        codigo = int(input("Digite o código: "))
        qtdproduzida = int(input("Digite a quantidade produzida: "))
        qtddescartada = int(input("Digite a quantidade descartada: "))
        totalprod += qtdproduzida
        if turno == 1:
            totalturno1 += qtddescartada
        else:
            totalturno2 += qtddescartada
        if codigo == 2:
            if qtddescartada >= 100:
                print("Normal")
            else:
                print("Irregular")
        else:
            if qtddescartada >=50:
                print("Irregular")
            else:
                print("Normal")


    if totalprod > maior:
        maior = totalprod
        linhamaior = lin
    #aqui1

print("A linha ", linhamaior, "tem a maior quantidade de ", maior)
print("O total do turno 1: ", totalturno1)
print("O total do turno 2: ", totalturno2)
