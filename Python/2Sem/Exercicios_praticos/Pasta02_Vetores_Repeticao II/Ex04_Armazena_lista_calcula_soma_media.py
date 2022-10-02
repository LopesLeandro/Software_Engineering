'''
Faça um programa que receba dez números e armazene em uma lista. Em seguida calcule a soma de todos os números percorrendo novamente a lista. Apresente a soma e em seguida a média baseada na soma e no número de números armazenados.
'''

lista = []
sum = 0

qnt = int(input('Quantos números quer calcular? \t'))
for i in range(qnt):
    num = int(input('Digite um número: \t'))
    lista.append(num)

for j in range(len(lista)):
    sum += lista[j]

media = sum / len(lista)

print('A soma: ', sum)
print('A média: ', media)