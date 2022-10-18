''''
2)	Faça uma função que transforme e mostre segundos em horas, minutos e segundos. 
Todas as variáveis devem ser passadas como parâmetro, não havendo variáveis globais.
a.	1h = 3600s
b.	1m = 60s
'''
valor_segundos = int(input('Digite o valor de segundos: '))
def funcao_conversor (segundos:int):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60


print(funcao_conversor('{horas}: {minutos}: {segundos}'))

print(funcao_conversor(valor_segundos))