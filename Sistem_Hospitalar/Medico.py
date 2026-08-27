from ProfissionalSaude import ProfissionalSaude

class Medico(ProfissionalSaude):
    def __init__(self, nome, cpf, registro, especialidade):
#pegar os atributos da classe mae
        super().__init__(nome, cpf, registro)
        self.especialidade = especialidade
#polimorfismo - medico atende de um jeito
    def atender_paciente(self, paciente):
        return f"Medico {self.nome} faz consulta e passa receita para {paciente.nome}"