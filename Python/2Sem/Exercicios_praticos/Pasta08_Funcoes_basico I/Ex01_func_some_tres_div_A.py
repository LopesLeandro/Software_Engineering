''''
1)	Faça uma função que receba três números inteiros: a,b e c, onde a é maior que 1. A função deve somar todos os inteiros entre b e c que sejam divisíveis por a (inclusive b e c) e retornar o resultado para a função principal.
'''
def f (a:int,b:int,c:int):
    soma = 0
    for i in range(b,c+1):
        if i % a == 0:
            soma += i
    return soma

valor_a = int(input('Digite o valor de a: '))
valor_b = int(input('Digite o valor de b: '))
valor_c = int(input('Digite o valor de c: '))
#print(f(valor_a,valor_b,valor_c))

# da para guardar também a funcão em uma variável
guardar = f(valor_a,valor_b,valor_c)
print(guardar)