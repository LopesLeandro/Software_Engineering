''''
5.	Crie uma função que receba como parâmetro a hora de início e a hora de término de um jogo, ambas subdivididas em dois valores distintos: horas e minutos. 
A função deverá retornar a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.
'''

def f_tempo_jogo(hora_inicio, minuto_inicio, hora_fim, minuto_fim):
    if hora_inicio == hora_fim:
        return minuto_fim - minuto_inicio
    else:
        if hora_fim < hora_inicio:
            return (((hora_inicio - hora_fim) * 60) - 1440) * -1 + (minuto_fim - minuto_inicio)
        return (hora_fim - hora_inicio) * 60 + (minuto_fim - minuto_inicio)

def calc():
    hora_inicio = int(input('Digite a hora de início: '))
    minuto_inicio = int(input('Digite os minutos de início: '))
    hora_fim = int(input('Digite a hora de término: '))
    minuto_fim = int(input('Digite os minutos de término: '))
    print(f'A duração do jogo foi de {f_tempo_jogo(hora_inicio, minuto_inicio, hora_fim, minuto_fim)} minutos.')

calc()