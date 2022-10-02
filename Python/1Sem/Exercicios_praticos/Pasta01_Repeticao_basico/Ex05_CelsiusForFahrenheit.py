#5) Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit,
# de 10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius.
# O programa deverá apresentar os valores das duas temperaturas.

celsius = 0
fahrenheit = 0

while celsius < 100:
    celsius += 10
    fahrenheit = (celsius * 1.8) + 32
    print(celsius, "celsius é equivalente dizer em Fahrenheit que estamos em", fahrenheit)