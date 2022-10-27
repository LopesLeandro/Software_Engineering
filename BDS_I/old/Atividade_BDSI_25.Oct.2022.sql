USE BDS;

-- 1.	Crie uma tabela para armazenar o nome do feriado e data dele. Em seguida pesquise quais são os feriados nacionais (brasileiros) e insira nessa tabela. A tabela devera ter código do feriado (auto-incremento), nome do feriado e a data em que ele é comemorado.

CREATE TABLE Feriados(
    CodigoFeriado INT IDENTITY(1,1) PRIMARY KEY,
    NomeFeriado VARCHAR(50) NOT NULL,
    DataFeriado DATE NOT NULL
);

INSERT INTO Feriados(NomeFeriado, DataFeriado)
VALUES('Confraternização Universal', '01/01/2022'),
('Tiradentes', '21/04/2022'),
('Dia do Trabalho', '01/05/2022'),
('Corpus Christi', '03/06/2022'),
('Independência do Brasil', '07/09/2022'),
('Nossa Senhora Aparecida', '12/10/2022'),
('Finados', '02/11/2022'),
('Proclamação da República', '15/11/2022'),
('Natal', '25/12/2022');


