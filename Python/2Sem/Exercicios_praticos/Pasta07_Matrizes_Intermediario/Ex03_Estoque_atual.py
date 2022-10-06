'''
3)	Faça um programa que receba o estoque atual de três produtos que estão armazenados em quatro armazéns e coloque esses dados em uma matriz 5x3. Sendo que a última 
linha da matriz contém o custo de cada produto, calcule e mostre:
a.	A quantidade de itens  armazenas em cada armazém
b.	Qual o armazém possui maior estoque do produto 2;
c.	Qual o armazém possui menor estoque
d.	Qual o custo total de cada produto
e.	Qual o custo total de cada armazém
'''
dados = [[0] * 3 for i in range(5)]
armazem = [0] * 4
maior_produto = 0
menor_produto = 9999
custo_armazem = [0] * 4
contador = 0

#Constroi a matriz facilmente para teste:
#for lin in range(5):
#    for col in range(3):
#        dados[lin][col] = contador
#        print(dados[lin][col], end=' \t')
#        contador += 1
#    print()

#Matriz solicitando informações conforme enunciado do exercício:
for lin in range(5):
    for col in range(3):
        if lin == 4:
            dados[lin][col] = float(input(f'Informe o custo do produto {col+1}: '))
        else:
            dados[lin][col] = int(input(f'Informe a quantidade do produto {col+1} no armazém {lin+1}: '))
        
for lin in range(5):
    for col in range(3):
        print(dados[lin][col], end=' \t')
    print()

#Quantidade em cada armazem e o que tem maior estoque do produto 2 e o armazem com o menor estoque:
for lin in range(4):
    soma_produto = 0
    for col in range(3):
        soma_produto += dados[lin][col]
        if dados[lin][1] > maior_produto:
            maior_produto = dados[lin][1]
            armazem_maior = lin + 1
        if dados[lin][col] < menor_produto:
            menor_produto = dados[lin][col]
            armazem_menor = lin + 1
    armazem[lin] = soma_produto
print('a) O total de produtos em cada armazém é de ', armazem)
print('b) O armazém que tem o maior estoque do produto 2 é o', armazem_maior)
print('c) O armazém que tem o menor estoque é o', armazem_menor)

#Custo total de cada produto:
custo_produto = [0] * 3
for lin in range(4):
    for col in range(3):
        custo_produto[col] += dados[lin][col] * dados[4][col]
print('d) O custo total de cada produto é de ', custo_produto)

#Custo total de cada armazém:
for lin in range(4):
    for col in range(3):
        custo_armazem[lin] += dados[lin][col] * dados[4][col]
print('e) O custo total de cada armazém é de ', custo_armazem)


#FIM DO PROGRAMA

#Daqui para baixo:
#Primeira tentativa de fazer o exercício, não ficou muito bom, e não funcionou kkkkk.
'''
dados = [[0] * 3 for i in range(5)]
produtos = [0] * 4
maior_prod2 = 0
custo = 0
custo_armazem = [0] * 4

for col in range(3):
    for lin in range(5):
        if lin == 4:
            dados[4][col] = int(input(f'Informe o custo do produto: {col + 1}'))
        else:
            dados[lin][col] = int(input(f'Informe a quantidade do produto {col + 1} no armazém {lin + 1}: '))
            qnt_item = dados[lin][col]
            if dados[lin][1] > maior_prod2:
                maior_prod2 = dados[lin][1]
                armazem_prod2 = lin + 1

for i in range(3):
    for j in range(5):
        print(dados[j][i], end='')
    print()

#for i in range(3):
#    for j in range(4):
#        custo += dados[4][i] * dados[j][i]
#        custo_armazem[j] += dados[4][i] * dados[j][i]

for lin in range(3):
    for col in range(4):
        
      #  custo += dados[lin][5] * dados[lin][col]
        custo_armazem[col] += produtos[col] * dados[lin][4]

for lin in range(4):
    for col in range(3):
        produtos[lin] += dados[lin][col]


print('a) Cada armazém possui:', produtos, 'itens.')
print('b) O armazém com maior estoque do produto 2 é o armazém:', armazem_prod2)
print('c) O armazém com menor estoque é o armazém:', produtos.index(min(produtos)) + 1)
print('d) O custo total de cada produto é:', dados[4])
print('e) O custo total de cada armazém é:', custo_armazem)
#print('e) O custo total de cada armazém é:', produtos * dados[4])

#    dados[5][col] = int(input('Informe o custo do produto: '))


for i in range(5):
    for j in range(3):
        print(dados[i][j], end=' \t')
    print()
'''


'''
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
print(f'Custo total de cada armazém: {soma_prod1}, {soma_prod2}, {soma_prod3}')'''