from Prontuario import Prontuario

class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
#composicao do prontuario criado aqui

        self.prontuario = Prontuario()

