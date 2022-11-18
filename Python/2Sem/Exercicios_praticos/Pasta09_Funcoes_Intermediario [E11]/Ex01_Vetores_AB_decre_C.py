''''
1.	Faça uma função que receba dois vetores A e B de dez elementos inteiros, por parâmetro. 
O procedimento deve determinar e mostrar um vetor C que contenha os elementos de A e B em ordem decrescente.

def preenche_vetor(vetor):
    for i in range(10):
        vetor.append(int(input("Digite um número inteiro: ")))
    return vetor

def ordena_decrescente(vetor):
    vetor.sort(reverse=True)
    return vetor

def vetor_c():
    vetor_a = []
    vetor_b = []
    vetor_c = []

    vetor_a = preenche_vetor(vetor_a)
    vetor_b = preenche_vetor(vetor_b)

    vetor_c = vetor_a + vetor_b
    vetor_c = ordena_decrescente(vetor_c)

    print(vetor_c)

vetor_c()
'''
def minhafuncao(lista1:list, lista2:list):
    novalista = []
    for i in lista1:
        novalista.append(i)
    for i in lista2:
        novalista.append(i)

    for i in range(0,len(novalista)-1):

        for j in range(i+1,len(novalista)):
            if novalista[i] < novalista[j]:
                aux = novalista[i]
                novalista[i] = novalista[j]
                novalista[j] = aux
                #novalista[i], novalista[j] = novalista[j], novalista[i]
    return novalista


#dunder methods
if __name__ == '__main__':
    lista1 = [0] * 10
    lista2 = [0] * 10
    for i in range(10):
        print('Digite um número')
        lista1[i] = int(input())
    for i in range(10):
        print('Digite um número')
        lista2[i] = int(input())
    listaresultado = minhafuncao(lista1,lista2)
    print(listaresultado)