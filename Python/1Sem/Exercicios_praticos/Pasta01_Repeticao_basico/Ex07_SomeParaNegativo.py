#7) Elaborar um programa que efetue a leitura sucessiva de valores numéricos e apresente no final o total do somatório,
#   a média e o total de valores lidos. O programa deve fazer as leituras dos valores enquanto o usuário estiver fornecedor
#   valores positivos. Ou seja, o programa deve parar quando o usuário fornecer um valor negativo.

cont = 0
sum = 0
med = 0

while True:
    i = int(input("Digite um valor: "))
    if i < 0:
        break
    sum = sum + i
    cont = cont + 1

cont = cont
med = sum / cont

print("A soma dos números é", sum)
print("A média dos números é %2.f"% med)
print("O número de valores lidos é", cont)

#PROFESSOR
while True:
    print("Digite um numero:")
    num = int(input())
    if num < 0:
        break
    else:
        acumulador += num
        contador += 1
print("A soma dos numeros é ", acumulador)
print("A quantidade total dos numeros é ", contador)
print("A média é ", media)
