#REPPARA3) Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião em
#relação ao filme: ótimo – 3, bom – 2, regular – 1. Faça um programa que receba a idade e a opinião de 15 espectadores
# e que calcule e mostre:
#- a média das idades das pessoas que responderam ótimo
#- a quantidade de pessoas que respondeu regular
#- a percentagem de pessoas que respondeu bom entre todos os espectadores analisados
idadeotimo = 0
contotimo = 0
contregular = 0
contbom = 0
for i in range(3):
    idade = int(input('Digite a idade: '))
    print('Qual sua opinião em relação ao filme?')
    opiniao = int(input('Ótimo - 3 | Bom - 2 | Regular - 1'))
    if opiniao == 3:
        idadeotimo += idade
        contotimo += 1
    if opiniao == 2:
        contbom += 1
    if opiniao == 1:
        contregular += 1

calcmediaidot = idadeotimo / contotimo
percbom = (contbom / 15) * 100


print('1) A média da idade das pessoas que responderam ótimo: %.0f' % calcmediaidot)
print('2) A quantidade de pessoas que respondeu regular: ', contregular)
print('3) O percentual de pessoas que respondeu bom entre todos os espectadores analisados: %.2f' % percbom)