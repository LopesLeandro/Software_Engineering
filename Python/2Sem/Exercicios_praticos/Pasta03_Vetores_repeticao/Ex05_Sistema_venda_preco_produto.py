'''
Faça um programa que receba a quantidade de peças vendidas por vendedor e armazene essas quantidades em um vetor. Receba também o preço da peça vendida de cada vendedor e armazene esses preços em outro vetor. Existem apenas dez vendedores e cada vendedor pode vender apenas um tipo de peça, isto é, para cada vendedor existe apenas um preço. Calcule e mostre a quantidade total de peças vendidas por todos os vendedores e para cada vendedor calcule e mostre o valor total da venda, isto é, a quantidade de peças * o preço da peça.
'''
'''
           +---+---+---+---+---+---+---+---+---+---+
listaqtd = | 3 | 8 |   |   |   |   |   |   |   |   |
           +---+---+---+---+---+---+---+---+---+---+
             0   1   2   3   4   5   6   7   8   9
           +---+---+---+---+---+---+---+---+---+---+
listapre = |10 | 2 |   |   |   |   |   |   |   |   |
           +---+---+---+---+---+---+---+---+---+---+
             0   1   2   3   4   5   6   7   8   9
'''

listaqtd = [0] * 10
listapre = [0] * 10

for i in range(10):
    print("Vendedor ->", i+1)
    print("Digite a qtd vendida")
    listaqtd[i] = int(input())
    print("Digite o preco do produto vendido")
    listapre[i] = float(input())

# quantidade total de peças vendidas por todos os vendedores
somaqtd = 0
for i in range(10):
    somaqtd += listaqtd[i]

print("A qtd total e ", somaqtd)
print("A qtd total e ", sum(listaqtd))

#para cada vendedor calcule e mostre o valor 
#total da venda, isto é, a quantidade de peças * o preço da peça.

for i in range(10):
    valtot = listaqtd[i] * listapre[i]
    print("Produto -> ", i+1, " valor total R$ ", valtot)