x <- 1:20
y <- x^2
plot(x,y)

plot(x,y,type='b',pch=6)

x <- seq(0,10,0.1)
x1 <- 0.4*exp(-0.4*x)
x2 <- 0.3*exp(-0.3*x)
y <- cbind(x1,x2)
matplot(y, type='1')
legend(80,0.3,c('x1','x2'),lty = c(1,2), col=c(1,2))

x <- 1:10
y <- c(2,5,9,6,7,8,4,1,3,10)
x;y
plot(x,y)

# Outro exemplo

plot(x,y, #plota x e y
     xlab = 'Eixo X', #nomeia o eixo x
     ylab = 'Eixo Y', #nomeia o eixo y
     main = 'Personalizando gráficos', #título
     xlim = c(0,10), #limites do eixo x
     ylim = c(0,10), #limites do eixo y
     col = 'gray', #cor dos pontos
     pch = 22, #formato dos pontos
     bg = 'purple', #cor do preenchimento dos pontos
     tcl = 0.4, #tamanho dos traços do eixo
     las = 1, #orientação dos valores no eixo
     cex = 1.5, #tamanho do ponto
#     bty = '5' #altera as bordas
)

# Histograma

x <- c(2,2,2,2,2,3,3,3,4,4,5,5,6)
y <- c(3,4,5,6,7,8,9,1,2,3,4,5,6)
hist(x)

table(x) #valores de x e suas frequências

# Personalizando o histograma

hist(x, 
     right = T, #intervalos fechados a direita
     include.lowest = F, #não soma extremos do vetor
     breaks = 1.6 #intervalo de classes
     )

colors()