#Faça um programa na linguagem Pythonpara gerenciar os volumes de lixo processados por uma empresa de reciclagem.
# Considere que em um dia a empresa recebe 8 caminhões de lixo reciclável, para cada um dos caminhões solicite: (2.0):
#  a.    Peso em quilogramas;
#  b.    Tipo do material que está no caminhão (D – Doméstico, I – Industrial);

#Calcule e mostre:
#a.    O tempo, em horas, que será necessário para processar o material em cada caminhão considerando a tabela abaixo:(2.0)
#+------------+----------------------------------+----------------------+
#| Tipo       | Peso                             | Tempo                |
#+------------+----------------------------------+----------------------+
#|            |  Mais de 8 toneladas             | 2 horas por tonelada |
#+ Industrial +----------------------------------+----------------------+
#|            |  Menos de 8 toneladas (inclusive)| 1 hora por tonelada  |
#+------------+----------------------------------+----------------------+
#|            |  Até 3 toneladas (inclusive)     | 4 horas              |
#+  Doméstico +----------------------------------+----------------------+
#|            |  Mais de 3 toneladas             | 7 horas              |
#+------------+----------------------------------+----------------------+

#b.    A média do peso de todos os caminhões com lixo do tipo doméstico. (2.0)

#c.    O número de caminhões, do tipo de material industrial, que tiveram seu tempo necessário para processar o material
# entre 24 e 48 horas. (2.0)

#d. O tipo do material do caminhão com o menor peso e o tipo do material do caminhão com o maior peso? (2.0)

peso_dom = 0
peso_total = 0
num_caminhoes = 0
maior = 0
menor = 9999999999
cam = 0
cont_dom = 0
for caminhao in range(1,9,1):
    print('Caminhão:',caminhao)
    peso = int(input('Peso em quilogramas do caminhão: '))
    tipo_material = str(input('Tipo de material: Doméstico [D]  |  Industrial [I]:'))
    if tipo_material == 'D' and peso > 3000:
        tempo_processa = 7
        peso_dom += peso
        cont_dom += 1
    if tipo_material == 'D' and peso <= 3000:
        tempo_processa = 4
        peso_dom += peso
        cont_dom += 1
    if tipo_material == 'I' and peso > 8000:
        tempo_processa = (peso / 1000) * 2
        if tempo_processa >= 24 and tempo_processa <= 48:
            num_caminhoes += 1
    if tipo_material == 'I' and peso <= 8000:
        tempo_processa = peso / 1000
    print('Horas necessárias para descarregar %.2f' % tempo_processa)
    if peso > maior:
        maior = peso
        tipo_pesado = tipo_material
    if peso < menor:
        menor = peso
        tipo_leve = tipo_material

media = peso_dom / cont_dom
print('------------------------------------------------------------------------')
print('Média de peso dos caminhões com lixo doméstico é %.2f'% media,'kg.')
print('O número de caminhões que precisaram entre 24h e 48h para descarregar é', num_caminhoes)
print('Tipo do material no caminhão mais leve é ',tipo_leve)
print('Tipo do material no caminhão mais pesado é ',tipo_pesado)