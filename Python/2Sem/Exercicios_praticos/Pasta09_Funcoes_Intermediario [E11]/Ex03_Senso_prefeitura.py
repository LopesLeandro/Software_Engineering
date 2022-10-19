''''
3.	A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário e número de filhos. 
Faça uma função que leia esses dados para um número não determinado de pessoas e retorne a média de salário da população, 
a média do número de filhos, o maior salário e o percentual de pessoas com salário até R$ 350,00.
'''

def dados():
    while True:
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
    salario, filhos = dados()
    media_salario = media_salario(salario, filhos)
    media_filhos = media_filhos(salario, filhos)
    maior_salario = maior_salario(salario, filhos)
    percentual = percentual(salario, filhos)
    print("A média de salário da população é: ", media_salario.__format__(".2f"))
    print("A média do número de filhos é: ", media_filhos.__format__(".2f"))
    print("O maior salário é: ", maior_salario.__format__(".2f"))
    print("O percentual de pessoas com salário até R$ 350,00 é: ", percentual.__format__(".2f"))