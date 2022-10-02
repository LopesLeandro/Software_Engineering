#REPPARA8) Um representante de vendas atende mensalmente 8 clientes recebendo os pedidos solicitados por eles.
# Para cada um dos clientes são informadas as seguintes no pedido:
# a)  Tipo do cliente (E – Especial, C – Comum)
# b) O número de tipos de produtos que o cliente deseja. Considere que o representante vende até 3 tipos diferentes de produtos.
# c) A quantidade para cada um dos tipos de produto. teste
# d) E o percentual de comissão que será cobrado pelo representante.
#OBS: Realize a validação das entradas acima, caso o usuário informe um valor incorreto, apresente uma mensagem de erro e solicite novamente.
#Calcule e mostre:
#- Dentre os 8 clientes quantos são do tipo ESPECIAL e quantos são do tipo COMUM.
#- Qual cliente solicitou a maior quantidade de produtos dentre os 8 atendidos.
#- Qual a média do total da quantidade de produtos dos pedidos realizados pelos clientes.
#- Considerando a tabela abaixo:
#Tipo Produto	Preço Unitário
#1	R$ 3,00
#2	R$ 9,00
#3	R$ 10,00
#Qual o valor total do pedido de cada um dos clientes?
#- Qual o valor total de comissão que o representante irá receber?
cliente = 0
especial = 0
comum = 0
maior = 0
q_cliente = 0
qnt_total = 0
total_num_produtos = 0
preco_todos = 0
comissao_total = 0
while cliente < 2:
    cliente += 1
    print('Cliente', cliente)
    tipo_cliente = str(input('Tipo do cliente: [E] Especial | [C] Comum'))
    if tipo_cliente == 'E':
        especial += 1
    else:
        if tipo_cliente == 'C':
            comum += 1
    if tipo_cliente == 'E' or tipo_cliente == 'C':
        num_produtos = int(input('Quantos tipos de produto deseja? De 1 a 3.'))
        if num_produtos != 1 or num_produtos != 2 or num_produtos != 3:
            total_num_produtos += num_produtos

            for produto in range(num_produtos):
                sel_produto = int(input('Qual produto:'))

                if sel_produto == 1:
                    preco = 3
                if sel_produto == 2:
                    preco = 9
                if sel_produto == 3:
                    preco = 10
                qnt_produtos = int(input('Quantidade deste produto: '))
                qnt_total += qnt_produtos
                preco_total = preco * qnt_produtos
                preco_todos += preco_total
                print('O total do pedido é R$: %.2f'% preco_total)
                comissao = int(input('Qual o percentual de comissão: '))
                cal_comissao = preco_total * (comissao/100)
                comissao_total += cal_comissao
                if qnt_produtos > maior:
                    maior = qnt_produtos
                    q_cliente = cliente
        else:
            print('Digite a informação corretamente.')
            cliente -= 1
            continue

    else:
        print('Digite a informação corretamente.')
        cliente -= 1
        continue


    media_quantidade = qnt_total / total_num_produtos

print('São do tipo Especial: ', especial, 'e do tipo Comum: ', comum, 'clientes.')
print('O cliente que pediu a maior quantidade de produtos é o cliente numero: ', q_cliente)
print('A media do total é: ', media_quantidade)
print('O total de comissão a receber é R$: %.2f'% comissao_total)
