USE MinhaCaixa;

SET DATEFORMAT YMD
SET LANGUAGE ENGLISH
-- SELECT YEAR(GETDATE())

-- SELECT * FROM Movimentos
-- WHERE Movimentos.MovimentoData = '2006-06-30'

-- SELECT DATENAME(MONTH,(MovimentoData)) 
-- FROM Movimentos

SELECT ClienteNome, 
YEAR(ClienteNascimento) AS BIRTH_YEAR,
DATENAME(MONTH,(ClienteNascimento)) AS BIRTH_MONTH,
DAY(ClienteNascimento) AS BIRTH_DAY,
DATEPART(yyyy,ClienteNascimento) AS ANO2,
DATEPART(yy,ClienteNascimento) AS ANO3
From Clientes
WHERE YEAR(ClienteNascimento) >= 1980 AND
YEAR(ClienteNascimento) <= 1985 AND

ClienteNome = 'Jon' OR ClienteNome = 'Marie'
ORDER BY ANO3

SELECT EOMONTH(GETDATE()) AS 'MONTH ENDLESS'
SELECT DATEADD(day,1,GETDATE())
SELECT DATEADD(MONTH,-1,GETDATE())

-- DISCOVERY BIRTH NEXT QUERY