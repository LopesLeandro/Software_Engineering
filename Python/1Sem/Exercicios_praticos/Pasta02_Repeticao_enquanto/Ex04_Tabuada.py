#Q4) Faça um programa que apresente os resultados de uma tabuada de um número qualquer, a qual deve ser impressa no seguinte formato:
#Considerando como exemplo o fornecimento do número 2 para o número qualquer, ter-se-ia a seguinte situação:
#2 x 1 = 2
#2 x 2 = 4
#2 x 3 = 6
#...
#2 x 10 = 20

n1 = int(input("Digite um número para calcular a tabuada:"))
resultado = 0

for i in range(1,11,1):
    print(n1," * ", end="")
    print(i,"= ", end="")
    resultado = n1 * i
    print(resultado)

#for i in range(1,11):
#    resultado = tabuada * i
#    print(tabuada," x ", i," = ", resultado)