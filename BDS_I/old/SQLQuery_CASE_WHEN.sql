USE MinhaCaixa

SELECT ClienteNome, ClienteSexo,
    CASE WHEN ClienteSexo = 'M' THEN 'Masculino'
         WHEN ClienteSexo = 'F' THEN 'Feminino'
ELSE 'NN' END AS Sexo,
ClienteEstadoCivil,
CASE WHEN ClienteEstadoCivil = 'C' THEN 'Casado'
     WHEN ClienteEstadoCivil = 'S' THEN 'Solteiro'
ELSE 'NN' END AS EstadoCivil
FROM Clientes
