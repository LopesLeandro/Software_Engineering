''''
3.	A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário e número de filhos. 
Faça uma função que leia esses dados para um número não determinado de pessoas e retorne a média de salário da população, 
a média do número de filhos, o maior salário e o percentual de pessoas com salário até R$ 350,00.
'''

#FUNÇÃO PARA NÚMERO DE FAMÍLIAS A COLETAR DADOS
from math import floor


def habitantes():
    num_habitantes = int(input('Digite o número de habitantes: '))
    return num_habitantes

#FUNÇÃO COLETA SALARIO E NÚMERO DE FILHOS E
#FUNÇÃO QUE CALCULA O PERCENTUAL DE PESSOAS COM SALÁRIO SUPERIOR A R$ 350,00
def dados(num_habitantes):
    salario = []
    filhos = []
    conta_salario_maior = 0
    for i in range(num_habitantes):
        salario.append(float(input('Digite o salário: R$ ')))
        if salario[i] > 350:
            conta_salario_maior += 1
        filhos.append(int(input('Digite quantidade de filhos: ')))
    percentual_maior = conta_salario_maior / num_habitantes * 100
    return salario, filhos, conta_salario_maior, percentual_maior


#FUNÇÃO QUE CALCULA A MÉDIA DE SALÁRIO DA POPULAÇÃO E A MÉDIA DO NÚMERO DE FILHOS
def f_media(salario, filhos, num_habitantes):
    soma_salario = 0
    soma_filhos = 0
    for i in range(num_habitantes):
        soma_salario += salario[i]
        soma_filhos += filhos[i]
    media_salario = soma_salario / num_habitantes
    media_filhos = soma_filhos / num_habitantes
    return media_salario, media_filhos

#FUNÇÃO QUE CALCULA O MAIOR SALÁRIO
def f_maior_salario(salario, num_habitantes):
    maior = 0
    for i in range(num_habitantes):
        if maior < salario[i]:
            maior = salario[i]
    return maior



#FUNÇÃO PRINCIPAL QUE IMPRIME E ORGANIZA AS FUNÇÕES E IMPRIME TUDO
def senso():
    num_habitantes = habitantes()
    salario, filhos, conta_salario_maior, percentual_maior = dados(num_habitantes)
    media_salario, media_filhos = f_media(salario, filhos, num_habitantes)
    maior_salario = f_maior_salario(salario, num_habitantes)
    #print(salario, filhos, media_salario, floor(media_filhos), maior_salario.__format__('.2f'), percentual_maior)
    print('A lista de valor de salários coletados: ', salario)
    print('A lista de quantidade de filhos coletados: ', filhos)
    print('A média de salário da população é de R$ {:.2f}'.format(media_salario))
    print('A média do número de filhos é de ', floor(media_filhos))
    print('O maior salário é de R$ {:.2f}'.format(maior_salario))
    print('O percentual de pessoas com salário superior a R$ 350,00 é de {:.2f}%'.format(percentual_maior))

#IMPRIME TUDO
senso()



'''
def pessoas():
    num_pessoas = int(input("Digite o número de pessoas: "))
    return num_pessoas

def dados(num_pessoas):
    for i in range(num_pessoas):
        salario = float(input("Digite o salário: "))
        if salario == 0:
            break
        filhos = int(input("Digite o número de filhos: "))
        return salario, filhos

def media_salario(salario, filhos):
    media_salario = salario / filhos
    return media_salario

def media_filhos(salario, filhos):
    media_filhos = filhos / salario
    return media_filhos

def maior_salario(salario, filhos):
    maior_salario = salario
    return maior_salario

def percentual(salario, filhos):
    percentual = salario / filhos
    return percentual

def senso_prefeitura():
    num_pessoas = pessoas()
    salario, filhos = dados()
    media_salario = media_salario(salario, filhos)
    media_filhos = media_filhos(salario, filhos)
    maior_salario = maior_salario(salario, filhos)
    percentual = percentual(salario, filhos)
    print("A média de salário da população é: ", media_salario.__format__(".2f"))
    print("A média do número de filhos é: ", media_filhos.__format__(".2f"))
    print("O maior salário é: ", maior_salario.__format__(".2f"))
    print("O percentual de pessoas com salário até R$ 350,00 é: ", percentual.__format__(".2f"))

senso_prefeitura()
'''