''''
2.	Faça um programa contendo uma função que retorne 1 se o número digitado for positivo ou 0 se for negativo.
'''

def f_return_pn(num):
    if num > 0:
        return 1
    else:
        return 0

def calc():
    num = int(input('Digite um número: '))
    print(f'Se [1] o número é positivo, se [0] negativo: {f_return_pn(num)}')

calc()