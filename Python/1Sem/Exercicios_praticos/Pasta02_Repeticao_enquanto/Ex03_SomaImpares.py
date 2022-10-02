#Q3) Faça um algoritmo que calcule a soma de todos os números ímpares dentro de uma faixa de valores determinada pelo usuário.
# Um número é ímpar quando sua divisão por 2 não é exata, ou seja, o resto resultante da divisão inteira pelo número 2 tem
# valor 1. Utilize a palavra resto como operador que calcula o resto da divisão de um numero por outro.

si = 0

print("Digite um numero:")
n1 = int(input())
print("Digite um numero:")
n2 = int(input())

for i in range(n1, n2+1):
    #n1 += 1
    if i % 2 != 0:
        si = si + i
    print(si, "|")

#SUGESTÃO PROFESSOR
#print("Digite um número inicial:")
#ini = int(input())
#print("Digite um número final:")
#fin = int(input())

#soma = 0
#for i in range(ini,fin+1):
#    if i % 2 == 1:
#        print(i)
#        soma =+ i
#print("A soma é igual a ",i)