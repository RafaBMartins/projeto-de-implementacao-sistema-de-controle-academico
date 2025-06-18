CREATE TABLE endereco (
    id SERIAL NOT NULL,
    cep VARCHAR(8) NOT NULL,
    logradouro VARCHAR(100),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    estado VARCHAR(2),
    CONSTRAINT pk_endereco PRIMARY KEY (id)
);

-- Criação da tabela aluno
CREATE TABLE aluno (
    cpf VARCHAR(11) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    email VARCHAR(100) NOT NULL,
    id_endereco INT NOT NULL,
    CONSTRAINT pk_aluno PRIMARY KEY (cpf),
    CONSTRAINT fk_id_endereco FOREIGN KEY (id_endereco) REFERENCES endereco(id)
);

-- Criação da tabela disciplina
CREATE TABLE disciplina (
    codigo VARCHAR(10) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    carga_horaria INT NOT NULL,
    professor VARCHAR(100) NOT NULL,
    CONSTRAINT pk_disciplina PRIMARY KEY (codigo)
);

-- Criação da tabela matricula
CREATE TABLE matricula (
    id SERIAL NOT NULL,
    cpf_aluno VARCHAR(11) NOT NULL,
    codigo_disciplina VARCHAR(10) NOT NULL,
    data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_matricula PRIMARY KEY (id),
    CONSTRAINT fk_cpf_aluno FOREIGN KEY (cpf_aluno) REFERENCES aluno(cpf),
    CONSTRAINT fk_codigo_disciplina FOREIGN KEY (codigo_disciplina) REFERENCES disciplina(codigo)
);

-- import sqlite3 as sq3
-- import requests 
-- import json


-- #código para cadastrar novo aluno
-- while True:
--     try:
--         banco=sq3.connect('controle_academico.db')

--         cursor=banco.cursor()

--         nome_aluno=input('Informe o nome: ')
--         cpf=str(input('Informe o CPF: '))
--         idade=str(input('Informe a idade: '))
--         email=input('Informe o e-mail: ')
--         cep=input('Informe o CEP: ')

--         endereco="cep" #Implementar conexão com correios
--         cursor.execute('INSERT INTO Aluno VALUES("'+cpf+'","'+nome_aluno+'","'+idade+'","'+email+'","'+endereco+'")')

--         banco.commit()
        
--     except sq3.IntegrityError:
--         print("CPF já cadastrado no sistema!")
--         break
--     except sq3.Error as erro:
--         print("Erro inesperado: {erro}")
--         break
--     finally:
--         banco.close()
--     break
-- #codigo para atualizar um aluno

-- cpf=input('Informe o CPF do aluno a ser atualizado')

-- banco=sq3.connect('controle_academico.db')

-- cursor=banco.cursor()

-- cursor.execute("SELECT * FROM Aluno WHERE cpf =?",(cpf,))

-- registro=cursor.fetchone()

-- banco.close()

-- if not registro:
--     print("CPF não encontrado")
-- else:

-- import streamlit as st

-- import sqlite3 as sq3

-- while True:
--     try:
--         banco=sq3.connect('controle_academico.db')

--         cursor=banco.cursor()

--         codigo_disc=str(input('Informe o código da disciplina: '))
--         nome_disc=input('Informe o nome da disciplina a ser cadastrada: ')
--         carga_horaria=str(input('Informe a carga horária da disciplina: '))
--         nome_professor=input('Informe o nome do professor da matéria: ')

--         cursor.execute('INSERT INTO Disciplina VALUES("'+codigo_disc+'","'+nome_disc+'","'+carga_horaria+'","'+nome_professor+'","'+endereco+'")')

--         banco.commit()
        
--     except sq3.IntegrityError:
--         print("Código de disciplina já cadastrado no sistema!")
--         #implementar para quando esse erro aparecer, redirecionar para edição
--         #da disciplina com o código informado
--         break
--     except sq3.Error as erro:
--         print("Erro inesperado: {erro}")
--         break
--     finally:
--         banco.close()
--     break
