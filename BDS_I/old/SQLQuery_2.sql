-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.

CREATE DATABASE SQL_Atividade_02

USE SQL_Atividade_02

CREATE TABLE CLIENTES
(
    CODCLIENTES INT CONSTRAINT PK_CLIENTES PRIMARY KEY,
    CLIENTENOME VARCHAR(50) NOT NULL,
    CLIENTEDATACADASTRO DATETIME NULL,
    CLIENTESALARIO MONEY
)
CREATE TABLE ENDERECOS
(
    ENDERECOSCOD INT CONSTRAINT PK_ENDERECOS PRIMARY KEY,
    ENDERECOSLOGRADOURO VARCHAR(50) NOT NULL,
    ENDERECOSNUMERO INT NOT NULL,
    ENDERECOSCOMPLEMENTO VARCHAR(50) NULL,
    ENDERECOSBAIRRO VARCHAR(50) NOT NULL,
    ENDERECOSCEP VARCHAR(50) NOT NULL,
    ENDERECOSCIDADE VARCHAR(50) NOT NULL,
    ENDERECOSUF VARCHAR(50) NOT NULL,
    CODCLIENTES INT CONSTRAINT FK_CLIENTES FOREIGN KEY REFERENCES CLIENTES(CODCLIENTES)
)

INSERT CLIENTES (CODCLIENTES, CLIENTENOME, CLIENTEDATACADASTRO, CLIENTESALARIO)
VALUES (1, 'KEMMEL PINTO', '1980-01-01', 9898.00),
       (2, 'JACINTO PINTO', '1980-01-01', 16310.00),
       (3, 'PAULA TEJANDO', '1980-01-01', 33000.00),
       (4, 'MIA REGAZZA', '1980-01-01', 47000.00),
       (5, 'KEVIN MAMAR', '1980-01-01', 15000.00)

INSERT ENDERECOS (ENDERECOSCOD, ENDERECOSLOGRADOURO, ENDERECOSNUMERO, ENDERECOSCOMPLEMENTO, ENDERECOSBAIRRO, ENDERECOSCEP, ENDERECOSCIDADE, ENDERECOSUF, CODCLIENTES)
VALUES (100, 'RUA 1', 111, 'AP 11', 'BAIRRO ITAIM BIBI', 'CEP 11.000-99', 'SAO PAULO', 'SP', 1),
       (200, 'RUA 2', 222, 'AP 22', 'BAIRRO SAO PAULO', 'CEP 22.000-99', 'SAO PAULO', 'SP', 2),
       (300, 'RUA 3', 333, 'AP 33', 'BAIRRO MOGI DAS CRUZES', 'CEP 33.000-99', 'SAO PAULO', 'SP', 3),
       (400, 'RUA 4', 444, 'AP 44', 'BAIRRO VILA MADALENA', 'CEP 44.000-99', 'SAO PAULO', 'SP', 4),
       (500, 'RUA 5', 555, 'AP 55', 'BAIRRO MORUMBI', 'CEP 55.000-99', 'SAO PAULO', 'SP', 5)

SELECT * FROM CLIENTES
SELECT * FROM ENDERECOS

UPDATE CLIENTES
    SET CLIENTEDATACADASTRO = '2042-10-09',
        CLIENTESLARIO = 50000
    WHERE CODCLIENTES >= 3 AND PESSOASNOME = 'PAULA TEJANDO'
    SET CLIENTEDATACADASTRO = '2093-08-03'
        CLIENTENOME = 'SUJIRO KIMIMAMMI'
    WHERE CODCLIENTES = 5

UPDATE ENDERECOS
    SET ENDERECOSLOGRADOURO = 'RUA ROY CAMPBELL',
        ENDERECOSNUMERO = 25,
        ENDERECOSCOMPLEMENTO = 'ESQUERDA',
        ENDERECOSBAIRRO = 'WASHINGTON',
        ENDERECOSCEP = '00.000-000',
        ENDERECOSCIDADE = 'MISHIGAN',
        ENDERECOSUF = 'EUA'
    WHERE PESSOASCOD = 3