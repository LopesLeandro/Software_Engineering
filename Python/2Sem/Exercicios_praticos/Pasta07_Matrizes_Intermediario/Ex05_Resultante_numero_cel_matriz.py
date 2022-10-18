''''
5)	Faça um programa que carregue uma matriz 3 x 3 com números reais e receba um valor, número digitado pelo usuário, calcule e mostre a matriz resultante da multiplicação do número digitado por elemento da matriz.
'''

table = [[0] * 3 for i in range(3)]
resultado = [[0] * 3 for i in range(3)]
#Constroi a matriz
casa = 0
for lin in range(3):
    for col in range(3):
        casa += 1
        table[lin][col] = int(input(f'Digite o valor da posição [{lin+1}][{col+1}]: '))
        resultado[lin][col] = table[lin][col] * casa

for lin in range(3):
    for col in range(3):
        print(table[lin][col], end=' \t')
    print()

#print(f'O resultado da multiplicação dos valores pela posição é: {resultado}')
print('A matriz resultante multiplicando posição por valor é: ')
for lin in range(3):
    for col in range(3):
        print(f'{resultado[lin][col]:^5}', end=' \t')
    print()
    