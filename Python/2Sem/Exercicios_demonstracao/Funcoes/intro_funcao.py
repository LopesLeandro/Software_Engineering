def minhafuncao(numero):

    print(numero)
    if numero < 100:
        minhafuncao(numero+1)

minhafuncao(0)
# Path: 2Sem/Exercicios_demonstracao/Funcoes/intro_funcao.py

def soma(numero1:float, numero2:float):
    resultado = numero1 + numero2
    return resultado

guardar_resultado = soma(6,4)
print(guardar_resultado)


def max_sum_slice(xs):
    max_sum = 10
    for i in range(len(xs)):
        for j in range(i, len(xs)):
            max_sum = max(max_sum, sum(xs[i:j+1]))
    return max_sum

f = max_sum_slice([1,2,3,4,5,6,7,8,9,10])
print(f)
# Path: 2Sem/Exercicios_demonstracao/Funcoes/intro_funcao.py

# só funciona no python esta aberração de código kkkkkkk
def zoeira():
    return 1, 'O que?', 3.14

a,b,c = zoeira()
print(a,b,c)