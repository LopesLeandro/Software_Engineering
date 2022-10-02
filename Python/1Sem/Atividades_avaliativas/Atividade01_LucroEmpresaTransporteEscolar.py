# Instruções:
# Faça um único programa na linguagem Python para calcular o lucro de uma empresa de transporte que tem uma van escolar.
# Considere que o cálculo é feito para uma única semana e que as vans trabalham de segunda a sábado, para cada dia de
# trabalho solicite (utilizando bloco(s) de repetição) (2.0):

# a.    O número total de passageiros transportados.
# b.    A KM realizada no dia de trabalho.

# Calcule e mostre:
# a.    Qual dia da semana foi transportado o maior número de passageiros e o menor número de passageiros. (2.0)
# b.    A média de KM rodados, considerando o total de KM da semana pelo número de dias de uma semana de trabalho. (2.0)
# c.    O número de dias na semana em que a van transportou mais de 50 passageiros no dia. (1.0)
# d.    O lucro da empresa na semana, considerando que a empresa recebe R$14,00 reais por passageiro, a van tem uma média
# de consumo de um litro a cada 11km e o combustível custa R$ 6.90 o litro. (3.0).
maior = 0
menor = 0
km_rodado_semana = 0
dias_lotado = 0
total_passageiros_semana = 0
for rotina in range(1, 7):
    def segunda():
        return "Segunda-Feira"

    def terca():
        return "Terça-feira"

    def quarta():
        return "Quarta-feira"

    def quinta():
        return "Quinta-feira"

    def sexta():
        return "Sexta-feira"

    def sabado():
        return "Sábado"

    switcher = {
        1: segunda,
        2: terca,
        3: quarta,
        4: quinta,
        5: sexta,
        6: sabado, }

    def switch(dia_semana):
        return switcher.get(dia_semana)()

    print(switch(rotina))

    num_passageiros = int(input('Digite o número de passageiros: '))
    if num_passageiros > 50:
        dias_lotado += 1
    km_rodado_dia = float(input('Digite os kms rodados: '))

    if num_passageiros > maior:
        maior = num_passageiros
        dia_maior = (switch(rotina))

    if rotina == 1:
        menor = num_passageiros
        dia_menor = (switch(rotina))
    if num_passageiros < menor:
        menor = num_passageiros
        dia_menor = (switch(rotina))

    km_rodado_semana += km_rodado_dia
    total_passageiros_semana += num_passageiros

custo = (km_rodado_semana / 11) * 6.90
media_rodado = km_rodado_semana / 6
faturamento = total_passageiros_semana * 14
lucro = faturamento - custo

print('a)')
print('Dia com maior número de passageiros: ', dia_maior)
print('Dia com menor número de passageiros: ', dia_menor)
print('b)')
print('A média de km rodados da semana é: ', media_rodado)
print('c)')
print(dias_lotado, ' é o número de dias que a van transportou mais de 50 pessoas')
print('d)')
print('O lucro semanal da empresa é de R$ %.2f' % lucro)