#6) Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
#representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
# alto e o número do mais baixo, junto com suas alturas.

omaior = 0
omenor = 3

for i in range(1,11):
    print("Aluno: ", i)
    codigo = int(input("Código do aluno: "))
    altura = float(input("Altura do aluno: "))
    if altura > omaior:
        omaior = altura
        sortudo = codigo
    if altura < omenor:
        omenor = altura
        coitado = codigo
print("Código: ", sortudo, " é o aluno com maior altura, com aproximadamente ", omaior, "cm.")
print("Código: ", coitado, "é o aluno com a menor altura, medindo ", omenor, "cm.")