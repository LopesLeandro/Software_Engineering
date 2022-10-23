''''
4.	Crie uma função que receba como parâmetro um valor inteiro e positivo N e retorne o valor de S que é obtido pelo seguinte cálculo:
S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!

'''

def f_fatorial(num):
    if num == 0:
        return 1
    else:
        return num * f_fatorial(num - 1)

def f_soma_fatorial():
    soma = 0
    num = int(input('Digite um número inteiro e positivo: '))
    for i in range(0, num + 1):
        soma += 1 / f_fatorial(i)
    return soma

print(f_soma_fatorial().__format__('.2f'))
