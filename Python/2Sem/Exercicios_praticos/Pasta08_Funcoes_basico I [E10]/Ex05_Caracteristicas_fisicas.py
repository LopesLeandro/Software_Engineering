''''
5)	Foi realizada uma pesquisa de algumas características físicas de cinco habitantes de uma certa região. De cada habitante foram coletados os seguintes dados: 
    sexo, cor dos olhos (A – Azuis ou C – Castanhos), cor dos cabelos (L – Louros, P – Pretos ou C – Castanhos) e idade.
a.	Faça uma função que leia esses dados em vetores. Determine, por meio de outra função, a média de idade das pessoas com olhos castanhos e cabelos pretos. Mostre esse resultado no programa principal.
b.	Faça uma função que determine e devolva ao programa principal a maior idade entre os habitantes.
c.	Faça uma função que determine e devolva ao programa principal a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros.
'''

#Coleta as informações sobre as pessoas
def f_pessoas_dados():
    sexo = []
    olhos = []
    cabelos = []
    idade = []
    for i in range(5):
        sexo.append(input('Digite o sexo: '))
        olhos.append(input('Digite a cor dos olhos: '))
        cabelos.append(input('Digite a cor dos cabelos: '))
        idade.append(int(input('Digite a idade: ')))
    return sexo, olhos, cabelos, idade

#a) Média de idade das pessoas com olhos castanhos e cabelos pretos
def f_media_idade(olhos, cabelos, idade):
    soma = 0
    contador = 0
    for i in range(5):
        if olhos[i] == 'C' and cabelos[i] == 'P':
            soma += idade[i]
            contador += 1
    return soma/contador

#b) Maior idade entre os habitantes
def f_maior_idade(idade):
    maior = 0
    for i in range(5):
        if idade[i] > maior:
            maior = idade[i]
    return maior

#c) Quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros.
def f_fem_azul_louros_idade(sexo, olhos, cabelos, idade):
    contador = 0
    for i in range(5):
        if sexo[i] == 'F' and idade[i] >= 18 and idade[i] <= 35 and olhos[i] == 'A' and cabelos[i] == 'L':
            contador += 1
    return contador

sexo, olhos, cabelos, idade = f_pessoas_dados()
print('a) Média de idade das pessoas com olhos castanhos e cabelos pretos: ', f_media_idade(olhos, cabelos, idade))
print('b) Maior idade entre os habitantes: ', f_maior_idade(idade))
print('c) Quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros: ', f_fem_azul_louros_idade(sexo, olhos, cabelos, idade))