SELECT ClienteNascimento,
DATENAME(MONTH, ClienteNascimento) AS Mes,
YEAR(ClienteNascimento) AS Ano,
DATENAME(MONTH,ClienteNascimento) + ' / ' +
CAST(YEAR(ClienteNascimento) AS CHAR(4))
From Clientes