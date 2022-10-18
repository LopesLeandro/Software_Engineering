''''
4)	Faça uma função que receba cinco valores inteiros, e retorne o maior valor. 
Faça uma segunda função que receba também cinco valores e retorne o menor deles.
'''

def valores():
    lista = []
    for i in range(5):
        lista.append(int(input('Digite um valor: ')))
    maior = max(lista)
    menor = min(lista)
    return lista,maior,menor

#def maior():
#    maior = max.valores(lista)
#    return maior
print(valores())
#print('A lista de valores é: ',valores()[0])
#print('O maior valor é: ',maior())
#print(valores())
#print('A lista é: ',valores()[0], 'O maior valor é: ',valores()[1], 'O menor valor é: ',valores()[2])