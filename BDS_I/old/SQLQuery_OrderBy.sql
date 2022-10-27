USE MinhaCaixa

--SELECT TOP 5 * FROM Clientes : puxa os 5 primeiros

-- SELECT * FROM Clientes
-- ORDER BY ClienteNome 

SELECT TOP 5 ClienteNome, ClienteRendaAnual, ClienteSexo
FROM Clientes
WHERE ClienteSexo = 'F'
ORDER BY ClienteRendaAnual --DEFAULT é ascendente

--JUNTAR TABELAS

SELECT ClienteNome AS Nome, ClienteRendaAnual, Contas.ContaNumero, ContaAbertura, Movimentos.MovimentoTipo
FROM Clientes AS Cli, Contas, Movimentos
WHERE Cli.ClienteCodigo = Contas.ClienteCodigo
AND Movimentos.ContaNumero = Contas.ContaNumero
AND Cli.ClienteCodigo = 1
SELECT * FROM Contas WHERE ClienteCodigo = 1

SELECT * FROM Clientes
WHERE ClienteNome LIKE 'J%'
AND ClienteNome LIKE '%E'
AND ClienteNome LIKE '%SS%'

SELECT ClienteNome, ClienteSexo,
CASE 
    WHEN ClienteSexo = 'M' THEN 'Masculino'
    WHEN ClienteSexo = 'F' THEN 'Feminino'
    ELSE 'Não Informado'
END AS Sexo
FROM Clientes