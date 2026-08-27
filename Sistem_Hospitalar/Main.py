from Paciente import Paciente
from Medico import Medico
from Enfermeiro import Enfermeiro
from Departamento import Departamento
from Prontuario import Prontuario

# Cores
verde = "\033[92m"
azul = "\033[94m"
amarelo = "\033[93m"
reset = "\033[0m"

print(azul + "===== SISTEMA HOSPITALAR =====" + reset)

# Paciente
paciente = Paciente("Ana", "11111111111", 25)

# Profissionais
medico = Medico("Carmem", "22222222222", "M001", "Cardiologia")
enfermeiro = Enfermeiro("Romeu", "33333333333", "E001", "Manha")

# Departamento
departamento = Departamento("Cardiologia")
departamento.adicionar_profissional(medico)
departamento.adicionar_profissional(enfermeiro)

# Prontuario
prontuario = Prontuario()
prontuario.adicionar_nota("Paciente chegou para atendimento.")

print(verde + "\nPaciente:" + reset)
print(paciente.nome)

print(amarelo + "\nAtendimento:" + reset)
print(medico.atender_paciente(paciente))
print(enfermeiro.atender_paciente(paciente))

print(azul + "\nDepartamento:" + reset)
print(departamento.listar_profissional())

print(verde + "Prontuario:" + reset)
print(prontuario.mostrar())