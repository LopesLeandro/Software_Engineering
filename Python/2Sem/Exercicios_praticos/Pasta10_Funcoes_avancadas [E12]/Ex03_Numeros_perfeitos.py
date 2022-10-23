''''
3.	Elabore uma função que retorne um vetor com os três primeiros números perfeitos. 
Sabe-se que um número é perfeito quando é igual à soma de seus divisores (exceto ele mesmo). 
Exemplo: os divisores de 6 são: 1 , 2 e 3, e 1+2+3 = 6, logo 6 é perfeito.
'''

def f_perfeito(num):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    if soma == num:
        return True
    else:
        return False

def f_vetor_perfeito():
    vetor = []
    lim = int(input('Digite o limite de contagem dos números: [limite == 100bi]'))
    qnt_perfeitos = int(input('Digite a quantidade de números perfeitos: [limite == 4]'))
    for i in range(1, lim): #100 bilhões
        if f_perfeito(i):
            vetor.append(i)
        if len(vetor) == qnt_perfeitos:
            break
    return vetor

print(f_vetor_perfeito())