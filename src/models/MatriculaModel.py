class MatriculaModel:
    def __init__(self, id: int, cpf_aluno: str, codigo_disciplina: str, data_hora: str):
        self.id = id
        self.cpf_aluno = cpf_aluno
        self.codigo_disciplina = codigo_disciplina
        self.data_hora = data_hora