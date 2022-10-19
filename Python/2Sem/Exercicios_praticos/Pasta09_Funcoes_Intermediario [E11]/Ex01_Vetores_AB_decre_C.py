''''
1.	Faça uma função que receba dois vetores A e B de dez elementos inteiros, por parâmetro. 
O procedimento deve determinar e mostrar um vetor C que contenha os elementos de A e B em ordem decrescente.
'''
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