''''
3)	Faça uma função que receba as três notas de um aluno como parâmetro e uma letra. 
Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se for P o procedimento calcula a média ponderada com os pesos 5,3 e 2. 
A média calculada deve ser devolvida ao programa principal para, então, ser mostrada.
'''

def f (nota_a:float, nota_b:float, nota_c:float):
    letra = input('Digite a letra A ou P: ')
    if letra == 'A':
        media_aritimetica = (nota_a + nota_b + nota_c) / 3
    if letra == 'P':
        media_ponderada = ((nota_a * 5) + (nota_b * 3) + (nota_c * 2)) / 3
    return media_aritimetica,media_ponderada

nota_a = float(input('Digite a nota 1: '))
nota_b = float(input('Digite a nota 2: '))
nota_c = float(input('Digite a nota 3: '))
print('Notas 1, 2 e 3 deste aluno: ', nota_a,', ', nota_b,', ',  nota_c)




#print(f('A média aritmética do aluno é: {media_aritimetica}'))
#print(f('A média ponderada do aluno é: {media_ponderada}'))

