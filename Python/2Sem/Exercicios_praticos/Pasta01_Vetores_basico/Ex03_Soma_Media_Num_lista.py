#Faça um programa que receba dez números e armazene em uma lista.
#Em seguida calcule a soma de todos os números percorrendo novamente a lista.
#Apresente a soma e em seguida a média baseada na soma e no número de números armazenados.

lista = [0] * 10
soma = 0

for i in range(10):
  lista[i] = int(input('Digite um número: '))

for c in range(10):
  soma += lista[c]

med = soma / 10

print('Lista: ', lista)
print('Soma da lista: ', soma)
print('Média da lista: ', med)