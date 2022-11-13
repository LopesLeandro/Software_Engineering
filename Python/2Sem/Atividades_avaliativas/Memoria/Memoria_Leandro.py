import random

#memoria = [' '] * 100
cabecinha = [' ', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', ' ', ' ', ' ', 'x']
opcao = 0
tamanho = 0
letra = ''
#for i in range(100):
#    if(random.randint(0,11) >= 5):
#        memoria[i] = 'x'
#    else:
#        memoria[i] = ' '
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
while(opcao != 4):
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()

    if(opcao == 1):
        #Implemente aqui a lógica da primeira escolha
        i=0
        while i < 100:
            if cabecinha[i] == " ":
                ini = i 
                j=ini+1
                while j < 100:
                    
                    if cabecinha[j] != " ":
                        fim = j
                        break
                    j += 1
                if (fim-ini) >= tamanho:
                    for cont in range(ini,ini+tamanho):
                        cabecinha[cont] = letra
                    break
            i += 1
    else:
        if (opcao == 2):
            #Implemente aqui a lógica da melhor escolha
            pass
        else:
            if(opcao == 3):
                #Implemente aqui a lógica da pior escolha
                i=0
                tamanho_ini = 0
                novo_ini = 0
                while i < 100:
                    if cabecinha[i] == " ":
                        #Encontra o primeiro espaço vazio
                        #Procura o primeiro espaço preenchido
                        
                        ini = i 
                        j=ini+1
                        
                        while j < 100:
                            
                            if cabecinha[j] != " ":
                                fim = j
                                tamanho = fim - ini
                                break
                            j += 1
                            if tamanho >= tamanho_ini:
                                tamanho_ini = tamanho
                                posicao = j - tamanho
                        
                                
                    i += 1
                cabecinha[posicao] = letra

                            #J=1
                        #pass
                        #break

                            
                            
                    
    # Aqui você deve imprimir todo o conteúdo da variável memória
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