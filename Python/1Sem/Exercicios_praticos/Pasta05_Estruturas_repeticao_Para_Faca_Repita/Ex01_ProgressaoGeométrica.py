#REPPARA1) Calcule e apresente a PROGRESSÃO GEOMÉTRICA dos 200 próximos números de 1 considerando o quociente 4.
cont = 0
prog = 0

prog = int(input("Digite um número: "))
while cont < 200:
    prog = prog * 4
    print(prog, " ", end="")
    cont += 1