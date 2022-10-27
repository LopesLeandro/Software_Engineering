SELECT * FROM Clientes

SELECT ClienteNome, ClienteRendaAnual, ClienteSexo,
CASE WHEN (ClienteRendaAnual >= 0 OR 
            ClienteRendaAnual <= 100000)
            AND ClienteSexo = 'M'
     THEN 'A'
ELSE 'Podre_Rico' END AS 'Classe_Cliente'

FROM Clientes
ORDER BY Classe_Cliente DESC