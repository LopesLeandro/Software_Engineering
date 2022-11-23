--Utilizando o banco de dados Minha Caixa, faça uma consulta que mostre o nome do cliente, o nome da agência, o bairro da agência e o número do cartão de crédito, 
-- somente para os clientes em que a conta foi aberta a partir de 2010. Caso ele não tenha cartão de crédito, mostre o telefone do cliente para contato.


SELECT Clientes.ClienteNome, Agencias.AgenciaNome, Agencias.AgenciaBairro, Cartoes.CreditoNumero FROM Clientes
INNER JOIN Contas ON Clientes.ClienteID = Contas.ClienteID
INNER JOIN Agencias ON Contas.AgenciaID = Agencias.AgenciaID
LEFT JOIN Cartoes ON Clientes.ClienteID = Cartoes.ClienteID
WHERE Contas.ContaDataAbertura >= '2010-01-01'
AND Cartoes.CreditoNumero IS NOT NULL
UNION
SELECT Clientes.ClienteNome, Agencias.AgenciaNome, Agencias.AgenciaBairro, Clientes.ClienteTelefone FROM Clientes
INNER JOIN Contas ON Clientes.ClienteID = Contas.ClienteID
INNER JOIN Agencias ON Contas.AgenciaID = Agencias.AgenciaID
LEFT JOIN Cartoes ON Clientes.ClienteID = Cartoes.ClienteID
WHERE Contas.ContaDataAbertura >= '2010-01-01'
AND Cartoes.CreditoNumero IS NULL
