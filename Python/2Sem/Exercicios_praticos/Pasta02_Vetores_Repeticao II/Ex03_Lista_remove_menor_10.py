'''
Faça um programa que receba dez números e armazene em uma lista. Em seguida, substitua todos os números cujo valor seja menor que 10 pelo valor ZERO. Imprima a lista em tela.
'''

lista = []

for i in range(10):
  num = int(input('Digite um número: '))
  if num < 10:
    pass
  else:
    lista.append(num)  

print('Lista sem menores de 10: ', lista)