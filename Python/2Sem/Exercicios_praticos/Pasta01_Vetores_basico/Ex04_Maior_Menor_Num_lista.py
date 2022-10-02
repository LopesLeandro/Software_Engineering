# Faça um programa que receba dez números e armazene em uma lista.
# Em seguida percorra toda a lista e procure qual o MAIOR valor dentro da lista e qual o MENOR valor dentro da lista.
# No final apresente o MAIOR e o MENOR valor.

lista = [""] * 10
maior = 0
rodada = 0

for i in range(10):
    lista[i] = int(input('Digite um número: '))

for n in range(10):
    if lista[n] > maior:
        maior = lista[n]
    if rodada == 0:
        menor = lista[n]
    if lista[n] < menor:
        menor = lista[n]
    rodada += 1

print('Maior valor: ', maior)
print('Menor valor: ', menor)