class Consulta:
    def __init__(self, medico, paciente, data):
        self.medico = medico
        self.paciente = paciente
        self.data = data
#Associacao - apenas "referencia" os dois, nao vai cria nem apaga

    def detalhes(self):
        return f"Data: {self.data} | Medico: {self.medico.nome} | Paciente: {self.paciente.nome}"