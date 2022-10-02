#8) Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado.
#   Ao final deve ser apresentados o maior e o menor número informado pelo usuário.

omaior = 0
omenor = 0
contador = 0

while True:
    num = int(input("Digite um valor: "))
    if num < 0:
        break
    else:
        if contador == 0:
            omaior = num
            omenor = num
        if num > omaior:
            omaior = num
        if num < omenor:
            omenor = num
        contador += 1
print("O maior valor é ", omaior)
print("O menor número é ", omenor)