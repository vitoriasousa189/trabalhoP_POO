class ProfissionalSaude():
    def __init__(self, nome, cpf, registro):
        self.nome = nome
        self.cpf = cpf 
        self.registro = registro
#metodo que vamos subescrever (polimorfismo)

    def atender_paciente(self, paciente):
        return f"Atendimento foi iniciado para o(a) paciente {paciente.nome}."