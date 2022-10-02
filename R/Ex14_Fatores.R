# Fatores proporcionam uma forma fácil e compacta de lidar com dados categóricos (ou nominais)
# Exemplos sexo, raça, tipo sanguíneo, fator Rh

s <- c('f','m','m','m','f','f','m','m','m','f')
s

# Ao transformarmos o vetor de caracteres em um fator, o R nos dá a possibilidade, por exemplo, de contar quantas vezes ocorre cada valor desse fator:
s <- factor(s)

# Levels: f m
# s deixou de ser um vetor de caracteres, transformando-se num fator de dois níveis: f e m.

