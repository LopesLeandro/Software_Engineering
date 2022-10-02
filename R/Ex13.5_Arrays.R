# São similares aos vetores e matrizes, mas podem ter qualquer número de dimensões.
# Para o R, um array é um simples vetor com o atributo de dimensões (dim)

# Criando arrays
# Atribuir dimensões a um vetor com comando dim()
x <- 1:12
dim(x) <- c(2,3,2) #3 dimensões em x (2 linhas, 3 colunas, 2 matrizes)

# O mesmo pode ser feito com arrays

y <- array(1:12,c(2,3,2))
y

# Atribuir nomes ãs dimensões do array
dimnames(x) <- list(lat=c("N","S"),long=c("W","E","C"),time=c("past","future"))
x


