# 5)	Faça um programa que receba dez números e armazene em uma lista.
# Em seguida solicite um outro número e armazene em uma variável chamada multiplicador.
# Percorra toda a lista e multiplique cada número pelo multiplicador e apresente em tela.

lista = [''] * 10

for i in range(10):
    lista[i] = int(input('Digite um número: '))

multiplicador = int(input('Digite um número multiplicador: '))

for i in range(10):
    resultado = lista[i] * multiplicador
    print(multiplicador,' x ', lista[i], '= ', resultado)