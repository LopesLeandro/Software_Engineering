#REPPARA4) Implemente um programa para controlar o numero de crianças em uma creche. Para isso solicite o número de turmas,
#e para CADA TURMA solicite o número da sala, o numero de alunos matriculados e sexo de cada uma das crianças
#(M – Masculino, F – Feminino), valide as entradas. Calcule e apresente em tela:
#a. Número total de crianças na creche.
#b. Média de alunos considerando todas as salas.
#c. O numero da sala com o maior número de meninos.
#d. O numero da sala com o menor número de meninas.
numtotal = 0
varsexom = 'm'
varsexof = 'f'
totalm = 0
totalf = 0
salamaior = 0
salmenor = 9999999999999999
print('CALCULAR O NÚMERO DE CRIANÇAS EM UMA CRECHE')
numturmas = int(input('Quantas turmas essa creche possui?'))
for i in range(numturmas):
    numsala = int(input('Qual o número da sala: '))
    numalunos = int(input('Qual o número de alunos desta sala: '))
    if numalunos <= 1:
        sexo = int(input('Qual o sexo do aluno: [M] para masculino e [F] para feminino'))
    else:
        for n in range(numalunos):
            print('Aluno: 0', n+1)
            sexo = str(input('Qual o sexo do aluno: [M] para masculino e [F] para feminino'))
            if sexo is varsexom:
                totalm += 1

            else:
                totalf += 1
        if totalm > totalf:
            salamaior = numsala
        if totalf < totalm:
            salmenor = numsala


    numtotal += numalunos
media = numtotal / numturmas

print('1) O número total de alunos é: ', numtotal)
print('2) A média de alunos considerando todas as salas é: %.2f' % media)
print('3) O número da sala com maior número de meninos é: ', salamaior)
print('4) O número da sala com o menor número de meninas', salmenor)
