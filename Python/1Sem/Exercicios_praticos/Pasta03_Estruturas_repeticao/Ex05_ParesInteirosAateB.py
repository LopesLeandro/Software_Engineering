#5)Faça um programa que leia cinco pares de valores (a,b), todos inteiros e positivos, um de cada vez. Mostre os números
# inteiros pares de a até b (inclusive).

cont = 0
while cont != 5:
    a = int(input("Digite um número: "))
    b = int(input("Digite um número: "))
    if a or b < 0:
        print("Somente números naturais.")
        break
    for i in range(a,b+1):
        if i % 2 == 0:
            print(i,". ", end="")
    cont += 1