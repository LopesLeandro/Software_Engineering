SELECT ClienteNome, ClienteSobrenome, ClienteRendaAnual FROM Clientes WHERE ClienteNome = 'Jon'
UNION
SELECT ClienteSobrenome, ClienteNome, NULL AS ClienteRendaAnual FROM Clientes WHERE ClienteNome = 'Jon'