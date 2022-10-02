#Q1) Faça um algoritmo que calcule a multiplicação de dois números inteiros sem utilizar o operador “*”. Em vez disso,
# utilize apenas o operador de adição “+”. Para implementar esse algoritmo, devemos lembrar que qualquer multiplicação
# pode ser expressa por meio de somas. Por exemplo, o resultado da expressão 6 * 3 é o mesmo que 6 + 6 + 6 ou 3 + 3 + 3
# + 3 + 3 + 3. Ou seja, soma-se um elemento com ele próprio o número de vezes do segundo elemento.


print("Digite um numero:")
n1 = int(input())
print("Digite um numero:")
n2 = int(input())
acumula = 0
cont = 0

for i in range(n1):
    print(n2, end = "")
    if cont < n1 - 1:
        print("+", end="")
    acumula += n2
    cont += 1
print("=", acumula)

#PROFESSOR
#print("Digite um numero")
#num1 = int(input())
#print("Digite o segundo numero")
#num2 = int(input())

#result = 0
#for i in range(num1):
#    print(num2, " + ", end=" ")
#    result = result + num2

#print("Resultado: ", result)
#FIM
#list(range(10))
#list(range(5,10,2 ou -1 ou 3 ou ...)