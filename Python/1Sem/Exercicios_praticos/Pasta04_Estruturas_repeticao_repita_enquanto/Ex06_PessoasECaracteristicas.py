# REPREP6) Faça um programa que receba a idade, o peso, a altura, a cor dos olhos (a – Azul, p – Preto, v – Verde e c – Castanho)
# e a cor dos cabelos (p – preto, c – castanho, l – Louro e r – Ruivo) de 20 pessoas (valide as entradas). Calcule e mostre:
# - a quantidade de pessoas com idade superior a 50 anos e peso inferior a 6- quilos;
# - a média das idades das pessoas com altura inferior a 1,50;
# - a percentagem de pessoas com olhos azuis entre todas as pessoas analisadas;
# - a quantidade de pessoas ruivas e que não possuem olhos azuis
veio_leve = 0
idade_baixinhos = 0
conta_baixinhos = 0
azuis = 0
ruivos = 0
for pessoas in range(1, 3):
    print('Pessoa', pessoas)

    repeat0 = True
    while repeat0:
        idade = int(input('Digite idade: \t'))
        if idade > 0:
            repeat0 = False
        else:
            print('Digite um dado válido.')
            repeat0 = True

    repeat1 = True
    while repeat1:
        peso = float(input('Digite peso: \t'))
        if peso > 0:
            repeat1 = False
        else:
            print('Digite um dado válido.')
            repeat1 = True
    if idade > 50 and peso > 0 and peso < 60:
        veio_leve += 1
    repeat2 = True
    while repeat2:
        altura = float(input('Digite altura: \t'))
        if altura > 0:
            repeat2 = False
        else:
            print('Digite um dado válido.')
            repeat2 = True
    if altura > 0 and altura < 150:
        idade_baixinhos += idade
        conta_baixinhos += 1
    repeat3 = True
    while repeat3:
        cor_olho = str(input('Cor dos olhos: [a] [p] [v] [c]'))
        if cor_olho == 'a' or cor_olho == 'p' or cor_olho == 'v' or cor_olho == 'c':
            repeat3 = False
        else:
            print('Digite um dado válido.')
            repeat3 = True
    if cor_olho == 'a':
        azuis += 1
    repeat4 = True
    while repeat4:
        cor_cabelo = str(input('Cor dos cabelos: [p] [c] [l] [r]'))
        if cor_cabelo == 'p' or cor_cabelo == 'c' or cor_cabelo == 'l' or cor_cabelo == 'r':
            repeat4 = False
        else:
            print('Digite um dado válido.')
            repeat4 = True
    if cor_cabelo == 'r' and cor_olho != 'a':
        ruivos += 1
perc_azuis = azuis / 20
media_baixinhos = idade_baixinhos / conta_baixinhos
print('a) Veios leves =',veio_leve)
print('b) Média idade baixinhos = ', media_baixinhos)
print('c) Percentual olhos azuis =',perc_azuis)
print('d) Quantidade ruivos sem olhos azuis = ',ruivos)