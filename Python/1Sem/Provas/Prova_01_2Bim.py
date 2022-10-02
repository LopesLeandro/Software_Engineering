#PROVA LEANDRO LOPES EM 26/05/2022

print("Turno 1")
print("Linha 1")
codproduto11 = int(input("Código numérico do produto: #"))
quantidade11 = int(input("Informe a quantidade produzida: "))
refulgo11 = int(input("Informe o total de refulgo: "))

print("Linha 2")
codproduto12 = int(input("Código numérico do produto: #"))
quantidade12 = int(input("Informe a quantidade produzida: "))
refulgo12 = int(input("Informe o total de refulgo: "))

print("Linha 3")
codproduto13 = int(input("Código numérico do produto: #"))
quantidade13 = int(input("Informe a quantidade produzida: "))
refulgo13 = int(input("Informe o total de refulgo: "))

print("Turno 2")
print("Linha 1")
codproduto21 = int(input("Código numérico do produto: #"))
quantidade21 = int(input("Informe a quantidade produzida: "))
refulgo21 = int(input("Informe o total de refulgo: "))

print("Linha 2")
codproduto22 = int(input("Código numérico do produto: #"))
quantidade22 = int(input("Informe a quantidade produzida: "))
refulgo22 = int(input("Informe o total de refulgo: "))

print("Linha 3")
codproduto23 = int(input("Código numérico do produto: #"))
quantidade23 = int(input("Informe a quantidade produzida: "))
refulgo23 = int(input("Informe o total de refulgo: "))

maior = 0
num1 = quantidade11 + quantidade21
num2 = quantidade12 + quantidade22
num3 = quantidade13 + quantidade23

maior = num1
linha = 1
if num2 > maior:
  maior = num2
  linha = 2
if num3 > maior:
  maior = num3
  linha = 3

totalrefulgoturno1 = refulgo11 + refulgo12 + refulgo13
totalrefulgoturno2 = refulgo21 + refulgo22 + refulgo23

print("RESPOSTA 1:")
print("A linha com maior número de produtos produzidos é a de número ", linha,".")


nivela = "Normal"
nivelb = "Normal"
nivelc = "Normal"
nivelaa = "Normal"
nivelbb = "Normal"
nivelcc = "Normal"

print("RESPOSTA 2:")
if refulgo11 >= 50:
    nivela = "Irregular"
print("Turno 1 | Linha 1 -- Situação ",nivela)
if refulgo12 > 100:
    nivelb = "Irregular"
print("Turno 1 | Linha 2 -- Situação ", nivelb)
if refulgo13 >= 50:
    nivelc = "Irregular"
print("Turno 1 | Linha 3 -- Situação ", nivelc)
if refulgo21 >= 50:
    nivelaa = "Irregular"
print("Turno 2 | Linha 1 -- Situação ",nivelaa)
if refulgo22 > 100:
    nivelbb = "Irregular"
print("Turno 2 | Linha 2 -- Situação ", nivelbb)
if refulgo23 >= 50:
    nivelcc = "Irregular"
print("Turno 2 | Linha 3 -- Situação ", nivelcc)

print("RESPOSTA 3:")
print("A quantidade total de refulgo no TURNO 1 é ", totalrefulgoturno1)
print("A quantidade total de refulgo no TURNO 2 é ", totalrefulgoturno2)