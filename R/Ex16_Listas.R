# São objetos usados para combinar diferentes estruturas de dados em um mesmo objeto, ou seja, vetores, matrizes, arrays, data.frames e até outras listas

pes <- list(idade=32, nome='Aline', notas=c(8,9,10), sexo='F')
pes

#Acessando elementos de uma lista
pes$nome #acessando o elemento nome

pes$notas[2] #acessando o segundo elemento do vetor notas

# Alguns comandos que retornam listas
# Muitos comandos do R retornam seu resultado na forma de listas .
# Um exemplo pode ser mostrado com o uso do comando t.test( ) que retorna um objeto que é uma lista.

# Execute um teste t simples para dois conjuntos de números:
x <- c(1,2,3,4,5,6,7,8,9,10)
y <- c(1,2,3,4,5,6,7,8,9,10)
tt <- t.test(x,y,var.equal=T)
tt

# p-value = 0.01296

# Podemos comprovar que o objeto tt é uma lista
is.list(tt)
mode(tt)

# Podemos exibir os componentes da lista com o comando names( ):
names(tt)

# Podemos extrair elementos do objeto tt individualmente:
tt$p.value
tt$statistic
t

# Podemos também extrair todos os elementos da lista com o comando unlist( ):
unlist(tt)

# Podemos também extrair todos os elementos da lista com o comando as.list( ):
as.list(tt)

# Podemos também extrair todos os elementos da lista com o comando as.data.frame( ):
as.data.frame(tt)

# Podemos também extrair todos os elementos da lista com o comando as.matrix( ):
as.matrix(tt)

# Podemos também extrair todos os elementos da lista com o comando as.array( ):
as.array(tt)

# Podemos também extrair todos os elementos da lista com o comando as.vector( ):
as.vector(tt)

# Podemos também extrair todos os elementos da lista com o comando as.character( ):
as.character(tt)
