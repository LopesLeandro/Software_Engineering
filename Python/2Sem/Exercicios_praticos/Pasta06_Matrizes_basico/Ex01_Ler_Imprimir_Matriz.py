''''
1)	Faça um programa para ler e imprimir uma matriz 2 por 4 de números inteiros.
linhas 2
Colunas 3
'''

lista = [[0] * 4 for i in range(2)]
contador = 1
for lin in range(2):
    for col in range(4):
        lista[lin][col] = contador
        print(lista[lin][col], end=" ") 
        contador += 1 
    print('\n')