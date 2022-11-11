USE MinhaCaixa

SELECT ClienteNome + ' ' + ClienteSobrenome
+ ' /' + CAST(ClienteRendaAnual AS CHAR(10))
AS NomeCompleto
FROM Clientes

SELECT ClienteNome + ' ' + ClienteSobrenome
+ ' /' + CONVERT(CHAR(10),ClienteRendaAnual)
AS NomeCompleto
FROM Clientes


