''''
1) Faça um programa que carregue uma matriz 12 x 4 com os valores das vendas de uma loja, onde cada linha representa um mês do ano e cada coluna representa uma semana do mês. Valide a entrada impedindo que sejam digitados valores negativos. (4.0)
Calcule e mostre:
a. O total vendido em cada mês do ano, mostrando nome do mês por extenso; (2.0)
b. O total vendido pela loja no ano; (1.0)
c. O mês em que houve o maior valor em vendas. (3.0)
'''
table = [[0] * 4 for i in range (12)]
month = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
for lin in range(12):
  for col in range(4):
    repeat = True
    while repeat:
      print('Valor das vendas no mês de', month[lin], 'na semana', col+1,'somam', end=' $ ')
      table[lin][col] = float(input())
      if table[lin][col] < 0:
        print('\t Digite um valor válido')
        repeat = True
      else:
        repeat = False
print('\n')
print('       TABELA DE VENDAS   ')
print(' Sem 1| Sem 2 | Sem 3 |  Sem 4|')
sem = ['Semana 1','Semana 2','Semana 3','Semana 4']
for lin in range(12):
  for col in range(4):
    print('$', table[lin][col], end=' | ')
  print()
print('\n')
higher = table[0][0]
higher_month = month[0]
sum_year = 0
for lin in range(12):
  sum = 0
  for col in range(4):
    sum += table[lin][col]
  print('Total de vendas no mês de', month[lin],'foi R$', sum)
  sum_year += sum
  if sum > higher:
    higher = sum
    higher_month = month[lin]
print('\n')
print('Total de vendas no ano foi R$ \t', sum_year)
print('\n')
print('O Mês com maior número de vendas é', higher_month, 'com R$', higher)
print('\n')
print('FIM DO PROGRAMA')
# END!