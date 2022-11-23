import random

cabecinha = [' '] * 100
#cabecinha = [' ', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', ' ', ' ', ' ', 'x']
opcao = 0
tamanho = 0
letra = ''
for i in range(100):
    if(random.randint(0,11) >= 5):
        cabecinha[i] = 'x'
    else:
        cabecinha[i] = ' '

#Aqui você deve imprimir todo o conteúdo da variável memória
for i in range(0,20):
    print(cabecinha[i],end="|")
print()
for i in range(20,40):
    print(cabecinha[i],end="|")
print()
for i in range(40,60):
    print(cabecinha[i],end="|")
print()
for i in range(60,80):
    print(cabecinha[i],end="|")
print()
for i in range(80,100):
    print(cabecinha[i],end="|")
print()

#Inicio do loop do menu do programa
while(opcao != 4):
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    if opcao == 4:
        print('Saiu')
        break
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()

    if(opcao == 1):
        #Implemente aqui a lógica da primeira escolha
        i=0
        espaco = 0
        while i < 100:
            if cabecinha[i] == " ": #inicia a localização da primeira casa vazia vazia
                ini = i 
                j=ini+1
                while j < 100:
                    
                    if cabecinha[j] != " ": #procura primeiro indexador preenchido
                        fim = j #coleta posição na lista 
                        espaco = fim - ini #new
                        break
                    
                    j += 1
                if (fim-ini) >= tamanho: #verifica se o espaço é suficiente para alocar a informação
                    for cont in range(ini,ini+tamanho): #Percorre entre o inicio e fim utilizando o inicio + o tamanho da informação para preencher a memoria
                        cabecinha[cont] = letra #coloca a letra escolhida 
                    break
            i += 1
        if tamanho > espaco: #Se não tiver espaço em lugar algum ele invalida a tentativa e apresenta a mensagem
            print('Tente uma informação menor, esta não cabe em lugar nenhum!')

    if (opcao == 2):
        #Implemente aqui a lógica da melhor escolha
        i=0
        melhor_espaco = 0
        omenor = len(cabecinha) #o menor recebe a maior largura disponível, o tamanho da memória
        espaco = 0
        while i < 100:
            if cabecinha[i] == " ": #inicia a localização da primeira casa vazia vazia
                ini = i
                j = ini + 1 #o próximo while não inicia em uma informação já conhecida
                
                while j < 100: #localiza a primeira casa preenchida
                    if cabecinha[j] != " ": #procura primeiro indexador preenchido
                        fim = j 
                        espaco = fim - ini #Armazena o tamanho do espaço
                            
                        if espaco < omenor and espaco >= tamanho: #Valida se o espaço é menor que o espaço já armazenado no omenor, e também se é um espaço util igual ou maior que a informação que se quer guardar
                            melhor_espaco = espaco #armazena o melhor espaço
                            pos_melhor_ini = i #armazena a posição do inicio do melhor espaço
                    
                            if melhor_espaco < omenor: 
                                omenor = melhor_espaco #Coleta o menor espaço até o momento
                                omenor_ini = i #Coleta a posição inicial do menor espaço
                        else:
                            i = j # inicio recebe o fim para o próximo ciclo
                            break
                    j += 1
            i += 1 # +1 no i para pegar uma casa desconhecida
            #A partir daqui os comentários ficariam muito repetitivos.
        if tamanho > melhor_espaco:  
            print('Tente uma informação menor, esta não cabe em lugar nenhum!')
        else:
            for cont in range(tamanho):
                cabecinha[omenor_ini+cont] = letra
     
    if (opcao == 3):
        #Implemente aqui a lógica da pior escolha
        i=0
        maior_espaco = 0
        while i < 100:
            if cabecinha[i] == " ":
                ini = i
                j = ini + 1
                while j < 100:
                    if cabecinha[j] != " ":
                        fim = j
                        espaco = fim - ini
                        if espaco > maior_espaco: #a mesma lógica só que pegando o maior espaço para ser a pior opção
                            maior_espaco = espaco #armazena o maior espaco ate o momento aqui
                            pos_maior_ini = ini #coleta a posicao onde o maior espaco começa
                        break
                    #i = j  
                    j += 1
            i += 1
        if maior_espaco >= tamanho:
            for cont in range(pos_maior_ini,pos_maior_ini+tamanho):
                cabecinha[cont] = letra
        else:
            print('Tente uma informação menor, esta não cabe em lugar nenhum!')

    for i in range(0,20):
        print(cabecinha[i],end="|")
    print()
    for i in range(20,40):
        print(cabecinha[i],end="|")
    print()
    for i in range(40,60):
        print(cabecinha[i],end="|")
    print()
    for i in range(60,80):
        print(cabecinha[i],end="|")
    print()
    for i in range(80,100):
        print(cabecinha[i],end="|")
    print()
