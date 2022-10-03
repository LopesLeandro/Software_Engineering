'''
3)	Faça um programa que receba o estoque atual de três produtos que estão armazenados em quatro armazéns e coloque esses dados em uma matriz 5x3. Sendo que a última linha da matriz contém o custo 
de cada produto, calcule e mostre:
a.	A quantidade de itens  armazenas em cada armazém
b.	Qual o armazém possui maior estoque do produto 2;
c.	Qual o armazém possui menor estoque
d.	Qual o custo total de cada produto
e.	Qual o custo total de cada armazém
'''

dados = [[0] * 5 for i in range(3)]
produtos = [0] * 3

for i in range(3):
    for j in range(4):
        dados[i][j] = int(input(f'Informe a quantidade do produto {i + 1} no armazém {j + 1}: '))
    dados[i][4] = int(input(f'Informe o custo do produto {i + 1}: '))
    produtos[i] = sum(dados[i][0:4])
    soma_prod1 = sum(dados[0][0:4])
    soma_prod2 = sum(dados[1][0:4])
    soma_prod3 = sum(dados[2][0:4])

print(f'Quantidade de itens armazenados em cada armazém: {produtos}')
print(f'Armazém com maior estoque do produto 2: {max(dados[1][0:4])}')
print(f'Armazém com menor estoque do produto 2: {min(dados[1][0:4])}')
print(f'Custo total de cada produto: {produtos}')
print(f'Custo total de cada armazém: {soma_prod1}, {soma_prod2}, {soma_prod3}')