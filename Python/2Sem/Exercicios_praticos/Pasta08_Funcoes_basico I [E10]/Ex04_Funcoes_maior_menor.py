''''
4)	Faça uma função que receba cinco valores inteiros, e retorne o maior valor. 
Faça uma segunda função que receba também cinco valores e retorne o menor deles.
'''

def f_valores():
    lista = []
    for i in range(5):
        lista.append(int(input('Digite um valor: ')))
    maior = max(lista)
    menor = min(lista)
    return lista,maior,menor

lista, maior, menor = f_valores()
print('A lista de números é: ', lista, '| O maior valor é: ', maior, '| O menor valor é: ', menor)
