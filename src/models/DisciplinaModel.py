class DisciplinaModel:
    def __init__(self, codigo: str, nome: str, carga_horaria: int, professor: str):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.professor = professor