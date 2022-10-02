# bind = ligar, vincular
# c = colunms
# r = rows

#Adicionando colunas
x <- matrix(10:1,col=2)
x

y <- cbind(x,1:5) #adiciona uma 3a coluna a matriz x
y

#Adicionando linhas

y <- rbind(y,c(99,99,99))
y

#Juntar matrizes
z <- cbind(y,rep(88,6),y) #adiciona duas colunas a matriz y
z

# Extrair informação das matrizes
# Extrair informação da 2a linha e 5a coluna
k <- c(1,2,3,5,7,9,11,13,15,17,19,21,25,29,33,39,45,51,57,63) 
k
k[2,5]


# Extrair linha ou coluna inteira
k[3,] #Extrair linha inteira
k[,4] #Extrair coluna inteira

# Extrair mais de uma linha e coluna com vetor de índices

k[c(1,3,5),]
