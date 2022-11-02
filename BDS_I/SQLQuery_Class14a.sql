-- SELECT COUNT(*) AS Quantidade, ClienteBairro FROM Clientes
-- GROUP BY ClienteBairro
-- ORDER BY 2 DESC

SELECT
ClienteBairro,
COUNT(ClienteCodigo) AS Quantidade,
SUM(ClienteRendaAnual) AS ClienteRendaAnual
FROM Clientes
GROUP BY ClienteBairro
ORDER BY 2 DESC