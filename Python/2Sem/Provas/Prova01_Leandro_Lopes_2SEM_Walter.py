lista_cep = [0] * 3 
lista_orcamento = [0] * 3
lista_situacao = [0] * 3
# A lista foi feita com 3 para facilitar os testes

for i in range(3):
    num_cep = int(input('Digite o CEP: '))
    orcamento = float(input('Digite o valor do orçamento: R$')) 
    lista_cep[i] = num_cep
    lista_orcamento[i] = orcamento
    repete = True
    while repete:
        situacao = int(input('Informe se o trabalho foi realizado. (1- Realizado | 0- Não realizado): '))    
        if situacao != 0 and situacao != 1:
            print('Digite uma opçao válida!')
            repete = True
        else:
            lista_situacao[i] = situacao
            repete = False

#MENU PROGRAMA
opcao = 0
while(opcao != 4):
    print('#######################')
    print('1 - Listar agendamentos')
    print('2 - Montante recebido')
    print('3 - Maior e menor orçamento')
    print('4 - Sair do programa')
    print('#######################')
    opcao = int(input('Digite uma opção: '))
#1 - LISTAR ATENDIMENTOS AGENDADOS (MOSTRAR TODOS OS AGENDAMENTOS = CEP + ORÇAMENTO)
    if opcao == 1:
        print('Os CEPs da agenda de hoje são: \t', lista_cep)
        print('Os orçamentos de hoje são: \t', lista_orcamento)
#2 - CALCULAR O MONTANTE RECEBIDO NO DIA QUANDO SERVIÇO REALIZADO (R$ QUANDO 1)
    if opcao == 2:
        soma = 0
        for i in range(3):
            if lista_situacao[i] == 1:
                soma += lista_orcamento[i]
        print("Valor recebido hoje: R$ ", soma)
#3 - ENCONTRAR O CEP DO ORÇAMENTO MAIS CARO E MAIS BARATO (MOSTRAR JUNTO O CEP)
    if opcao == 3:
        maior_valor = lista_orcamento[0]
        cep_maior = lista_cep[0]
        menor_valor = lista_orcamento[0]
        cep_menor = lista_cep[0]
        
        for i in range(3):
            if maior_valor < lista_orcamento[i]:
                maior_valor = lista_orcamento[i]
                cep_maior = lista_cep[i]
            
            if menor_valor > lista_orcamento[i]:
                menor_valor = lista_orcamento[i]
                cep_menor = lista_cep[i]
            
        print("O maior orçamento é: R$ ", maior_valor, " no endereço CEP: ", cep_maior)
        print("O menor orçamento é: R$ ", menor_valor, " no endereço CEP: ", cep_menor)
#4 - SAIR DO PROGRAMA
print("Adeus!")