CREATE TABLE Empregados (
    ID int NOT NULL PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
);

INSERT into Empregados (ID, LastName, FirstName, Age)
values (1, 'Lopes', 'Leandro', 32);

SELECT * from Empregados;