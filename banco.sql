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