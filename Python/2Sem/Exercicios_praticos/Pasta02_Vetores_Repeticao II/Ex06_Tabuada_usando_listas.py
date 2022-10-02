''''
Faça um programa que receba dez números e armazene em uma lista. 
Em seguida solicite um outro número e armazene em uma variável chamada multiplicador. 
Percorra todo a lista e multiplique cada número pelo multiplicador e apresente em tela.
'''

lista = [0] * 10

for i in range(10):
    num = int(input('Digite um número: \t'))
    lista[i] = num

multiplicador = int(input('Digite o multiplicador: \t'))

for j in range(10):
    resultado = multiplicador * lista[j]
    print('-> \t', multiplicador, ' * ', lista[j], '= \t', resultado)
