#1) Um artigo do periódico Materials Engineering descreve os resultados de teste de tensão quanto à adesão em 22 corpos de prova de liga U-700. 
#A carga no ponto de falha do corpo de prova é dada pelo arquivo “carga no ponto de falha.txt”. 
#Verifique se os dados sugerem que a carga média na falha excede 10 MPa. 
#Considere o nível de significância de 5%. Interprete o resultado.

# Importar arquivo
tst_tensao = read.table("/Users/leandrolopes/Library/Mobile Documents/com~apple~CloudDocs/Eng. Software/Software_Engineering/R/New Task 02/carga_ponto_falha.txt", head = TRUE)
#tst_tensao <- scan() #Importar como informação numérica
tst_tensao #plota a variavel

#Ho = A carga média é igual 10 Mpa
#Ha = A carga média excede os 10Mpa

t.test(tst_tensao, 
       mu = 10, 
       alternative = "greater", 
       conf.level = 0.95)

#data:  tst_tensao
#t = 4.9017, df = 21, p-value = 3.781e-05
#alternative hypothesis: true mean is greater than 10
#95 percent confidence interval:
# 12.40996      Inf
#sample estimates:
#mean of x 
# 13.71364 

#Dado que p-value é menor que alfa (sig), então rejeito a hipotese nula. 
#E além disto, temos que o intervalo de confiança máximo é 12.40996 e a média fechou em 13.71, reforçando que ficou fora do invetervalo de aceitação estatística.


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#2) Dois catalisadores estão sendo analisados para determinar como eles afetam o rendimento médio de um processo químico. 
#Especificamente, o catalisador 1 está corretamente em uso, mas o catalisador 2 é aceitável. 
#Uma vez que o catalisador 2 é mais barato, ele deve ser adotado, desde que ele não mude o rendimento do processo. 
#Um teste é feito em uma planta piloto, resultando nos dados do arquivo “catalisadores”. 
#Há alguma diferença entre os rendimentos médios? Use α = 0,05 e considere variâncias iguais. Formule antes as hipóteses.

#ho = O rendimento médio é igual.
#ha = O rendimento médio é diferente, ou seja, sofre alteração.

catalisador = read.table("/Users/leandrolopes/Library/Mobile Documents/com~apple~CloudDocs/Eng. Software/Software_Engineering/R/New Task 02/catalisador.txt", head = TRUE)
catalisador

t.test(catalisador[,1],
       catalisador[,2],
       conf.level = 0.95)

#data:  catalisador[, 1] and catalisador[, 2]
#t = -0.35359, df = 13.353, p-value = 0.7292
#alternative hypothesis: true difference in means is not equal to 0
#95 percent confidence interval:
#  -3.387118  2.432118
#sample estimates:
#  mean of x mean of y 
#92.2550   92.7325 

# O catalisador 2 não altera o rendimento do processo, porque o p-value apresentado é maior que alfa, descartando a hipotese nula. 
#Além disso, o intervalo de confiança passa entre o ZERO, demonstrando que possui igualdade.

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#3) Uma companhia fabrica propulsores para uso em motores de turbinas de avião. 
#Uma das operações envolve esmerilhar o acabamento de uma superfície particular para um componente de liga de titânio. 
#Dois processos diferentes para esmerilhar podem ser usados, podendo produzir peças com iguais rugosidades médias na superfície. 
#Uma amostra aleatória de n1 = 11 peças, proveniente do primeiro processo, resulta em um desvio-padrão de s1 = 5,1 micropolegadas. 
#Uma amostra aleatória de n2 = 16 peças, proveniente do segundo processo, resulta em um desvio-padrão de s2 = 4,7 micropolegadas. 
#Verifique se a razão entre as duas variâncias é diferente de 1 com um nível de confiança de 90%. 
#Considere que os dois processos sejam diferentes e a rugosidade na superfície seja normalmente distribuída.
#Use o comando rnorm( ) para criar o conjunjunto de dados.

#n1 = 11 peças
#desv_pad_s1 = 5.1 micropolegadas.
#n2 = 16 peças
#desv_pad_s2 = 4.7
# var =! 1
#alfa = 0.1
#Ho = A razão entre as duas variâncias é igual a 1
#Ha = A razão entre as duas variâncias é diferente de 1

#Criando o conjunto de dados
n1 = 11
n2 = 16
desv_pad_s1 = 5.1
desv_pad_s2 = 4.7

amostra1 = rnorm(n1, mean = 0, sd = desv_pad_s1)
amostra2 = rnorm(n2, mean = 0, sd = desv_pad_s2)

var.test(amostra1, amostra2, conf.level = 0.9)

qqnorm(amostra1)
qqnorm(amostra2)

#data:  amostra1 and amostra2
#F = 0.95486, num df = 10, denom df = 15, p-value = 0.9686
#alternative hypothesis: true ratio of variances is not equal to 1
#90 percent confidence interval:
# 0.3753788 2.7165871
#sample estimates:
#ratio of variances 
#         0.9548581 

#A razão entre as duas variâncias é diferente de 1, porque o p-value apresentado é maior que alfa, descartando a hipotese nula.
#Além disso o conjunto de dados no gráfico não é paralelo a linha de normalização, demonstrando que a distribuição não é aproximadamente normal.

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#Verifique se os dados do arquivo “carga no ponto de falha” segue distribuição normal.

#ho = Os dados seguem distribuição normal.
#ha = Os dados não seguem distribuição normal.

carga_falha = read.table("/Users/leandrolopes/Library/Mobile Documents/com~apple~CloudDocs/Eng. Software/Software_Engineering/R/New Task 02/carga_ponto_falha.txt", head = TRUE)

shapiro.test(carga_falha)

qqnorma(carga_falha)
qqline(carga_falha)

# Resultados
#	Shapiro-Wilk normality test

#data:  carga_falha
#W = 0.96981, p-value = 0.7067

#Os dados seguem distribuição normal, porque o p-value apresentado é maior que alfa, mantendo a hipotese nula.

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# 5) Verifique se os dados do arquivo “catalisadores” seguem distribuição normal.

# h0 = Os dados seguem distribuição normal.
# ha = Os dados não seguem distribuição normal.

catalisador = read.table("/Users/leandrolopes/Library/Mobile Documents/com~apple~CloudDocs/Eng. Software/Software_Engineering/R/New Task 02/catalisador.txt", head = TRUE)
catalisador

amostra1 = catalisador[,1]
amostra2 = catalisador[,2]

amostra1
amostra2

shapiro.test(amostra1)

shapiro.test(amostra2)

qqnorm(amostra1)
qqline(amostra1)
qqnorm(amostra2)
qqline(amostra2)

# Resultados
#shapiro.test(amostra1)

#	Shapiro-Wilk normality test

#data:  amostra1
#W = 0.92171, p-value = 0.4439

#> shapiro.test(amostra2)

#	Shapiro-Wilk normality test

#data:  amostra2
#W = 0.88182, p-value = 0.196

# qqnorm(amostra1)
# qqline(amostra1)


# qqnorm(amostra2)
# qqline(amostra2)

# A amostra 1 e 2 seguem distribuição normal, porque o p-value apresentado é maior que alfa, mantendo a hipotese nula.
