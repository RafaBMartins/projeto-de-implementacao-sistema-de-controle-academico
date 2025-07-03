import sqlite3
import os
from typing import Optional
from src.models.AlunoModel import AlunoModel

class AlunoDAO:
    def __init__(self, aluno: Optional[AlunoModel] = None):
        self.aluno = aluno

    def abrir_conexao(self):
        db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'registro_academico.db')
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    
    def insert(self):
        try:
            conn = self.abrir_conexao()
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO alunos (cpf, nome, idade, email, cep)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.aluno.cpf, self.aluno.nome, self.aluno.idade, self.aluno.email, self.aluno.cep))

            conn.commit()
            return
        except sqlite3.Error as erro:
            raise erro
        finally:
            conn.close()
    
    def update(self):
        try:
            conn = self.abrir_conexao()
            cursor = conn.cursor()

            cursor.execute('''
                UPDATE alunos
                SET nome = COALESCE(NULLIF(?, ''), nome), idade = COALESCE(NULLIF(?, 0), idade), email = COALESCE(NULLIF(?, ''), email), cep = COALESCE(NULLIF(?, ''), cep)
                WHERE cpf = ?
            ''', (self.aluno.nome, self.aluno.idade, self.aluno.email, self.aluno.cep, self.aluno.cpf))

            conn.commit()
            return
        except sqlite3.Error as erro:
            raise erro
        finally:
            conn.close()
    
    def delete(self, cpf: str):
        try:
            conn = self.abrir_conexao()
            cursor = conn.cursor()

            cursor.execute('DELETE FROM alunos WHERE cpf = ?', (cpf,))

            conn.commit()

            if cursor.rowcount == 0:
                raise Exception("Aluno não encontrado")
            return
        except sqlite3.Error as erro:
            raise erro
        finally:
            conn.close()
    
    def fetchByCpf(self, cpf: str):
        try:
            conn = self.abrir_conexao()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM alunos WHERE cpf=?", (cpf,))
            response = cursor.fetchone()
            return response
        except sqlite3.Error as erro:
            raise erro
        finally:
            conn.close()
    
    def fetchAll(self):
        try:
            conn = self.abrir_conexao()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM alunos")
            response = cursor.fetchall()
            return response
        except sqlite3.Error as erro:
            raise erro
        finally:
            conn.close()