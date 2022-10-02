#REPREP8) O sistema de avaliação de uma determinada disciplina obedece aos seguintes critérios:
#- durante o semestre são dadas três notas;
#- a nota final é obtida pela média aritmética das três notas;
#- é considerado aprovado o aluno que obtiver a nota final superior ou igual a 6 e que tiver comparecido a um mínimo de 40 aulas.
#Faça um programa que:
#- leia um conjunto de dados contendo o número da matrícula, as três notas e a frequência (número de aulas frequentadas)
# de dez alunos (valide todos os dados).
#Calcule e mostre:
# - para cada aluno o número da matrícula, a nota final e a mensagem (aprovado ou reprovado);
# - a maior e a menor nota da turma;
# - o total de alunos reprovados;
# - a percentagem de alunos reprovados por frequência abaixo da mínima necessária.
maior = 0
menor = 12
cont_reprovados = 0
frequencia_baixa = 0

for alunos in range(1,11):
    print('Aluno',alunos)
    repeat0 = True
    while repeat0:
        matricula = int(input('Digite a matricula:  '))
        if matricula <= 0:
            print('Digite uma matrícula válida')
            repeat0 = True
        else:
            repeat0 = False
    nota_total = 0
    for nota in range(3):

        repeat1 = True
        while repeat1:
            nota_aluno = float(input('Digite a nota:  '))
            if nota_aluno <= 0:
                print('Digite uma nota válida.')
                repeat1 = True
            else:
                repeat1 = False

        nota_total += nota_aluno

    media_aluno = nota_total / 3

    repeat4 = True
    while repeat4:
        frequencia = int(input('Digite a frequência do aluno: '))
        if frequencia <= 0:
            print('Digite uma frequência válida.')
            repeat4 = True
        else:
            repeat4 = False
        if frequencia < 40:
            frequencia_baixa += 1
    if nota_aluno > maior:
        maior = nota_aluno
    if nota_aluno < menor:
        menor = nota_aluno
    print('Resposta A)')
    print('Aluno Matricula: ',matricula)
    print('Nota final: %.2f'%media_aluno)
    if media_aluno >= 6 and frequencia >= 40:
        print('Aluno aprovado!')
    else:
        print('Aluno reprovado.')
        cont_reprovados += 1

    perc_freqbaixa = (frequencia_baixa / 10) * 100
print('Resposta B)')
print('A maior nota foi ', maior)
print('A menor nota foi', menor)

print('Resposta C)')
print('O total de alunos reprovados foi', cont_reprovados)

print('Resposta D)')
print('O percentual de reprovados por frequencia foi %.2f'% perc_freqbaixa)