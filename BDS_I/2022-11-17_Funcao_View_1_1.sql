SELECT ClienteNome, ClienteNascimento FROM Clientes
WHERE month(ClienteNascimento)
=month(GETDATE())