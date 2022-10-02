#REPREP2)Em um campeonato de futebol existem cinco times e cada time possui onze jogadores. Faça um programa que receba
# a idade, o peso e a altura de cada um dos jogadores, calcule e mostre (valide todos os dados de entrada):
# - a quantidade de jogadores com idade inferior a 18 anos;
# - a média das idades dos jogadores de cada time;
# - a média das alturas de todos os jogadores do campeonato;
# - a percentagem de jogadores com mais de 80 quilos entre todos os jogadores do campeonato.
idade_menor = 0
total_idade_time = 0
total_altura = 0
peso_inferior = 0

for time in range(1,6):
    print('Time 0',time)
    for jogador in range(1,12):
        print('Jogador 0',jogador)
        idade = int(input('Idade deste jogador:\t'))
        if idade < 0:
            print('Dado inválido.')
            jogador -= 1
            continue
        if idade > 0 and idade < 18:
            idade_menor += 1
        peso = float(input('Peso deste jogador:\t'))
        if peso < 0:
            print('Dado inválido.')
            jogador -= 1
            continue
        if peso > 0 and peso < 80:
            peso_inferior += 1
        altura = float(input('Altura deste jogador:\t'))
        if altura < 0:
            print('Dado inválido.')
            jogador -= 1
            continue


        total_idade_time += idade
        media_idade_time = total_idade_time / 11

    print('A média de idade do time é de ',media_idade_time,' anos.')
    total_altura += altura
    media_altura_total = total_altura / 55
    perc_peso_inferior = (55 / peso_inferior) * 100
print('A quantidade de jogadores com idade inferior a 18 anos é: ', idade_menor)
print('O percentual de jogadores com menos de 80 quilos é %.2f'% perc_peso_inferior)
