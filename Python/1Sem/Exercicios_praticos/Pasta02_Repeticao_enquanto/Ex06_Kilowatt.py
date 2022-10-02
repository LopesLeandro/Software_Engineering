#REPENQ6) Faça um programa que receba o valor do salário mínimo e uma lista contendo a quantidade de quilowatts gasta por
#consumidor e o tipo do consumidor (1-Residencial, 2-Comercial, 3-Industrial).
#Calcule e mostre:
#- O valor de cada quilowatt, sabendo que o quilowatt custa 1/8 do salário mínimo;
#- O valor a ser pago por cada consumidor (conta final mais acréscimos), considerando que o acréscimo é o mesmo da tabela
#a seguir:
#Tipo	% de acréscimo sobre o valor gasto
#1	5
#2	10
#3	15
#
#- O faturamento geral da empresa
#- a quantidade de consumidores que pagam entre R$ 500,00 e R$ 1000,00
#Termine a entrada de dados quando a quantidade de quilowatts digitada for igual a zero.

#########################################################################################################################
consumo = 1
faturamento = 0
conta = 0
salminimo = 1212

while consumo != 0:
    sal = int(input("Qual o salário do consumidor: "))
    print("1-Residencial | 2-Comercial | 3-Industrial")
    clientype = int(input())
    if clientype == 1:
        clientype = 0.05

    if clientype == 2:
        clientype = 0.1
    if clientype == 3:
        clientype = 0.15

    consumo = float(input("Qual o consumo: "))
    valwatt = salminimo / 8
    valorconsumocliente = consumo * valwatt
    totalpagar = (valorconsumocliente * clientype) + valorconsumocliente
    faturamento += totalpagar
    if totalpagar > 500 and totalpagar < 1000:
        conta += 1
    print("O valor de cada quilowatt é: R$", valwatt)
    print("Total a pagar cliente: R$ ", totalpagar, ".")

print("O faturamento da empresa é: R$", faturamento)
print("O número de clientes que pagam entre R$ 500,00 e R$ 1.000,00 é: ", conta)

# SOLUÇÃO DO PROFESSOR

#    print("Digite o salário mínimo:")
#    salmin = float(input())
#    valkw = salmin / 8
#    faturamentogeral = 0
#    contador = 0
#    print("O valor do KW/h é", valkw)
#    while True:
#        print("Digite a qtd de KW/h")
#        qtdkw = float(input())
#        print("Digite o tipo 1-RES/2-COM/3-IND")
#        tipo = int(input())
#        if qtdkw == 0:
#            break
#        valpagar = qtdkw * valkw
#        if tipo == 1:
#            valpagar = valpagar * 1.05
#        else:
#            if tipo == 2:
#                valpagar = valpagar * 1.10
#            else:
#                valpagar = valpagar * 1.15
#        print("O valor a pagar é ", valpagar)
#        if valpagar >= 500 and valpagar <= 1000:
#            contador += 1
#        faturamentogeral += valpagar
#    print("O faturamento geral é ", faturamentogeral)
#    print("A qnt de pessoas com conta entre 500 e 1000 é ", contador)






