#2) Em um campeonato de futebol existem cinco times e cada time possui onze jogadores. Faça um programa que receba a idade,
# o peso e a altura de cada um dos jogadores, calcule e mostre:
#- a quantidade de jogadores com idade inferior a 18 anos;
#- a média das idades dos jogadores de cada time;
#- a média das alturas de todos os jogadores do campeonato;
#- a percentagem de jogadores com mais de 80 quilos entre todos os jogadores do campeonato.

qtdmenor = 0
somaaltura = 0
qtdgordinhos = 0
for time in range(5):
    print("Time: ", time+1)
    somaidade = 0
    for jogador in range(11):
        print("Jogador: ", jogador+1)
        print("Digite a idade")
        idade = int(input())
        print("Digite o peso")
        peso = float(input())
        print("digite a Altura ")
        altura = float(input())
        somaidade += idade
        somaaltura += altura
        if peso > 80:
            qtdgordinhos+=1
        if idade < 18:
            qtdmenor+=1
    #fim for jogadores
    mediatime = somaidade / 11
    print("A media do time e ", mediatime)

print("Quantidade menor de 18 ", qtdmenor)
medialtura = somaaltura / 55
print("A media das alturas e ", medialtura)
percgordinhos = qtdgordinhos * 100 / 55
print("O percentual de gordinhos e ", qtdgordinhos)