#1) Faça um programa que receba duas notas de seis alunos, calcule e mostre:
#- Média aritmética das duas notas de cada aluno;
#- A mensagem que esta na tabela a seguir:
#+--------------------+--------------+
#|Média Aritmética    |   Mensagem   |
#+--------------------+--------------+
#|     até 3.0        |   Reprovado  |
#|  entre 3.0 e 7.0   |   Exame      |
#|    Acima de 7.0    |   Aprovado   |
#+--------------------+--------------+
#Ao final:
#- O total de alunos aprovados;
#- O total de alunos em exame;
#- O total de alunos reprovados;
#- A média da classe.

contaprov = 0
contreprov = 0
contexame = 0
for aluno in range(6):
    print("Digite a primeira nota")
    nota1 = float(input())
    print("Digite a segunda nota")
    nota2 = float(input())
    media = (nota1 + nota2) / 2
    print("A media e ", media)
    if media < 3:
        print("Reprovado")
        contreprov += 1
    else:
        if media >= 3 and media < 7:
            print("Exame")
            contexame += 1
        else:
            print("Aprovado")
            contaprov += 1
    # fim do IF

# fim FOR
print("A qtd de reprovados e ", contreprov)
print("A qtd de aprovados e ", contaprov)
print("A qtd de exames ", contexame)