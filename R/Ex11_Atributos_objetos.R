#Character     -> Textos ou caracteres
#Numeric       -> Números inteiros ou reais
#Logical       -> Verdadeiro ou falso (TRUE/FALSE)
#Complex       -> Número complexo
#List          -> Combina diferentes tipos de um mesmo objeto
#Function      -> Comandos

#Exemplo
x <- c(1,2,3,4,5,11)
mode(x); length(x); class(x); typeof(x); is.numeric(x); is.character(x); is.logical(x); is.complex(x); is.list(x); is.function(x)

a <- 'Angela'; b <- TRUE; c <- -8i
mode(a); mode(b); mode(c) #Exibe os atributos 'tipo' dos objetos
