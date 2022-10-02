#7) Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos
# os seguintes dados:
#a) nome da cidade;
#b) número de veículos de passeio;
#c) número de acidentes de trânsito com vítimas
#Deseja-se saber:
#a) qual o maior e o menor índice de acidentes de trânsito e a que cidades pertencem;
#b) qual a média de veículos nas cinco cidades juntas;
#c) qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
maiorindice = 0
menorindice = 999999999999999999999999999999999999999999999999999999
indicecidadepequena = 0
cidademenorindice = 0
cidademaiorindice = 0
totalveiculos = 0
numcidadespequenas = 0

for i in range(5):
    cidade = str(input("Nome da cidade: "))
    numveiculos = int(input("Número de veículos de paseeio: "))
    numacidentes = int(input("Número de acidentes de trânsito: "))
    indice = float(numacidentes/numveiculos)*100
    totalveiculos += numveiculos
    if indice > maiorindice:
        maiorindice = indice
        cidademaiorindice = cidade
    if indice < menorindice:
        menorindice = indice
        cidademenorindice = cidade
    if numveiculos < 2000:
        indicecidadepequena += numveiculos
        numcidadespequenas += 1

mediapequena = indicecidadepequena / numcidadespequenas
media = totalveiculos / 5
print("a.1: A cidade com maior indice de acidente é: ", cidademaiorindice, "que possuir um indice de %2.f" % maiorindice, "%.")
print("a.2: A cidade com menor indice de acidente é: ", cidademenorindice, "que possuir um indice de %2.f" % menorindice, "%.")
print("b.1: A média de veículos de todas as cidades é: ", media)
print("c.1: A média de acidentes em cidades com menos de 2000 veículos de passeio é de %2.f" % mediapequena)