''''
2.	Faça uma função que receba, por parâmetro, a altura e o sexo de uma pessoa e retorne o seu peso ideal. 
Para homens calcular o peso ideal usando a fórmula a seguir: pesoideal = 72.7 * alt – 58 e para mulheres: pesoideal = 62.1 * alt – 44.7
'''

def dados():
    altura = float(input("Digite a altura: "))
    sexo = input("Digite o sexo: ")
    return altura, sexo

def peso_ideal(altura, sexo):
    if sexo == "M":
        pesoideal = (72.7 * altura) - 58
    elif sexo == "F":
        pesoideal = (62.1 * altura) - 44.7
    return pesoideal

def imc():
    altura, sexo = dados()
    pesoideal = peso_ideal(altura, sexo)
    print("O peso ideal é: ", pesoideal.__format__(".2f"))

imc()