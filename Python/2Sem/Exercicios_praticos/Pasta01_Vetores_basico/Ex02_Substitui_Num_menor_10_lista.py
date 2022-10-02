#Faça um programa que receba dez números e armazene em uma lista.
#Em seguida, substitua todos os números cujo valor seja menor que 10 pelo valor ZERO.
#Imprima a lista em tela.

lista = [0] * 10

for i in range(10):
  lista[i] = int(input('Digite um número: '))
  if lista[i] < 10:
    lista[i] = 0
print('Lista sem menores de 10: ', lista)