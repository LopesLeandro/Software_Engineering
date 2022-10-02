x= c(2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,6)
hist(x)
table(x)

hist(x,     right = T,include.lowest = F,breaks = 1:6)

dados <-c(25,27,18,16,21,22,21,20,18,23,27,21,19,20,21,16)
hist(dados, 
     nc=6,
     right=F,
     main="Histograma",
     xlab="tempo em minutos",
     ylab="frequencia",
     col="blueviolet",
     density=25)

colors()
