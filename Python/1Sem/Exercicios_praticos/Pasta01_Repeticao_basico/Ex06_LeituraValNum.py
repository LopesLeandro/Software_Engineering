#6) Elaborar um programa que efetue a leitura de 10 valores numéricos e
#   apresente no final o total do somatório e a média do total.
num = 1
sum = 0
med = 0

while num <= 10:
    i = int(input("Digite um valor: "))
    num += 1
    sum = sum + i

med = sum / 10

print("A soma dos números é", sum)
print("A média dos números é %2.f"% med)
