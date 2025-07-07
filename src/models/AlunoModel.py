from typing import Optional

class AlunoModel:
    def __init__(self, cpf: str, nome: str, idade: int, email: str, cep: str, logradouro: str = None, bairro: str = None, cidade: str = None):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade