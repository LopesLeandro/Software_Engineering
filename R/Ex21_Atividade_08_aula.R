# 1) O arquivo “Defeitos no computador” mostra a distribuição da quantidade de defeitos por computador para uma amostra de 100 aparelhos. Calcule:
# a) a média de defeitos por computador
# b) a moda
# c) amediana
# d) a variância
# e) o desvio padrão

# Importar arquivo
defeitos = read.table("/Users/leandrolopes/Library/Mobile Documents/com~apple~CloudDocs/Eng. Software/Software_Engineering/R/Data/defeitos.txt", head = TRUE)
defeitos <- scan() #Importar como informação numérica
defeitos #plota a variavel
lenght <- c(1,2,3,4,5,6)
# Resposta letra a)
media <- mean(defeitos) #média de defeitos
media
# Resposta letra b)
moda <- table(defeitos) #moda de defeitos
moda
# Resposta letra c)
median(defeitos) #mediana de defeitos

# Resposta letra d)
var(defeitos) #variância de defeitos

# Resposta letra e)
sd(defeitos) #desvio padrão de defeitos

plot(density(defeitos), 
        main = "Distribuição de defeitos", 
        xlab = "Defeitos", 
        ylab = "Densidade", 
        col = "purple", 
        lwd = 3)


barplot(moda, lenght,
        main = 'Distribuição da moda', 
        ylab = 'y',
        xlab = 'x',
        col = c('purple'), 
        density = 50,
        ylim = c(0, 50))

