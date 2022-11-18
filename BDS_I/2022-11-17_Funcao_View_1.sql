CREATE VIEW vClientesIdade
AS 
SELECT ClienteNome,
    DATEDIFF(
        YEAR, ClienteNascimento,
        GETDATE()
        ) AS Idade
FROM dbo.Clientes;

