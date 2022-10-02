#3)Tem-se um conjunto de dados contendo a altura e o sexo (M ou F) de 10 pessoas. Faça um programa que calcule e mostre:
#a) a maior e a menor altura do grupo;
#b) a média de altura das mulheres;
#c) o número de homens;
#d) o sexo da pessoa mais alta.

omaior = 0
omenor = 3
nummulheres = 0
somaalturamulheres = float(0)
fem = 'F'

for pessoas in range(10):
    altura = float(input("Altura da pessoa: [Ex.: 1.78]"))
    sexo = str(input("Sexo da pessoa: "))
    if altura > omaior:
        omaior = altura
        sexogig = sexo
    if altura < omenor:
        omenor = altura
    if sexo is fem:
        nummulheres += 1
        somaalturamulheres += altura

#PROCESSAMENTO
mediaalturamulheres = somaalturamulheres / nummulheres
numhomensnahistoria = 10 - nummulheres


#SAÍDA
print("A maior pessoa tem ", omaior, "de altura.")
print("A menor pessoa tem ", omenor, "de altura.")
print("A média de altura das mulheres é ", mediaalturamulheres)
print("O número de homens é igual a ", numhomensnahistoria)
print("O sexo da pessoa mais alta é ", sexogig)