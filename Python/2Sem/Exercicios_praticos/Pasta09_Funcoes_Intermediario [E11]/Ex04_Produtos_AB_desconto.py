''''
4.	Um determinado estabelecimento fará uma venda com descontos nos produtos A e B. 
Se forem comprados apenas os produtos A ou apenas os produtos B, o desconto será de 10%. 
Caso sejam comprados os produtos A e B, o desconto será de 15%. 
O custo da unidade de cada produto é dado respectivamente para os produtos A e B como sendo de R$ 10 e R$ 20. 
Elaborar um programa que por meio de sub-rotina calcule e apresente o valor da despesa do freguês na compra dos produtos. 
Lembre-se que o freguês poderá levar mais de uma unidade de um determinado produto. 
'''

def desconto (a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0 or b == 0:
        return 10
    else:
        return 15

def valor (a, b):
    return (a * 10) + (b * 20)

def operacao():
    a = int(input("Quantos do produtos A? "))
    b = int(input("Quantos do produtos B? "))
    print("Desconto: ", desconto(a, b), '%')
    print("Valor: ", valor(a, b).__format__(".2f"))

operacao()
