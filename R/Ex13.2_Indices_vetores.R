#Os elementos armazenados em um vetor podem ser acessados através dos chamados índices, com o uso de colchetes [ ]. # nolint

x <- 5:1 #sequência de 5 a 1
x

x[2:4] #elementos de índice 2 ao 4

x[c(2,4)] #elementos de índice 2 e 4

x[3]

#Usando expressões logicas para acessar os valores
x <- (5:1)
x[x < 4] #elementos menores que 4
x[-2] #elementos diferentes de 2

