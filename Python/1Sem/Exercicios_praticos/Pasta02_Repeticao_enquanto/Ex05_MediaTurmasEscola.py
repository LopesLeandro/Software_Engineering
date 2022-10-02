#REPENQ5) Faça um algoritmo que calcule a média de todas as turmas de uma escola. Considere como entradas o número de turmas
# e o número de alunos de cada turma. A média de cada turma deve ser apresentada, além da média geral, que será o resultado
# da média das turmas.

numturmas = int(input("Digite o número de turmas: "))
somamedias = 0
mediaescola = 0
for turma in range(numturmas):
    print("Turma:", turma+1)
    print("Digite a quantidade de alunos: ")
    numalunos = int(input())
    somaturma = 0
    for aluno in range(numalunos):
        print("\tAluno: ",aluno+1)
        print("\tDigite a média do aluno: ")
        mediaaluno = float(input())
        somaturma += mediaaluno
        #aquiohh
    mediaturma = somaturma / numalunos
    print("A média da turma é ", mediaturma)
    somamedias += mediaturma
    mediaescola = somamedias / numturmas
print("A média da escola é ", mediaescola)