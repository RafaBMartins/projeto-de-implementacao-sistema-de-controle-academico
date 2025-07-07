import sqlite3
from typing import Optional
import requests
from src.models.AlunoModel import AlunoModel
from src.dao.AlunoDAO import AlunoDAO

class AlunoControler:
    def __init__(self, aluno: Optional[AlunoModel] = None):
        self.aluno = aluno

    def buscar_endereco(self):
        try:
            url = f"https://viacep.com.br/ws/{self.aluno.cep}/json/"
            response = requests.get(url)
            return response.json()
        except Exception as erro:
            raise erro
        
    def cadastrar_aluno(self):
        if not self.aluno.cpf.strip():
            raise Exception("O campo CPF é obrigatório")
        if not self.aluno.nome.strip():
            raise Exception("O campo Nome é obrigatório")
        if not self.aluno.email.strip():
            raise Exception("O campo E-mail é obrigatório")
        if not self.aluno.cep.strip():
            raise Exception("O campo CEP é obrigatório")

        try:
            endereco = self.buscar_endereco()
            self.aluno.logradouro = endereco['logradouro']
            self.aluno.bairro = endereco['bairro']
            self.aluno.cidade = endereco['localidade']
            aluno_dao = AlunoDAO(self.aluno)
            aluno_dao.insert()
            return
        except sqlite3.IntegrityError as erro:
            if "UNIQUE constraint failed" in str(erro):
                raise Exception("Aluno já cadastrado")
            raise Exception(f"Erro ao cadastrar aluno: {erro}")
        except sqlite3.Error as erro:
            raise Exception(f"Erro ao cadastrar aluno: {erro}")
        except requests.exceptions.RequestException:
            raise Exception(f"CEP inválido")
        
    def atualizar_aluno(self):
        try:
            endereco = self.buscar_endereco()
            self.aluno.logradouro = endereco['logradouro']
            self.aluno.bairro = endereco['bairro']
            self.aluno.cidade = endereco['localidade']
            aluno_dao = AlunoDAO(self.aluno)
            aluno_dao.update()
            return
        except sqlite3.Error as erro:
            raise Exception(f"Erro ao atualizar aluno: {erro}")
        except requests.exceptions.RequestException:
            raise Exception(f"CEP inválido")
    
    def deletar_aluno(self, cpf: str):
        try:
            aluno_dao = AlunoDAO()
            aluno_dao.delete(cpf)
            return
        except sqlite3.IntegrityError as erro:
            if "FOREIGN KEY constraint failed" in str(erro):
                raise Exception("Aluno possui matrícula cadastrada")
            raise Exception(f"Erro ao deletar aluno: {erro}")
        except sqlite3.Error:
            raise Exception("Aluno não encontrado")
        except Exception as erro:
            raise erro
    
    def buscar_por_cpf(self, cpf: str):
        try:
            aluno_dao = AlunoDAO()
            response = aluno_dao.fetchByCpf(cpf)
            if not response:
                raise Exception("Aluno não encontrado")
            aluno = AlunoModel(response[0], response[1], response[2], response[3], response[4], response[5], response[6], response[7])
            return aluno
        except sqlite3.Error as erro:
            raise Exception(f"Erro ao buscar aluno: {erro}")
    
    def buscar_todos_alunos(self):
        try:
            aluno_dao = AlunoDAO()
            response = aluno_dao.fetchAll()
            if not response:
                return []
            alunos = [AlunoModel(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4], aluno[5], aluno[6], aluno[7]) for aluno in response]
            return alunos
        except sqlite3.Error as erro:
            raise Exception(f"Erro ao buscar todos os alunos: {erro}")