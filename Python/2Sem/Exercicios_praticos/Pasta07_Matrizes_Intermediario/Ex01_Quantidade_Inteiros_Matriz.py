''''
1)	Faça um programa que carregue uma matriz 3x5 com números inteiros, calcule e mostre a quantidade de elementos entre 15 e 20.
'''

tab = [[0] * 3 for i in range(5)]
contador = 9
elementos = 0
elementos_string = []

for lin in range(5):
    for col in range(3):
        tab[lin][col] = contador
        if tab[lin][col] > 14 and tab[lin][col] < 21:
            elementos += 1
            elementos_string.append(tab[lin][col])
        print(tab[lin][col], end=" \t")
        contador += 1
    print()

print('Temos um total de ', elementos, 'elementos entre 15 e 20.')
print('Os elementos entre 15 e 20 são: ', elementos_string)