from src.models.AlunoModel import AlunoModel
from src.dao.AlunoDAO import AlunoDAO

class AlunoControler:
    def __init__(self, aluno: AlunoModel):
        self.aluno = aluno

    def cadastrar_aluno(self, aluno: AlunoModel):
        try:
            AlunoDAO().insert_aluno(aluno)
            return True
        except:
            return False