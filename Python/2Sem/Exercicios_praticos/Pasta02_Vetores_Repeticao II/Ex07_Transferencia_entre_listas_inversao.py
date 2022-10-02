''''
Faça um programa que receba dez números e armazene em uma lista. 
Em seguida copie todos os números da primeira lista para uma segunda lista, mas na ordem invertida da primeira lista.
'''

lista_a = [0] * 10
lista_b = [0] * 10

for i in range(len(lista_a)):
    num = int(input('Digite um número inteiro: '))
    if num >= 0:
        lista_a[i] = num
for i in range(10):
  lista_b[(len(lista_a)-1) - i] = lista_a[i]

print(lista_a)
print(lista_b)