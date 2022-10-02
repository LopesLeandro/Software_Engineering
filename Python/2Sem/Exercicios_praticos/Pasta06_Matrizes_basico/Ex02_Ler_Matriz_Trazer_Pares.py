'''
2)	Ler uma matriz A de duas dimensões com 7 linhas e 7 colunas. Ao final apresentar o total de elementos pares existentes dentro da matriz.
'''
import random
from datetime import datetime
lista = [[0] * 7 for i in range(7)]
pares = []
contador_par = 0

for lin in range(7):
    random.seed(datetime.now())
    for col in range(7):
        #lista[lin][col] = int(random.random() * 100)
        lista[lin][col] = int(random.random() * 100)
        print(lista[lin][col], end=" \t")
        
        if lista[lin][col] % 2 == 0:
            num_z = lista[lin][col]
            pares.append(num_z)
            contador_par += 1
    print()

print('Estes são os números pares: ', pares)
print('O total de números pares é: ', contador_par)