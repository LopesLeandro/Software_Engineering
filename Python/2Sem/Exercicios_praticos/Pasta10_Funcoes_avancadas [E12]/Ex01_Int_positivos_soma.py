''''
1.	Faça um programa contendo uma função que receba dois números positivos por parâmetro e retorne a soma dos N números inteiros existentes entre eles.
'''

def f_soma(num_1, num_2):
    soma = 0
    for i in range(num_1, num_2):
        soma += i
    return soma

def calc():
    num_1 = int(input('Digite um número positivo: '))
    num_2 = int(input('Digite outro número positivo: '))
    #soma = f_soma(num_1, num_2)
    print(f'A soma dos números entre estes dois é: {f_soma(num_1, num_2)}')

calc()

