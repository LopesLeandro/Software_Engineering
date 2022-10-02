'''
Faça um programa que receba dez números e armazene em uma lista. 
Em seguida percorra toda a lista e procure qual o MAIOR valor dentro da lista e qual o MENOR valor dentro da lista. 
No final apresente o MAIOR e o MENOR valor.
'''

lista = []
maior = 0
menor = 999

for i in range(10):
    num = int(input('Digite um número: '))
    lista.append(num)
for j in range(10):
    if lista[j] > maior:
        maior = lista[j]
    if lista[j] < menor:
        menor = lista[j]
print('Maior: ', maior)
print('Menor: ', menor)