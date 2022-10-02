# Faça um programa que receba dez números e armazene em uma lista.
# Em seguida conte quantos números são impar e quantos são par.
# Apresente os contadores na tela.

lista = [0] * 10
impar = 0
par = 0

for i in range(10):
    lista[i] = int(input('Digite um número: '))
    if lista[i] % 2 != 0:
        impar += 1
    else:
        par += 1

print('Lista: ', lista)
print('Impares: ', impar)
print('Pares: ', par)