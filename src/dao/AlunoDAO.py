import sqlite3
from src.models.AlunoModel import AlunoModel

class AlunoDAO:
    def __init__(self):
        pass

    def insert_aluno(self, aluno: AlunoModel):
        conn = sqlite3.connect('../registro_academico.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO alunos (cpf, nome, idade, email, endereco)
            VALUES (?, ?, ?, ?, ?)
        ''', (aluno.cpf, aluno.nome, aluno.idade, aluno.email, aluno.endereco))

        conn.commit()
        conn.close()

    def update_aluno(self, aluno: AlunoModel):
        conn = sqlite3.connect('../registro_academico.db')
        cursor = cursor()

        cursor.execute('''UPDATE alunos(nome,idade,email,endereco) VALUES(?,?,?,?)''',( aluno.nome, aluno.idade, aluno.email, aluno.endereco),
                       ''' WHERE alunos(cpf)== "%s"''',aluno.cpf)
        
        conn.commit()
        conn.close()

    def delete_aluno(self,aluno:AlunoModel):
        conn = sqlite3.connect('../registro_academico.db')
        cursor = cursor()

        cursor.execute('''DELETE alunos(cpf,nome,idade,email,endereco) WHERE alunos(cpf)== "%s"''',aluno.cpf)

        conn.commit()
        conn.close()

    def print_aluno(self):
        conn = sqlite3.connect('../registro_academico.db')
        cursor = cursor()

        cursor.execute(''' CODIGO''')

        conn.commit()
        conn.close()