#Q2) Faça um algoritmo que leia um número inteiro e calcule o seu fatorial. Se o número for negativo, informe que o valor
# é inválido. Sabemos que o fatorial de um número n, representado por n!, é dado por:
# n * (n-1) * (n-2) * ... * 1, para n > 0 e n! = 1 para n = 0
# 5! = 5*4*3*2*1=120
print("Digite um número:")
num = int(input())

if num < 0:
    print("Número inválido you animal!")
else:
    for i in range(1,num+1):
        print(i, "! = ", end="")
        fat = 1
        for j in range(i,0,-1):
            print(j,".",end="")
            fat = fat * j
        print(" = ", fat)

#SUGESTÃO PROFESSOR
#result = 1
#print(num,"!= ",end="")
#for i in range(num,0,-1):
#    print(i, " * ", end="")
#    result = result * i
#print(" = ",result)
