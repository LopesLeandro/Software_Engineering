'''
Faça um programa que receba dez números e armazene em uma lista. Em seguida conte quantos números são impar e quantos são par. Apresente os contadores na tela.
'''

lista = []
lista_impares = []
lista_pares = []
c = 0

while c != 'n' and c != 'N':
    num = int(input('Digite um número: '))
    lista.append(num)
    print('Continuar? \n S - Sim \t  N - Não')
    c = str(input())

for j in range(len(lista)):
    if lista[j] % 2 == 0:
        lista_pares.append(lista[j])
    else:
        lista_impares.append(lista[j])
    
    
print('Lista pares: ', lista_pares)
print('Lista impares: ', lista_impares)