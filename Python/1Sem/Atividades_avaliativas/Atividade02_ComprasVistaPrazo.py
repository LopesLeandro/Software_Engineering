#Instruções: Uma loja utiliza o código V para transação à vista e P para transação a prazo.
# Faça um programa que receba o código e o valor de quinze transações, calcule e mostre:
#a.    O valor total das compras à vista;
#b.    O valor total das compras à prazo;
#c.    O valor total das compras efetuadas;
#d.    O valor da primeira prestação das compras a prazo, sabendo-se que serão pagas em três vezes;
total_vista = 0
total_prazo = 0
valor_total = 0

for transacao in range(1,16):
    print('---------------------------------------------------------')
    print('TRANSAÇÃO: ', transacao)
    repeat0 = True
    while repeat0:
        tipo = str(input('Selecione: Compra a vista [V]  | Compra a prazo [P]: '))
        if tipo != 'V' and tipo != 'P':
            print('Tipo de compra errado, tente novamente!')
            repeat0 = True
        else:
            repeat0 = False
            repeat1 = True
            while repeat1:
                valor_compra = float(input('Valor da compra: R$ '))
                if valor_compra <= 0:
                    print('Digite um valor válido!')
                    repeat1 = True
                else:
                    repeat1 = False
            if tipo == 'V':
                total_vista += valor_compra
            if tipo == 'P':
                total_prazo += valor_compra
                valor_parcela = valor_compra / 3
                print('O valor da 1º parcela será de R$ %.2f'% valor_parcela)

    valor_total += valor_compra
print('##########################################################')
print('Total de compras a vista: R$ %.2f'% total_vista)
print('Total de compras a prazo: R$ %.2f' % total_prazo)
print('O valor total de todas as compras R$ %.2f'% valor_total)
print('##########################################################')