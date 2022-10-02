#REPREP7) Faça um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final,
# quantidade de parcelas e valor da parcela (valide as entradas). Considere o seguinte:
#- O preço final para compra à vista tem um desconto de 20%
#- A quantidade de parcelas pode ser: 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60.
#- Os percentuais de acréscimo seguem a tabela abaixo:
#Quantidade de Parcelas	Percentual de Acréscimo sobre o preço final
#Tabela no arquivo word.


repeat0 = True
while repeat0:
    preco_carro = float(input('Valor do veículo: \t'))
    if preco_carro < 1:
        print('Digite o valor correto.')
        repeat0 = True
    else:
        repeat0 = False
    valor_vista = preco_carro - (preco_carro * 0.20)
    print('Valor a vista: R$ %.2f'%valor_vista)
    for parcela in range(6,61,6):
        if parcela == 6:
            acrescimo = 0.03
        if parcela == 12:
            acrescimo = 0.06
        if parcela == 18:
            acrescimo = 0.09
        if parcela == 24:
            acrescimo = 0.12
        if parcela == 30:
            acrescimo = 0.15
        if parcela == 36:
            acrescimo = 0.18
        if parcela == 42:
            acrescimo = 0.21
        if parcela == 48:
            acrescimo = 0.24
        if parcela == 54:
            acrescimo = 0.27
        if parcela == 60:
            acrescimo = 0.30

        valor_final = (preco_carro * acrescimo) + preco_carro
        prestacao = valor_final / parcela
        print('Número prestações: ',parcela,'| Acrescimo:  %.2f'%acrescimo,'%','| Valor parcela: R$ %.2f'%prestacao, '| Valor final: R$ %.2f'% valor_final)
