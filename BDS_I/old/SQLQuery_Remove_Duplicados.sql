--SELECT DISTINCT ClienteBairro FROM Clientes
--SELECT ClienteBairro,
--SELECT COUNT(DISTINCT ClienteBairro) FROM Clientes
--ORDER BY ClienteBairro  
SELECT COUNT(ClienteBairro) FROM Clientes
GROUP BY ClienteBairro