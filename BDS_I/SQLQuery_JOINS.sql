USE MinhaCaixa

-- Como haviamos aprendido
SELECT ClienteNome, ContaTipo, contas.ClienteCodigo, clientes.ClienteCodigo
FROM Clientes, CONTAS
WHERE Clientes.ClienteCodigo =Contas.ClienteCodigo

-- Agora com JOIN 
SELECT ClienteNome, ContaTipo,
contas.ClienteCodigo, clientes.ClienteCodigo
FROM Clientes 
    INNER JOIN Contas ON (Clientes.ClienteCodigo=Contas.ClienteCodigo)
    LEFT JOIN Movimentos ON (Contas.ContaNumero=Movimentos.ContaNumero)