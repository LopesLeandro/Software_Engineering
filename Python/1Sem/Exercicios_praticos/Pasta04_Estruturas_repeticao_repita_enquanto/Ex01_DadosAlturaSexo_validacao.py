#REPREP1) Tem-se um conjunto de dados contendo a altura e o sexo (M ou F) de 10 pessoas (Valide os dados de entrada para
# garantir que a altura e o sexo sejam valores válidos). Faça um programa que calcule e mostre:
# a) a maior e a menor altura do grupo;
# b) a média de altura das mulheres;
# c) o número de homens;
# d) o sexo da pessoa mais alta.

maior = 0
menor = 0
cont_mulheres = 0
altura_mulheres = 0
i = 1
while i < 10:
    print("Dados da pessoa: ", i)
    altura = float(input('Digite a altura: '))
    sexo = str(input('Digite o sexo: [M] ou [F]: '))
    i += 1
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida!')
        i = i - 1
        continue
    if sexo == 'F':
        altura_mulheres += altura
        cont_mulheres += 1
    if i == 0:
        maior = altura
        menor = altura
    if altura > maior:
        maior = altura
        sexo_maior = sexo
    if altura < menor:
        menor = altura

media_altura_fem = altura_mulheres / cont_mulheres
num_homens = 10 - cont_mulheres
print('O mais alto tem ', maior, 'cm.')
print('O mais baixo tem ', menor, 'cm.')
print('A média da altura feminina é ', media_altura_fem)
print('O número de homens é igual a ', num_homens)
print('O sexo do mais alto é: ', sexo_maior)