#1) Um artigo do periódico Materials Engineering descreve os resultados de teste de tensão quanto à adesão em 22 corpos de prova de liga U-700. 
#A carga no ponto de falha do corpo de prova é dada pelo arquivo “carga no ponto de falha.txt”. 
#Verifique se os dados sugerem que a carga média na falha excede 10 MPa. 
#Considere o nível de significância de 5%. Interprete o resultado.

# Importar arquivo
tst_tensao = read.table("/Users/leandrolopes/Library/Mobile Documents/com~apple~CloudDocs/Eng. Software/Software_Engineering/R/New Task 02/carga_ponto_falha.txt", head = TRUE)
#tst_tensao <- scan() #Importar como informação numérica
tst_tensao #plota a variavel

#Ho = A carga média excede 10 Mpa
#Ha = A carga média não excede os 10Mpa

t.test(tst_tensao, 
       mu = 10, 
       alternative = "two.sided", 
       conf.level = 0.95) 
#Teste de hipótese

#data: tst_tensao
#t = 4.9017 df = 21 p-value = 7.563e-05
#95% confident interval = 12.13807 & 15.28920
#mean 13.71364

#Dado que p-value é maior que alfa (sig), então eu não rejeito a hipotese nula.
#Meu intervalo de confiança ficou entre 12 e 15 e minha média em 13,7, excede os 10 Mpa

#Grafico significancia
plot(signif(tst_tensao, 2), 
     main = "Significância", 
     xlab = "Carga no ponto de falha", 
     ylab = "Significância", 
     col = "blue", 
     pch = 22, 
     bg = "purple", 
     tcl = 0.4, 
     las = 1, 
     cex = 1.5, 
     bty = "5")
    