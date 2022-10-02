tab = [[" "] * 3 for i in range(3)]
jogador = "X"
while True:
    for lin in range(3):
        for col in range(3):
            print(tab[lin][col],end="|")
        print()
    print("Jogador: ", jogador)
    print("Digite o numero da linha")
    lin = int(input())
    print("Digite o numero da coluna")
    col = int(input())
    #validar jogada repetida
    tab[lin-1][col-1] = jogador
    #verificar o vencedor
    #verificar se deu velha
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"