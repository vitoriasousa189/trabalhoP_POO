from ProfissionalSaude import ProfissionalSaude

class Enfermeiro(ProfissionalSaude):
    def __init__(self, nome, cpf, registro, turno):
        super().__init__(nome, cpf, registro)
        self.turno = turno

#polimorfismo - enfermeiro trabalha de outro jeito

    def atender_paciente(self, paciente):
        return f"Enfermeiro {self.nome} faz triagem e mede sinais vitais de {paciente.nome}"