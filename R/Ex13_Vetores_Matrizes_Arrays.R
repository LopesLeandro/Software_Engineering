#Objeto             Tipos                                                               Suporta tipos diferentes # nolint
#Vetor              Numérico, caractere, complexo ou #Lógicos                           Não # nolint
#Fator              Numérico ou caracteres                                              Não # nolint
#Matriz             Numérico, caractere, complexo ou lógico                             Não # nolint
#Array              Numérico, caractere, complexo ou lógico                             Sim # nolint
#Data.frame         Numérico, caractere, complexo ou lógico                             Sim # nolint
#ts                 Numérico, caractere, complexo ou lógico                             Sim # nolint
#lista              Numérico, caractere, complexo, lógico, função, expressão, etc.      Sim # nolint

x <- c(2, 3, 5, 7, 11) #os cinco primeiros números primos
x #exibe o conteúdo do objeto x

y <- c(x, 13, 17, 19) #adicionando três números primos
y #exibindo y

#Sequências
seq(início, fim, incremento) #nolint
seq(1, 10, 1)

seq(1, 10, 2) #não termina em 10
seq(10, 1, -3) #usando incremento negativo

a <- 1:10 #cria sequência de inteiros de 1 a 10
a

b <- 10:1 #cria sequência de inteiros de 10 a 1
b

longo <- 100:50 #sequência decrescente de 100 a 50
longo

#Repetições
rep(1,10) #repete o número 1 dez vezes

rep(c(1,2),5) #repete os números 1 e 2 cinco vezes

c(rep(0,10),rep(1,10)) #repete 0 dez vezes e 1 dez vezes

x <- 10
rep(c(1,2),x) #repete os números 1 e 2 x vezes