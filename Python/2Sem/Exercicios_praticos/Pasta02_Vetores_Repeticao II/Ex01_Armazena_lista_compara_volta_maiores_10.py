'''1)	Faça um programa que receba dez números e armazene em uma lista. Em seguida percorra toda a lista mostrando apenas os números que cujo valor seja superior a 10.'''

lista = []
lista_maiores = []
contador = 0
c = 0

while c != 'n' and c != 'N':
    num = int(input('Digite um número: '))
    lista.append(num)
    print('Continuar? \n S - Sim \t  N - Não')
    c = str(input())

for j in range(len(lista)):
    if lista[j] > 10:
        lista_maiores.append(lista[j])
    contador += 1
    
print('Lista maiores que 10: ', lista_maiores)
