CREATE DATABASE MinhaCaixa

USE MinhaCaixa 

SELECT * FROM Clientes AS Cli --As linhas onde o sexo é masculino e todas as colunas
WHERE ClienteSexo = 'M' 
    AND (ClienteBairro = 'CENTRO' OR ClienteBairro = 'BOM RETIRO')
    AND ClienteEstadoCivil = 'S'

SELECT ClienteNome FROM Clientes --Todas as linhas e só a coluna ClienteNome

SELECT ClienteNome, ClienteSobrenome FROM Clientes --Todas as linhas e as colunas 