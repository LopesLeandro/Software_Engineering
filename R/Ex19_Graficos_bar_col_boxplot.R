#Barplot das cores
barplot(table(c('a','a','a','b','e','e','e','h','h','h','h','h','h','n','n','n','n','r','s','t','u','v','w','x','y','z')),
        main = 'Gráfico de cores',
        xlab = 'Cores',
        ylab = 'Frequência',
        bty = 'l',
        col = 'purple',
        horiz = TRUE
)

#Nomeando colunas
prof <- c(1751,1186,947,29)
escola <- c('privada','publica','estadual','federal')
barplot(prof, names.arg = escola,
        main = 'Quantidade de professores',
        xlab = 'Instituição',
        ylim = c(0,2000),
        col = 'purple',
        # É possível também nomear as posições através do comando names( ) e aumentar a fonte do título e eixos
        cex.axis = 2,
        cex.names = 2,
        density = 50,
        #horiz = TRUE,
        #names.arg = escola
)



