''''
4)	Faça um programa que carregue uma matriz 10x3 com as notas de dez alunos em três provas. 
Mostre um relatório com o número do aluno (número da linha) e a prova em que cada aluno obteve menor nota. 
Ao final do relatório, mostre quantos alunos tiveram menor nota na prova 1, quantos alunos tiveram menor nota na prova 2 e quantos alunos tiveram menor nota na prova 3.
'''

table = [[0] * 3 for i in range(11)]
#armazem = [0] * 4
#maior_produto = 0
#menor_produto = 9999
#custo_armazem = [0] * 4
contador = 0
linha = -1

#Constroi a matriz
for lin in range(10):
    linha += 1
    for col in range(3):
            table[lin][col] = int(input(f'Digite a nota da prova {col+1} do aluno {linha+1}: '))
    print()

linha = 0
for lin in range(10):
    linha += 1
    if linha >= 1:
        print('A:',linha, end=' \t |')
    else:
        print('Prova:', end=' \t |')
    menor_nota = 10
    for col in range(3):
        if lin == 0:
            print(col + 1, end='\t')
        else:
            print(table[lin][col], end=' \t')
    print()



def menor_nota ():
    linha = 0
    alunos_prova_1 = 0
    alunos_prova_2 = 0
    alunos_prova_3 = 0
    s_prova = [0] * 3
    for lin in range(10):
        linha += 1
        menor_nota = 10
        for col in range(3):
            if table[lin][col] < menor_nota:
                menor_nota = table[lin][col]
                coluna = col + 1
        if coluna == 1:
            alunos_prova_1 += 1
        if coluna == 2:
            alunos_prova_2 += 1
        if coluna == 3:
            alunos_prova_3 += 1
            


        print(f'O aluno {linha} teve a menor nota na prova {coluna}')
    print(f'Alunos com menor nota na prova 1: {alunos_prova_1}')
    print(f'Alunos com menor nota na prova 2: {alunos_prova_2}')
    print(f'Alunos com menor nota na prova 3: {alunos_prova_3}')
    #print(f'O número de alunos com a menor nota na prova 1 é {s_prova[0]} , na prova 2 foram {s_prova[1]}, e na prova 3 foram {s_prova[2]}')
    
    
menor_nota()

'''
                    alunos_prova_1 += 1
                if menor_nota == 2:
                    alunos_prova_2 += 1
                if menor_nota == 3:
                    alunos_prova_3 += 1
'''





#Matriz solicitando informações conforme enunciado do exercício:
#for lin in range(5):
#    for col in range(3):
#        if lin == 4:
#            dados[lin][col] = float(input(f'Informe o custo do produto {col+1}: '))
#        else:
#            dados[lin][col] = int(input(f'Informe a quantidade do produto {col+1} no armazém {lin+1}: '))
#        
#for lin in range(10):
#    for col in range(3):
#        print(table[lin][col], end=' \t')
#    print()

