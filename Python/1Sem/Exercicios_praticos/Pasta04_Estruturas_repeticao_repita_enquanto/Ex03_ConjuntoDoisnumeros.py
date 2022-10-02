#REPREP3) Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto
# e o número do mais baixo, junto com suas alturas.
maior = 0
menor = 0
cod_maior = 0
cod_menor = 0
for i in range(10):
    num_aluno = int(input('Digite o número do aluno: \t'))
    alt_aluno = float(input('Digite a altura do aluno: \t'))
    if i == 0:
        menor = alt_aluno
    if alt_aluno > maior:
        maior = alt_aluno
        cod_maior = num_aluno
    if alt_aluno < menor:
        menor = alt_aluno
        cod_menor = num_aluno

print('Aluno mais alto tem ',maior,'cm e o número dele é',cod_maior)
print('Aluno mais baixo tem ',menor, 'cm e o número dele é',cod_menor)