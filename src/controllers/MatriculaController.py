import sqlite3
from typing import Optional
from src.models.MatriculaModel import MatriculaModel
from src.dao.MatriculaDAO import MatriculaDAO

class MatriculaController:
    def __init__(self, matricula: Optional[MatriculaModel] = None):
        self.matricula = matricula
    
    def cadastrar_matricula(self):
        try:
            if not self.matricula.cpf_aluno.strip():
                raise Exception("O campo CPF Aluno é obrigatório")
            if not self.matricula.codigo_disciplina.strip():
                raise Exception("O campo Código Disciplina é obrigatório")

            matricula_dao = MatriculaDAO(self.matricula)
            matricula_dao.insert()
        except sqlite3.IntegrityError as erro:
            if "FOREIGN KEY constraint failed" in str(erro):
                raise Exception("Disciplina/Aluno não encontrados")
            raise Exception(f"Erro ao cadastrar matricula: {erro}")
        except Exception as erro_message:
            raise Exception(erro_message)
    
    def deletar_matricula(self, cpf_aluno, codigo_disciplina):
        try:
            matricula_dao = MatriculaDAO()
            matricula_dao.delete(cpf_aluno, codigo_disciplina)
        except Exception as erro_message:
            raise Exception(erro_message)
    
    def buscar_todas_matriculas(self):
        try:
            matricula_dao = MatriculaDAO()
            response = matricula_dao.fetchAll()
            if not response:
                return []
            matriculas = [MatriculaModel(matricula[0], matricula[1], matricula[2]) for matricula in response]
            return matriculas
        except Exception as erro_message:
            raise Exception(erro_message)
