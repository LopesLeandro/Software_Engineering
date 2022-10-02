'''
VETORES6 - Faça um programa que simule um controle bancário. Para tanto, devem ser lidos os códigos de dez contas e os seus respectivos saldos. 

Os códigos devem ser armazenados em um vetor de números inteiros (não pode haver mais que uma conta com o mesmo código) e os saldos devem ser armazenados em um vetor de números reais. O saldo deverá ser cadastrado na mesma posição do código. Por exemplo, se a conta 504 for armazenada na quinta posição do vetor de saldos. Depois de fazer a leitura dos valores, mostrar o seguinte menu na tela:

i.	Efetuar depósito
ii.	Efetuar saque
iii.	Consultar o ativo bancário (ou seja, o somatório dos saldos de todos os clientes)
iv.	Finalizar o programa

Para efetuar depósito deve-se solicitar o código da conta e o valor a ser depositado. Se a conta não estiver cadastrada, mostrar a mensagem Conta não encontrada e voltar ao menu. Se a conta existir, atualizar o seu saldo.


Para efetuar saque deve-se solicitar o código da conta e o valor a ser sacado. Se a conta não estiver cadastrada, mostrar a mensagem Conta não encontrada e voltar ao menu. 
    Se a conta existir, verificar se o seu saldo é suficiente para cobrir o saque. (Estamos supondo que a conta não pode ficar com o saldo negativo). 
    Se o saldo for suficiente, realizar o saque e voltar ao menu. Caso contrário mostrar a mensagem Saldo insuficiente e voltar ao menu.

Para consultar o ativo bancário deve-se somar o saldo de todas as contas do banco. Depois de mostrar esse valor, voltar ao menu.
O programa só termina quando for digitada a opção 4 – Finalizar o programa.

'''
opcao = 0
valorTotalContas = 0

listaContas = [0] * 10
listaSaldos = [0] * 10
#listaContas = [1234, 2345, 3456, 4567] PARA TESTE
#listaSaldos = [10, 20, 30, 40] PARA TESTE


#CADASTRO DAS CONTAS
contador = 0

while contador < len(listaContas):
  print("Insira a conta", contador+1)
  numConta = int(input())
  print()

  validaConta = False
  for n in range(len(listaContas)):
    if listaContas[n] == numConta:
      validaConta = True
      print("CONTA REPETIDA")
      break

  if not validaConta:
    listaContas[contador] = numConta

    print("Digite o saldo da conta:")
    saldoConta = float(input())
    listaSaldos[contador] = saldoConta
    print()
  
    contador += 1
      

print("CONTAS: ",listaContas)
print("SALDOS: ",listaSaldos)
print()



while opcao != 4:
  print("Sistema Bancário")
  print("1.	Efetuar depósito")
  print("2.	Efetuar saque")
  print("3.	Consultar o ativo bancário")
  print("4.	Finalizar o programa")
  print("Digite o num da opção:")
  opcao = int(input())
  if opcao < 0 or opcao > 4:
    print("OPÇÃO INVALIDA, DIGITE NOVAMENTE \n")

  validaConta = True
  localConta = 0

  #DEPOSITO
  if opcao == 1:
    numConta = int(input("Digite o número da conta: "))

    for i in range(len(listaContas)):
      if listaContas[i] == numConta:
        validaConta = False
        localConta = i

    if not validaConta:
      print()
      print("Saldo Atual: R$%.2f" % listaSaldos[localConta])
      valorDeposito = float(input("Digite o valor do depósito: R$ "))
      listaSaldos[localConta] += valorDeposito
      print()
      print("DEPOSITO EFETUADO")
      print("Saldo Atual: R$%.2f" % listaSaldos[localConta])
      print()
    else:
      print("Conta não encontrada")
      print()

  #SAQUE
  if opcao == 2:
    numConta = int(input("Digite o número da conta: "))
    print()

    validaConta = True
    for n in range(len(listaContas)):
      if listaContas[n] == numConta:
        localConta = n
        validaConta = False
        break

    if not validaConta:
      print("Saldo Atual: R$%.2f" % listaSaldos[localConta])
      saldoConta = float(input("Digite o valor do saque: R$"))
      print()
      if saldoConta <= listaSaldos[localConta]:
        listaSaldos[localConta] -= saldoConta
        print("SAQUE EFETUADO")
        print("Saldo Atual: R$%.2f" % listaSaldos[localConta])
        print()
      else:
        print("Saldo Insuficiente")
        print()
    else:
      print("Conta não encontrada")
      print()
    
  #ATIVO BANCARIO
  if opcao == 3:
    for k in range(len(listaContas)):
      valorTotalContas += listaSaldos[k]

    print("Valor total das contas cadastradas: R$%.2f" % valorTotalContas)
    print()
 
print(listaSaldos)
print("OPERAÇÃO ENCERRADA")