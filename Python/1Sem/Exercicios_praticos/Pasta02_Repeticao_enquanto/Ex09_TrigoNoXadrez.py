#Q9) Elaborar um programa que efetue o cálculo e no final apresente o somatório do número de grãos de trigo que se pode
#obter num tabuleiro de xadrez, obedecendo a seguinte regra: colocar um grão de trigo no primeiro quadro e nos quadros
#seguintes o dobro do quadro anterior. Ou seja, no primeiro quadro coloca-se 1 grão, no segundo quadro colocam-se 2 grãos
#(neste momento têm-se 3 grãos), no terceiro quadro colocam-se 4 grãos (tendo neste momento 7 grãos), no quarto quadro
#colocam-se 8 grãos (tendo-se então 15 grãos) até atingir o sexagésimo quarto quadrado.

#Numero de casas do tabuleiro: 8 x 8 = 64
adicionador = 0
quadro = 0

for casa in range(0,64):
    if casa == 0:
        adicionador = 1
    else:
        adicionador = adicionador * 2
    quadro = quadro + adicionador
    print(quadro)