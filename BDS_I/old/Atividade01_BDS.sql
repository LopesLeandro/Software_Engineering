'''
Criar um diagrama de banco de dados no BrModelo, de um assunto de seu interesse. Esse banco deve conter pelo menos duas tabelas/entidades.
Essas entidades devem possuir pelo menos 4 atributos.
As entidades devem estar relacionadas entre si por chaves primárias e estrangeiras.
Você deverá inserir pelo menos 4 linhas em cada entidade.
Você deverá executar pelo menos duas atuliazações de dados.
IMPORTANTE: Você deverá entregar um arquivo com a extensão .SQL para que eu possa rodar e corrigir. O arquivo deverá conter:

CREATE DATABASE, TABLE, INSERT, UPDATE E SELECT.
'''

-- Criando o banco de dados
CREATE DATABASE IF NOT EXISTS Atividade01_BDS;
USE Atividade01_BDS;

-- Criando a tabela de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- Criando a tabela de produtos
