# Faça um programa que receba dez números e armazene em uma lista.
# Em seguida copie todos os números da primeira lista para uma segunda lista, mas na ordem invertida da primeira lista.

lista_a = [0] * 10
lista_b = [0] * 10

for i in range(len(lista_a)):
    num = int(input('Digite um número inteiro: '))
    if num >= 0:
        lista_a[i] = num

for i in range(len(lista_a)):
  lista_b[(len(lista_a)-1) - i] = lista_a[i]
'''
cont = len(lista_a)
for j in range(len(lista_a)):
    lista_b[cont - 1] = lista_a[j]
    cont -= 1
'''
print(lista_b)

'''
CORREÇÃO

lista = [0] * 10
listaInv = [0] * 10

for i in range(10):
  print("Digite um número")
  lista[i] = int(input())

FORMA 1
cont = 9
for i in range(10):
  listaInv[cont] = lista[i]
  cont -= 1


FORMA 2
for i in range(10):
  listaInv[(len(lista)-1) - i] = lista[i]


#A função len() retorna o número de itens em um objeto. Quando o objeto é uma sequência, a função len() retorna o número de caracteres na sequência.


(len(10) - 1 ) - i o i nesse caso começa do 0 e vai até o 9, o len vai puxar 10 casas, porém o 10 está fora do tamanho da lista, ai pegamos o 10, diminuimos 1 e vamos diminiundo do i, que começa do zero e vai até o 9, conforme exemplo a baixo

PRIMEIRO
(10 - 1 ) - 0
(9) - 0
9

SEGUNDO
(10 - 1 ) - 1
(9) - 1
8

TERCEIRO
(10 - 1 ) - 2
(9) - 2
7

FORMA 3

for i in range(10):
  listaInv[i] = lista.pop()


print(listaInv)
'''