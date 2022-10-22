# SOMATÓRIO
x <- c(10,20,30,40)
sum(x)

Y <- c(65,75,85,65,95,80)
sum(Y^2)-Y[1]^2-Y[5]^2

#OU

sum(Y[-c(1,5)]^2)

# PRODUTÓRIO

z<-c(15,25,35,45)
prod(z)

prod(z[-c(3,4)])

# MEDIDAS DE POSIÇÃO AMOSTRAL

k <- c(3,7,8,NA,11)
mean(k)

# Remover o NA

mean(k,na.rm = T)

# MEDIANA

p <- c(3,3,3,7,5,5,5,5,5,5,5,5,9,9,10,99,77,10,1)
sum(p)
median(p)

# MODA
table(p)

mfv(p)

subset(table(p),table(p)==max(table(p)))

# MEDIDAS DE DISPERSÃO AMOSTRAL

# Variancia S2
nascimentos <- c(1,1,2,2,2,3,4,5,5,6,6,66,7,7,8,8,8,8,8,9,9,9,10,10,11,12,13,14)
var(nascimentos)
signif(var(nascimentos),3)

# Desvio padrão

sd(nascimentos)

signif(sd(nascimentos),3)

sqrt(var(nascimentos))
signif(sqrt(var(nascimentos)),3)

# AMPLITUDE TOTAL
range(nascimentos)

# COEFICIENTE DE VARIAÇÃO

cv <- (sd(nascimentos)/mean(nascimentos))*100
cv
