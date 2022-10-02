Nome <- c ('José Santos','Angela Dias','Aline Souza','Mayara Costa','Lara Lins','Nicolas Barros')
Nome

Idade <- c(17,17,16,15,15,13)
Idade

Sexo <- factor(c('f','f','m','m','m','f'))
Sexo

NF<-c(92,75,34,99,87,999)
NF

escola <- data.frame(Nome,Idade,Sexo,NF)
escola

escola[2,1] #Elemento da linha 2, coluna 1

escola[2,] #Elemento da linha 2, coluna qualquer

escola[,1] #Verificamos que realmente a coluna é um fator

escola[,1] <-as.character(escola[,1]) #Converte a coluna para caracter

escola[,1]

escola$Nome
escola$Nome[2]
escola$Nome[1:3]

escola<-cbind(escola, Conceito=c('A','B','C','D','E','F'))
escola

escola<-rbind(escola, 'linha 7'=c('Caio Shhhhhh',12,factor('f'),'99','A+'))
escola

escola<-rbind(escola, 'linha 8'=c('Pedro Excel',19,'m','9999','A++'))
escola

escola <- escola[,-5]
escola

v <- escola[1:6,]
v

escola[escola$Sexo=='m',] #exibindo só masc
escola[escola$Sexo=='f',] #exibindo só fem

escola[order(escola$NF),] #Ordena por NF

escola[rev(order(escola$NF)),] #Ordena por NF invertido

escola[order(escola$Nome),] #Ordena por Nome

escola[order(escola$Sexo,escola$NF),] #Ordena por Nome

split(escola,Idade)
