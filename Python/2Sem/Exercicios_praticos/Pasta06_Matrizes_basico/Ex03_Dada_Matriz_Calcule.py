''''
3)	Dada a seguinte matriz, calcule:
- A soma dos elementos de primeira coluna;
- O produto dos elementos da primeira linha;
- A soma de todos os elementos;
- O produto da diagonal principal.
'''

tab = [[0] * 4 for i in range(4)]
soma_tudo = 0
contador = 0
linha_a = []
col_a = []
soma_lin = 0
soma_col = 0
#contador_par = 0
for lin in range(4):
    for col in range(4):
        tab[lin][col] = contador
        print(tab[lin][col], end=" \t")
        contador += 1
        soma_tudo += tab[lin][col]
        #if lista[lin][col] % 2 == 0:
        #    num_z = lista[lin][col]
        #    pares.append(num_z)
        #    contador_par += 1
        if lin <= 0:
            soma_lin += tab[lin][col]
            linha_a.append(tab[lin][col])
    print()
    
    soma_col += tab[lin][0]
    col_a.append(tab[lin][0])




print('-' * 58)
print('| a) A soma dos elementos da primeira coluna é: ', soma_col, '\t |')
print('| a.1) Os elementos dessa soma são: ', col_a, '\t |')
print('-' * 58)
print('| b) A soma dos elementos da primeira linha é: ', soma_lin, '\t |')
print('| b.1) Os elementos dessa soma são: ', linha_a, '\t |')
print('-' * 58)
print('| c) A soma de todos os elementos é: ', soma_tudo, '\t \t |')
print('-' * 58)
#####