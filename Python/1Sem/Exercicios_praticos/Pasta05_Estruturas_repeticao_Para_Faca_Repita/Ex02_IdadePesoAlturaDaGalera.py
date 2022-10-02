#REPPARA2) Faça um programa que receba a idade, a altura e o peso de 25 pessoas. Calcule e mostre:
#- a quantidade de pessoas com idade superior a 50 anos
#- a média das alturas das pessoas com idade entre 10 e 20 anos;
#- a percentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.
contidade = 0
alturacriancajovem = float(0)
qntcriancajovem = 0
contmagrelas = 0
for i in range(25):
    print("Dados da pessoa: ", i+1)
    idade = int(input('Digite a idade:'))
    altura = float(input('Digite a altura: '))
    peso = float(input('Digite o peso: '))

    if idade > 50:
        contidade += 1
    if idade > 9 and idade < 21:
        alturacriancajovem += altura
        qntcriancajovem += 1
    if peso < 40:
        contmagrelas += 1

percmagrelas = (contmagrelas / 25) * 100
mediacriancajovem = alturacriancajovem / qntcriancajovem
print('1) A quantidade de pessoas com idade superior a 50 anos: ', contidade)
print('2) A média das alturas das pessoas com idade entre 10 e 20 anos: %.2f' % mediacriancajovem)
print('3) O percentual de pessoas com peso inferior a 40 quilos entre todos é %.2f' % percmagrelas)