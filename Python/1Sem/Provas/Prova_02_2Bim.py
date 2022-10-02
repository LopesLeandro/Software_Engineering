#Faça um único programa na linguagem Python para calcular o lucro que um salão de festas tem durante um mês de funcionamento.
# Considere que o salão de festas funciona apenas aos sábados e domingos, portanto abre apenas 8 vezes (dias) em um mês,
# sempre acontece um evento.

#Para cada evento (utilizando bloco(s) de repetição) solicite as seguintes informações: (2.0)
#a. O dia no mês em que vai acontecer o evento;
#b. O número de pessoas que estarão no evento;

#Calcule e mostre:
#a. Considerando a tabela abaixo, defina e mostre o valor da locação. (2.0)
#+----------------------------------+--------------------+
#| Número de pessoas                | Valor da locação   |
#+----------------------------------+--------------------+
#| Caso não ultrapasse 1000 pessoas |    R$ 4500,00      |
#+----------------------------------+--------------------+
#|  Caso ultrapasse 1000 pessoas    |  R$ 5,00 reis      |
#|                                  |  por pessoa        |
#+----------------------------------+--------------------+

#b. Qual a média do valor da locação (considerando todas as locações). (2.0)
#c. Quantos eventos não ultrapassaram 1000 pessoas? (2.0)
#d. Qual o dia do mês onde ocorreu o evento com o maior número de pessoas.(2.0)
total_locacao = 0
menor_mil = 0
maior_evento = 0

for funcionamento in range(1,9):
    print('Evento:',funcionamento)
    dia_evento = int(input('Dia do mês que ocorrerá o evento:\t'))
    num_convidados = int(input('Qual o número de convidados: \t'))
    if num_convidados > 0 and num_convidados <= 1000:
        preco_locacao = 4500
        menor_mil += 1
    else:
        preco_locacao = num_convidados * 5
    total_locacao += preco_locacao
    if num_convidados > maior_evento:
        maior_evento = num_convidados
        dia_maior_evento = dia_evento
    print('a) O valor da locação será de R$ %.2f'%preco_locacao)
media_locacao = total_locacao / 8
print('________________________________________________________________________________')
print('b) A média do valor da locação será de R$ %.2f'%media_locacao)
print('c) O número de eventos que não ultrapassaram 1000 pessoas é ',menor_mil)
print('d) O dia do evento com maior número de pessoas será o dia',dia_maior_evento)
print('________________________________________________________________________________')