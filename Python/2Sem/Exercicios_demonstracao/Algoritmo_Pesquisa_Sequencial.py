lista = [9,8,7,5,3]

print('Digite o valor procurado')
valproc = int(input())

achei = False
for i in range(5):
    if lista[i] == valproc:
        print('Encontrei')
        achei = True
        break

if not achei:
   print('Não encontrei.')