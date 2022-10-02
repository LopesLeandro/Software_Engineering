"""
3)	Dada a seguinte matriz, calcule:
- A soma dos elementos de primeira coluna;
- O produto dos elementos da primeira linha;
- A soma de todos os elementos;
- O produto da diagonal principal.
1	2	3	4
5	6	7	8
9	10	11	12
13	14	15	16
"""
matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#contador = 1
#for lin in range(4):
#    for col in range(4):
#        matriz[lin][col] = contador
#        contador+=1

#A soma dos elementos de primeira coluna;
#soma = matriz[0][0] + matriz[1][0] + matriz[2][0] + matriz[3][0]
soma = 0
for lin in range(4):
    soma += matriz[lin][0]
print("A soma dos elementos da primeira coluna e ", soma)

#O produto dos elementos da primeira linha;
prod = 1
for col in range(4):
    #prod = prod * matriz[0][col]
    prod *= matriz[0][col]
print("O produto e ", prod)

#A soma de todos os elementos;
somatudo = 0
for lin in range(4):
    for col in range(4):
        somatudo += matriz[lin][col]
print("Soma de todos os valores ", somatudo)

"""
- O produto da diagonal principal.
1	-	-	-
-	6	-	-
-	-	11	-
-	-	-	16
"""
proddiag = 1
for i in range(4):
    proddiag *= matriz[i][i]
print("O produto da diagonal principal e ", proddiag)