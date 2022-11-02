USE MinhaCaixa;
-- count, count distinct, avg, max, min, sum
-- SELECT ClienteBairro,MovimentoValor FROM

-- SELECT ClienteBairro, SUM(MovimentoValor) AS Total
-- SELECT TOP 10 ClienteBairro, AVG(MovimentoValor) AS Total
SELECT TOP 10 ClienteBairro, SUM(MovimentoValor) AS Total,
COUNT(Clientes.ClienteCodigo) AS Quantidade
FROM
    Movimentos

        INNER JOIN Contas ON (Movimentos.ContaNumero=Contas.ContaNumero)

        INNER JOIN Clientes ON (Contas.ClienteCodigo=Clientes.ClienteCodigo)
-- WHERE COUNT(Clientes.ClienteCodigo) > 200
GROUP BY ClienteBairro
HAVING COUNT(Clientes.ClienteCodigo) > 200
-- ORDER BY ClienteBairro
-- ORDER BY sum(MovimentoValor) DESC
ORDER BY 2 DESC