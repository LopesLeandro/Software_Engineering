# x<-matrix(data=dados,nrow=m,ncol=n,byrow=Q) 
# m= número de linhas
# n= número de colunas
# Se Q = 1, ativa disposição por linhas (T)
# Se Q = 0, mantém disposição por colunas (F)

A <- matrix(c(1:10),2,5,1)
A

A <- matrix(c(1:10),2,5,T)
A

x < - (1:12)
B <- matrix(x, ncol=3)
B

summary(B) #ambém pode ser usado para obter informações de qualquer objeto, inclusive de matrizes.

#Caso deseje um resumo de todos os elementos da matriz, transforme em vetor antes de usar o summary():

summary(as.vector(B))
summary(x)

