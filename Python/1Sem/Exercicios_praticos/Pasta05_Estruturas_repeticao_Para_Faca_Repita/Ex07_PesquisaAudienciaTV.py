#REPPARA7) Uma rede de TV deseja realizar uma pesquisa a respeito da audiência de seu canal em relação aos seus concorrentes,
#foram pesquisadas 10 famílias. Para isso a empresa realiza o seguinte questionário abaixo, insira o código necessário para
# que os dados de entrada sejam validados, e caso ocorra um valor incorreto apresente uma mensagem e solicite novamente o valor:
#  a.	O número do canal que as pessoas da casa mais assistem dentre as opções (4, 5, 7 ,12)
#  b.	O número de pessoas que vivem na casa
#  c.	A idade de CADA UMA DAS PESSOAS que vive na casa
#  d.	A região de onde moram (N – Norte / S – Sul / L – Leste / O – Oeste)


#Calcule e mostre em tela:
#- A MÉDIA idade dos moradores de CADA CASA.
#- A rede de TV adota um sistema de pontuação para cada casa de acordo com a tabela abaixo. Calcule a pontuação e apresente em tela:

###Tabela não consta, está no documento word###

#- A MÉDIA de pontos das 10 famílias entrevistadas.
#- O percentual de audiência de cada um dos canais disponíveis na cidade.
#- Qual a região, a idade e o canal mais assistindo onde mora a pessoa mais jovem e a pessoa mais idosa dentre as entrevistadas.
casa = 0
pessoas_media = 0
pontos_audiencia = 0
idade_media = 0
media_pontos_audiencia = 0
audiencia_canal4 = 0
audiencia_canal5 = 0
audiencia_canal7 = 0
audiencia_canal12 = 0
canal4 = 0
canal5 = 0
canal7 = 0
canal12 = 0
maisjovem = 150
maisvelho = 0
while True:
    if casa > 10:
        break
    casa += 1
    print('Casa 0',casa)
    numero_canais = int(input('Número do canal mais assistido pela família [4], [5], [7], ou [12]? R: '))
    if numero_canais == 4 or numero_canais == 5 or numero_canais == 7 or numero_canais == 12:
        numero_pessoas = int(input('Qual o número de pessoas que vivem na casa? R: '))
        regiao_familia = str(input('Em que região esta família mora: N-Norte | S-Sul | L-Leste | O-Oeste?'))
        idade_acumulada = 0
        for familia in range(numero_pessoas):
            print('Pessoa 0',familia)
            idade_pessoas = int(input('Qual a idade desta pessoa? R: '))
            idade_acumulada += idade_pessoas
            idade_media = idade_acumulada / numero_pessoas
            if idade_media <= 30:
                if regiao_familia == 'N' or regiao_familia == 'n' or regiao_familia == 'L' or regiao_familia == 'l':
                    pontos_audiencia += 20
                    pontos = 20
                else:
                    pontos_audiencia += 35
                    pontos = 35
            if idade_media > 30 and idade_media <=50:
                if regiao_familia == 'N' or regiao_familia == 'n':
                    pontos_audiencia += 40
                    pontos = 40
                if regiao_familia == 'S' or regiao_familia == 's':
                    pontos_audiencia += 50
                    pontos = 50
                if regiao_familia == 'L' or regiao_familia == 'l' or regiao_familia == 'O' or regiao_familia == 'o':
                    pontos_audiencia += 60
                    pontos = 60
            if idade_media > 50:
                pontos_audiencia += 30
                pontos = 30
            if numero_canais == 4:
                audiencia_canal4 += pontos
                canal4 += 1
            if numero_canais == 5:
                audiencia_canal5 += pontos
                canal5 += 1
            if numero_canais == 7:
                audiencia_canal7 += pontos
                canal7 += 1
            if numero_canais == 12:
                audiencia_canal12 += pontos
                canal12 += 1
        if idade_pessoas < maisjovem:
            maisjovem = idade_pessoas
            regiao_jovem = regiao_familia
            canal_jovem = numero_canais
        if idade_pessoas > maisvelho:
            maisvelho = idade_pessoas
            regiao_velho = regiao_familia
            canal_velho = numero_canais
        media_pontos_audiencia = pontos_audiencia / 10
        perccanal4 = (audiencia_canal4 / pontos_audiencia) * 100
        perccanal5 = (audiencia_canal5 / pontos_audiencia) * 100
        perccanal7 = (audiencia_canal7 / pontos_audiencia) * 100
        perccanal12 = (audiencia_canal12 / pontos_audiencia) * 100
        print('A média da idade dos moradores da casa é: ', idade_media)
        print('A média de pontos de audiência entre as familias é: ', media_pontos_audiencia)
    else:
        print('Digite a opção correta.')
        casa -= 1
        continue
print('O percentual de audiência do canal [4] é: %.2f' % perccanal4)
print('O percentual de audiência do canal [5] é: %.2f' % perccanal5)
print('O percentual de audiência do canal [7] é: %.2f' % perccanal7)
print('O percentual de audiência do canal [12] é: %.2f' % perccanal12)
print('Região do mais jovem é: ', regiao_jovem, 'e a idade é: ', maisjovem, 'e o canal mais assistido é: ', canal_jovem)
print('Região do mais velho é: ', regiao_velho, 'e a idade é: ', maisvelho, 'e o canal mais assistido é: ', canal_velho)