"""
2)	Ler uma matriz A de duas dimensões 
com 7 linhas e 7 colunas. Ao final 
apresentar o total de elementos pares 
existentes dentro da matriz.
"""
import random
from datetime import datetime
matriz = [[0] * 7 for i in range(7)]
random.seed(datetime.now())
for lin in range(7):
    for col in range(7):
        print("Digite um numero")
        #matriz[lin][col] = int(input())
        matriz[lin][col] = int(random.random() * 100)
        print(matriz[lin][col])

contapar = 0
for lin in range(7):
    for col in range(7):
        if matriz[lin][col] % 2 == 0:
            contapar +=1

print("O numero total de pares e: ", contapar)