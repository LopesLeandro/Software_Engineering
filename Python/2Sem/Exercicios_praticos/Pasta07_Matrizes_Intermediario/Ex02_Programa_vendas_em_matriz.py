''''
2)	Faça um programa que receba as vendas semanais (de um mês) de cinco vendedores de uma loja e armazene essas vendas em uma matriz. Calcule e mostre:
a.	O total de vendas do mês de cada vendedor
b.	O total de vendas de cada semana (todos os vendedores juntos)
c.	O total de vendas do mês
'''

vendedor = []
vendas_semanais = []
vendas_mes = []
matriz = [[0] * 5 for i in range(4)]

for i in range(5):
    print('Vendedor ',i+1)
    
    repete = True
    while repete:
        codigo_vendedor = int(input('Digite o código do vendedor: '))
        if codigo_vendedor > 99 and codigo_vendedor < 1000:
            vendedor.append(codigo_vendedor)
            repete = False
        else:
            print('Digite um código válido! [000]')
            repete = True
    
    for lin in range(4):
        print('Semana ', lin)
        repete2 = True
        while repete2:
            venda_semana = int(input('Digite o total das vendas desta semana do vendedor: '))
            if codigo_vendedor >= 0:
                vendas_mes.append(venda_semana)
                repete2 = False
            else:
                print('Digite um valor válido!')
                repete2 = True
contcol = 0
contlin = 0
for lin in range(5):
    print('V:', vendedor[contlin], '\t')
    contlin += 1
    for col in range(4):
        print(vendas_mes[contcol], '\t', end='')
        contcol += 1