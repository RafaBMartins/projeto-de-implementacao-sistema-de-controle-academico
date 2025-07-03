import sqlite3
from typing import Optional
import os
from src.models.DisciplinaModel import DisciplinaModel

class DisciplinaDAO:
    def __init__(self, disciplina: Optional[DisciplinaModel] = None):
        self.disciplina = disciplina
    
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
                INSERT INTO disciplinas (codigo, nome, carga_horaria, professor)
                VALUES (?, ?, ?, ?)
            ''', (self.disciplina.codigo, self.disciplina.nome, self.disciplina.carga_horaria, self.disciplina.professor))

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
                UPDATE disciplinas
                SET nome = COALESCE(NULLIF(?, ''), nome), carga_horaria = COALESCE(NULLIF(?, 0), carga_horaria), professor = COALESCE(NULLIF(?, ''), professor)
                WHERE codigo = ?
            ''', (self.disciplina.nome, self.disciplina.carga_horaria, self.disciplina.professor, self.disciplina.codigo))

            conn.commit()
            return
        except sqlite3.Error as erro:
            raise erro
        finally:
            conn.close()
    
    def delete(self, codigo: str):
        try:
            conn = self.abrir_conexao()
            cursor = conn.cursor()

            cursor.execute('DELETE FROM disciplinas WHERE codigo = ?', (codigo,))

            conn.commit()

            if cursor.rowcount == 0:
                raise Exception("Disciplina não encontrada")
            return
        except sqlite3.Error as erro:
            raise erro
        finally:
            conn.close()
    
    def fetchByCodigo(self, codigo: str):
        try:
            conn = self.abrir_conexao()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM disciplinas WHERE codigo=?", (codigo,))
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
            cursor.execute("SELECT * FROM disciplinas")
            response = cursor.fetchall()
            return response
        except sqlite3.Error as erro:
            raise erro
        finally:
            conn.close()