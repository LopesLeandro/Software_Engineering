SELECT Clientes.ClienteNome, CartaoCredito.CartaoCodigo,
CASE WHEN CartaoCodigo IS NULL THEN
ClienteTelefone ELSE 'Não ligar' END AS 'Condição'
FROM Clientes
--INNER JOIN CartaoCredito Traz os que tem cartao de credito (4)
LEFT JOIN CartaoCredito --Traz os que não tem e os que tem 
    ON (Clientes.ClienteCodigo=CartaoCredito.ClienteCodigo)
    AND ClienteSexo = 'm'
RIGHT JOIN Contas
    ON (Clientes.ClienteCodigo=Contas.ClienteCodigo)