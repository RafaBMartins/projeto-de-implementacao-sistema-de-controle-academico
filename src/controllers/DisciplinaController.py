import sqlite3
from typing import Optional
from src.models.DisciplinaModel import DisciplinaModel
from src.dao.DisciplinaDAO import DisciplinaDAO

class DisciplinaController:
    def __init__(self, disciplina: Optional[DisciplinaModel] = None):
        self.disciplina = disciplina
    
    def cadastrar_disciplina(self):
        if not self.disciplina.codigo.strip():
            raise Exception("O campo Código é obrigatório")
        if not self.disciplina.nome.strip():
            raise Exception("O campo Nome é obrigatório")
        if not self.disciplina.professor.strip():
            raise Exception("O campo Professor é obrigatório")

        try:
            disciplina_dao = DisciplinaDAO(self.disciplina)
            disciplina_dao.insert()
            return
        except sqlite3.IntegrityError as erro:
            if "UNIQUE constraint failed" in str(erro):
                raise Exception("Disciplina já cadastrada")
            raise Exception(f"Erro ao cadastrar disciplina: {erro}")
        except sqlite3.Error as erro:
            raise Exception(f"Erro ao cadastrar disciplina: {erro}")
    
    def atualizar_disciplina(self):
        try:
            disciplina_dao = DisciplinaDAO(self.disciplina)
            disciplina_dao.update()
            return
        except sqlite3.Error as erro:
            raise Exception(f"Erro ao atualizar disciplina: {erro}")
    
    def deletar_disciplina(self, codigo: str):
        try:
            disciplina_dao = DisciplinaDAO()
            disciplina_dao.delete(codigo)
            return
        except sqlite3.IntegrityError as erro:
            if "FOREIGN KEY constraint failed" in str(erro):
                raise Exception("Disciplina possui matrícula cadastrada")
            raise Exception(f"Erro ao deletar disciplina: {erro}")
        except sqlite3.Error:
            raise Exception("Disciplina não encontrada")
        except Exception as erro:
            raise erro
    
    def buscar_por_codigo(self, codigo: str):
        try:
            disciplina_dao = DisciplinaDAO()
            response = disciplina_dao.fetchByCodigo(codigo)
            if not response:
                raise Exception("Disciplina não encontrada")
            disciplina = DisciplinaModel(response[0], response[1], response[2], response[3])
            return disciplina
        except sqlite3.Error as erro:
            raise Exception(f"Erro ao buscar disciplina: {erro}")
    
    def buscar_todas_disciplinas(self):
        try:
            disciplina_dao = DisciplinaDAO()
            response = disciplina_dao.fetchAll()
            if not response:
                return []
            disciplinas = [DisciplinaModel(disciplina[0], disciplina[1], disciplina[2], disciplina[3]) for disciplina in response]
            return disciplinas
        except sqlite3.Error as erro:
            raise Exception(f"Erro ao buscar todas as disciplinas: {erro}")