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
