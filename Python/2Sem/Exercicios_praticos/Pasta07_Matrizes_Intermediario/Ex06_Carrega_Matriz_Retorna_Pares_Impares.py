''''
6)	Faça um programa que carregue uma matriz 3 x 4, calcule e mostre:

a.	A quantidade de elementos pares
b.	A soma dos elementos ímpares
c.	A média de todos os elementos
'''

table = [[0] * 4 for i in range(3)]
contador = 1
pares = 0
impares = 0
media = 0
#Constroi a matriz
for lin in range(3):
    for col in range(4):
    #    table[lin][col] = int(input(f'Digite o valor da posição [{lin+1}][{col+1}]: '))
        table[lin][col] = contador
        contador += 1
        if table[lin][col] % 2 == 0:
            pares += 1
        else:
            impares += 1
        media += table[lin][col]

for lin in range(3):
    for col in range(4):
        print(table[lin][col], end=' \t')
    print()

print(f'A quantidade de elementos pares é: {pares}')
print(f'A soma dos elementos ímpares é: {impares}') 
print(f'A média de todos os elementos é: {media/(contador-1)}')
