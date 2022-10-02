# REPETIÇÃO9) Faça um programa que receba vários números, calcule e mostre:
# - a soma dos números digitados;
# - a quantidade de números digitados;
# - a média dos números digitados;
# - o maior número digitado;
# - o menor número digitado;
# - a média dos números pares;
# - a porcentagem dos números ímpares entre todos os números digitados.
# Finalize a entrada de dados com a digitação do número 30000.

n = 0
s = 0
c = 0
b = 30000
m = 0
a = 0
z = 0
sp: int = 0
cp = 0
si = 0
ci = 0
pi = 0

while True:
    print("Digite um numero:")
    n = int(input())
    if n == b:
        break
    else:
        s += n
        # c += 1
        if c == 0:
            z = n
            a = n
        if n > z:
            z = n
        if n < a:
            a = n
        c += 1
    if n % 2 == 0:
        sp = sp + n
        cp += 1
    if n % 2 != 0:
        ci += 1

m = s / c
mp = sp / cp
pi = (ci / c) * 100

print("A soma dos numeros é ", s)
print("A quantidade de números digitados é ", c)
print("A média dos numeros é ", m)
print("O maior número é ", z)
print("O menor número é ", a)
print("A soma dos números pares é ", sp)
print("A média dos números pares é ", mp)
print("O percentual de números impares entre todos é", pi)