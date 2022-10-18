''''
3)	Faça uma função que receba as três notas de um aluno como parâmetro e uma letra. 
Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se for P o procedimento calcula a média ponderada com os pesos 5,3 e 2. 
A média calculada deve ser devolvida ao programa principal para, então, ser mostrada.
'''
#It works!
def media_aritmetica(nota_a,nota_b,nota_c):
    media_art = (nota_a + nota_b + nota_c) / 3
    return media_art

def media_ponderada(nota_a,nota_b,nota_c):
    media_pond = ((nota_a * 5) + (nota_b * 3) + (nota_c * 2)) / 10
    return media_pond

def main():
    nota_a = float(input('Digite a primeira nota: '))
    nota_b = float(input('Digite a segunda nota: '))
    nota_c = float(input('Digite a terceira nota: '))
    letra = str(input('Digite a letra A ou P: '))
    if letra == 'A':
        media = float(media_aritmetica(nota_a,nota_b,nota_c))
    if letra == 'P':
        media = float(media_ponderada(nota_a,nota_b,nota_c))
    return media

print(main())

'''
def coleta_notas(nota_a:float,  nota_b:float, nota_c:float):
    nota_a = float(input('Digite a primeira nota: '))
    nota_b = float(input('Digite a segunda nota: '))
    nota_c = float(input('Digite a terceira nota: '))
    return nota_a, nota_b, nota_c
    #if letra == 'A':
    #    media = coleta_notas() / 3
    #if letra == 'P':
    #    media = media_ponderada(nota_a,nota_b,nota_c)
    #return media
#print(coleta_notas())
#letra = str(input('Digite a letra A ou P: '))
#if letra == 'A':
#    media = coleta_notas(nota_a, nota_b, nota_c) / 3
'''
'''
print(f'Notas 1, 2 e 3: {coleta_notas()}')
letra = str(input('Digite a letra A ou P: '))
if letra == 'A':
    print(f'Média aritmética: {coleta_notas(media_aritmetica())}')
if letra == 'P':
    print(f'Média ponderada: {media_ponderada}')
'''


'''
def f (nota_a:float, nota_b:float, nota_c:float):
    letra = str(input('Digite a letra A ou P: '))
    if letra == 'A':
        media_aritimetica = (nota_a + nota_b + nota_c) / 3
        print(f('A média aritmética é: {media_aritimetica}'))
    if letra == 'P':
        media_ponderada = ((nota_a * 5) + (nota_b * 3) + (nota_c * 2)) / 3
        print(f('A média ponderada é: {media_ponderada}'))
    return media_aritimetica,media_ponderada

#nota_a = float(input('Digite a nota 1: '))
#nota_b = float(input('Digite a nota 2: '))
#nota_c = float(input('Digite a nota 3: '))
print(f'Notas 1, 2 e 3 deste aluno:  {(nota_a)}, {nota_b()},  {nota_c()}')
print(f'A média aritmética é: {media_aritimetica}')

''''''

#print(f('A média aritmética do aluno é: {media_aritimetica}'))
#print(f('A média ponderada do aluno é: {media_ponderada}'))
'''
