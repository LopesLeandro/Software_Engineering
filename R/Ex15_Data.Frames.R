# São semelhantes às matrizes, pois possuem linhas e colunas
# Porém, colunas diferentes podem armazenar elementos de tipos diferentes
# Por exemplo a primeira coluna pode ser numérica, quanto a segunda, constituída de caracteres.

# A distinção mais importante é que em um data.frame (ao contrário de uma lista), todos os membros devem ser vetores de igual comprimento (The Book of R)
# O data frame é uma das ferramentas mais importantes e frequentemente usadas em R para análise de dados estatísticos
# Cada linha representa uma unidade (instância ou observação)
# Cada coluna representa uma variável observada em cada unidade

# Exemplo:

nome <- c("João","Maria","José","Ana","Pedro","Paulo","Júlia","Carlos","Marcos","Mariana")
nome

idade <- c(20,25,30,35,40,45,50,55,60,65)
idade

sexo <- factor(c("M","F","M","F","M","M","F","M","M","F"))
sexo

NF <- c(1,2,3,4,5,6,7,8,9,10)
NF

# Agora que cada vetor foi criado, reunimos tudo em um objeto com estrutura de dados de um data.frame:

escola <- data.frame(nome,idade,sexo,NF)
escola

# Índices nos data.frames

escola [2,1] # 2a linha, 1a coluna
escola [2,] # 2a linha, todas as colunas

# O “Nome” foi originalmente criado como um vetor de caracteres, porém o R passou a entendê-lo como um fator dentro do data.frame.
# Isso acontece porque o argumento stringsAsFactors, por padrão definido como TRUE, converte vetores de caracteres em fatores na construção do data.frame.
# Pode se converter a estrutura de dados de cada uma das colunas de um data.frame usando as, seguido de um ponto e o nome da nova estrutura desejada:

escola[,1]

escola[,1] <- as.character(escola[,1]) #converte a coluna 1 em um vetor de caracteres
escola[,1]

# A outra maneira de acessar elementos de um data.frame é usar o nome do objeto, o símbolo $ e o nome da coluna de interesse
# Acessando a coluna “Nome”

escola$nome

escola$nome[2] #Acessando o segundo elemento da coluna “Nome”

escola$nome[1:3] #Acessando do primeiro ao terceiro elemento da coluna “Nome”

# Manipulando um data.frame
# Adicionar ou remover colunas com cbind() e rbind()

# Adicionando uma coluna
escola <- cbind(escola, Conceito=c("A","B","C","D","E","F","G","H","I","J"))
escola

# Adicionando uma linha
escola <-rbind(escola, 'linha 11'=c("Caio",12,factor("M"),"99","A+"))
escola

# Pode se utilizar índices com o sinal negativo para eliminar linhas ou colunas de um data.frame:
escola < escola[,5] #elimina a coluna 5

# Pode-se também selecionar um subgrupo de um data.frame e armazená-lo em um outro objeto:
v <- escola[1:6,]
v

# Pode se exibir apenas uma classe:
escola[escola$sexo=="M",] #exibe apenas os alunos do sexo masculino

# Ordenar linhas de um data.frame segundo os dados contidos em determinada coluna também é extremamente útil:
escola[order(escola$NF),] #ordena as linhas de acordo com a NF

# Ordenar por ordem inversa (decrescente):
escola[rev(order(escola$NF)),] #ordena as linhas de acordo com a NF

# É possível ordenar por mais de uma coluna:
escola[order(escola$NF,escola$idade),] #ordena as linhas de acordo com a NF e a idade

# Grupos
# O R permite agrupar linhas de um data.frame segundo os valores de uma ou mais colunas
# Podemos separar o data frame em grupos, como por exemplo por Sexo:
split(escola,sexo)

# Agrupando Data.frames
# merge()
# Permite que dois data.frames sejam unidos por uma coluna ou linha que tenham em comum:

novo <- data.frame(nome=escola$nome,numero=1:6)
novo

merge(escola,novo,by="nome")
