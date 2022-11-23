--USE MinhaCaixa;
--SELECT ClienteNome, ClienteNascimento FROM Clientes
--WHERE month(ClienteNascimento)
--=month(GETDATE())

--Unitilizando o banco de dados MinhaCaixa, escreva uma consulta que mostre o nome e sobrenome do cliente (concatenados), e se o cliente for homem, mostre Sr. e se for mulher Sra. na frente do nome/sobrenome.

--Exemplo:

--Cliente
--Sr. Ruben Torres
--Sra. Christy Zhu

-- Path: BDS_I/2022-11-17_Funcao_View_2_1.sql
-- Compare this snippet from BDS_I/questions_sql.sql:

--USE MinhaCaixa;
--SELECT ClienteNome, ClienteSobrenome, ClienteSexo FROM Clientes
--WHERE ClienteSexo = 'M'
--UNION
--SELECT ClienteNome, ClienteSobrenome, ClienteSexo FROM Clientes
--WHERE ClienteSexo = 'F'


SELECT 
CASE WHEN ClienteSexo = 'M'
THEN 
    'Sr. ' + ClienteNome + ' ' + ClienteSobrenome
ELSE 
    'Sra. ' + ClienteNome + ' ' + ClienteSobrenome
END AS NomeCompleto FROM Clientes


SELECT ClienteBairro,
COUNT(ClienteBairro) 
    AS Quantidade FROM Clientes 
GROUP BY ClienteBairro


SELECT TOP 10 YEAR(GETDATE()) - YEAR(ClienteNascimento) AS idade,
Clientes.ClienteRendaAnual as Renda FROM Clientes


SELECT top 5 Clientes.ClienteBairro   ,
SUM(Clientes.ClienteRendaAnual) as Renda FROM Clientes   GROUP BY Clientes.ClienteBairro ORDER BY 1



SELECT TOP 10 YEAR(GETDATE()) - YEAR(ClienteNascimento) AS idade, 
Clientes.ClienteRendaAnual as Renda
FROM Clientes 
ORDER BY idade, Renda DESC




SELECT top 5 Clientes.ClienteBairro,
--Clientes.ClienteRendaAnual as Renda FROM Clientes
SUM(Clientes.ClienteRendaAnual) as Renda FROM Clientes
--GROUP BY Clientes.ClienteRendaAnual 
ORDER BY 2
--GROUP BY Clientes.ClienteBairro 
--ORDER BY 2

SELECT ClienteBairro, ClienteNome FROM Clientes
WHERE ClienteBairro in 
('CENTRO', 'FLORESTA', 'ATIRADORES'),
CAST(Clientes.ClienteBairro AS CHAR(20)) -- AS Bairro
COUNT(ClienteNome)





SELECT ClienteNome,ClienteSobrenome, (ClienteRendaAnual * 5.36) AS Dolar, (ClienteRendaAnual * 5.51) AS Euro FROM Clientes;

SELECT ClienteNome,ClienteSobrenome, (ClienteRendaAnual / 5.36) AS Dolar, (ClienteRendaAnual / 5.51) AS Euro FROM Clientes;

SELECT ClienteNome,ClienteSobrenome, (ClienteRendaAnual / 5.36) - 100 AS Dolar, (ClienteRendaAnual / 5.51) - 100 AS Euro FROM Clientes;


SELECT ClienteNome, AgenciaNome,  
    CASE WHEN ClienteSexo = 'M' THEN 'Masculino'
         WHEN ClienteSexo = 'F' THEN 'Feminino'
ELSE 'NN' END AS Sexo,
ClienteEstadoCivil,
CASE WHEN ClienteEstadoCivil = 'C' THEN 'Casado'
     WHEN ClienteEstadoCivil = 'S' THEN 'Solteiro'
ELSE 'NN' END AS EstadoCivil
FROM Clientes
