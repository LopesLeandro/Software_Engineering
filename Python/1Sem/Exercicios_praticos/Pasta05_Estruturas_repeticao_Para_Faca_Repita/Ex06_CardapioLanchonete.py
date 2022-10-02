#REPPARA6) O cardápio de uma lanchonete é o seguinte
#Produto	Código	Preço
#Cachorro Quente	100	R$ 1,20
#Bauru Simples	101	R$ 1,30
#Bauru com Ovo	102	R$ 1,50
#Hambúrguer	103	R$ 1,20
#Cheeseburguer	104	R$ 1,30
#Refrigerante	105	R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas (valide as entradas). Calcule e mostre
#o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar
#quando o pedido deve ser encerrado.
continua = 0
total_pedido = 0

print('CARDÁPIO')
print('     Produto    | Código | Preço')
print('Cachorro-quente |   100  | R$ 1,20')
print('Bauru simples   |   101  | R$ 1,30')
print('Bauru com ovos  |   102  | R$ 1,50')
print('Hamburguer      |   103  | R$ 1,20')
print('Cheeseburguer   |   104  | R$ 1,30')
print('Refrigerante    |   105  | R$ 1,00')

while True:
    pedido = int(input('Digite o código do produto desejado: '))
    if pedido >= 100 and pedido < 106:
        quantidade = int(input('Digite a quantidade desejada: '))
        if pedido == 100 or pedido == 103:
            precoitem = quantidade * 1.20
        if pedido == 101 or pedido == 104:
            precoitem = quantidade * 1.30
        if pedido == 102:
            precoitem = quantidade * 1.50
        if pedido == 105:
            precoitem = quantidade * 1.00
        print('O preço destes itens é R$ %.2f' % precoitem, '.')
        continua = int(input('Você quer adicionar mais itens ao pedido? [1] Sim | [0] Não'))
        total_pedido += precoitem
    else:
        print('Digite o código correto')
        continue
    if continua == 0:
        break
print('O valor total do pedido é R$ %.2f' % total_pedido)