''''
Faça um programa que carregue dois vetores de dez elementos numéricos cada um e mostre um vetor resultante da intercalação desses dois vetores.
'''

lista_a = [1,3,5,7,9,11,13,15,17,19]
lista_b = [2,4,6,8,10,12,14,16,18,20]
lista_agrupada = []

for i in range(10):
    lista_agrupada.append(lista_a[i])
    lista_agrupada.append(lista_b[i])


print(lista_agrupada)