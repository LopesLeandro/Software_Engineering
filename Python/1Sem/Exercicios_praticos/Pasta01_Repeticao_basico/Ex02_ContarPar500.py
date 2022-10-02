#Contar e apresentar somatório dos números pares de 1 até 500

contador = 0
soma = 0

while contador <= 500:
    if contador % 2 == 0:
        soma = soma + contador
        print(contador)
    contador += 2
print(soma)