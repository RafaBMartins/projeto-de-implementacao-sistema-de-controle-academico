import sqlite3
from typing import Optional
import os
from src.models.MatriculaModel import MatriculaModel

class MatriculaDAO:
    def __init__(self, matricula: Optional[MatriculaModel] = None):
        self.matricula = matricula
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
                INSERT INTO matriculas (cpf_aluno, codigo_disciplina)
                VALUES (?, ?)
            ''', (self.matricula.cpf_aluno, self.matricula.codigo_disciplina))

            conn.commit()
            return
        except sqlite3.Error as erro:
            raise erro
        finally:
            conn.close()
    
    def delete(self, cpf_aluno, codigo_disciplina):
        try:
            conn = self.abrir_conexao()
            cursor = conn.cursor()

            cursor.execute('DELETE FROM matriculas WHERE cpf_aluno = ? AND codigo_disciplina = ?', (cpf_aluno, codigo_disciplina))

            conn.commit()

            if cursor.rowcount == 0:
                raise Exception("Matricula não encontrada")
            return
        except sqlite3.Error as erro:
            raise erro
        finally:
            conn.close()
    
    def fetchAll(self):
        try:
            conn = self.abrir_conexao()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM matriculas")
            response = cursor.fetchall()
            return response
        except sqlite3.Error as erro:
            raise erro
        finally:
            conn.close()