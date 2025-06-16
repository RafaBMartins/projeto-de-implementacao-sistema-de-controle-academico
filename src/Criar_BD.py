import sqlite3 as sq3

banco=sq3.connect('controle_academico.db')

cursor=banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS " \
"Disciplina(codigo VARCHAR(10) NOT NULL," \
"nome VARCHAR(100) NOT NULL," \
"carga_horaria INT NOT NULL," \
"professor VARCHAR(100) NOT NULL," \
"CONSTRAINT pk_disciplina PRIMARY KEY (codigo))")

cursor.execute("CREATE TABLE IF NOT EXISTS " \
"Matricula(id SERIAL NOT NULL,"\
"cpf_aluno VARCHAR(11) NOT NULL," \
"codigo_disciplina VARCHAR(10) NOT NULL," \
"data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP," \
"CONSTRAINT pk_matricula PRIMARY KEY (id)," \
"CONSTRAINT fk_cpf_aluno FOREIGN KEY (cpf_aluno) REFERENCES aluno(cpf)," \
"CONSTRAINT fk_codigo_disciplina FOREIGN KEY (codigo_disciplina) REFERENCES disciplina(codigo))")

cursor.execute("CREATE TABLE IF NOT EXISTS " \
"Aluno(cpf VARCHAR(11) NOT NULL," \
"nome VARCHAR(100) NOT NULL," \
"idade INT NOT NULL," \
"email VARCHAR(100)NOT NULL," \
"id_endereco INT NOT NULL," \
"CONSTRAINT pk_aluno PRIMARY KEY (cpf)," \
"CONSTRAINT fk_id_endereco FOREIGN KEY (id_endereco) REFERENCES endereco(id))")

banco.commit()
banco.close()   