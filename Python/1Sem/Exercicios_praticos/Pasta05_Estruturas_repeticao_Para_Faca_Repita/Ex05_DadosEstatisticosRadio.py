#REPPARA5) Uma radio necessita realizar alguns cálculos estatísticos referente ao número de minutos de musicas e de
#propagandas que são vinculadas. Considere que a radio fica 744 horas por mês no ar. Solicite POR SEMANA o número horas
#da programação em que foram vinculadas músicas e o numero de horas em que foram vinculadas apenas propagandas.
# Calcule e mostre:
#  a. A semana em que houve o a maior quantidade de horas de propagandas vinculadas.
#  b. A semana em que houve a menor quantidade de horas de musicas vinculadas.
#  c. O total de horas de propagandas vinculadas.
#  d. O total de horas de musicas vinculadas.
#  e. O percentual que o total de horas de propagandas representa do numero total de horas que a rádio fica no ar

#teste

horasmes = 744
tothorasmusica = 744
tothorasproganda = 0
maiorprop = 0
menormusic = 0
totalpropaganda = 0
totalmusica = 0
for i in range(1,5):
    print('Semana: 0', i)
    horasmusica = int(input('Quantas horas de música nesta semana:  '))
    horasproganda = int(input('Quantas horas de propaganda nesta semana:  '))
    if horasproganda > tothorasproganda:
        tothorasproganda = horasproganda
        maiorprop = i
    if horasmusica < tothorasmusica:
        tothorasmusica = horasmusica
        menormusic = i
    totalpropaganda += horasproganda
    totalmusica += horasmusica

quantapropagandamane = float(totalpropaganda / 744) * 100

print('1) A semana com maior quantidade de propagandas é: ', maiorprop)
print('2) A semana com menor quantidade de música é: ', menormusic)
print('3) O total de horas de propagandas vinculadas é: ', totalpropaganda)
print('4) O total de horas de musicas vinculadas é: ', totalmusica)
print('5) O percentual de propaganda em relação as horas no ar é de %.2f' %quantapropagandamane, '%.')
