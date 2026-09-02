from Paciente import Paciente
from Medico import Medico
from Enfermeiro import Enfermeiro
from Departamento import Departamento
from Prontuario import Prontuario

verde = "\033[92m"
azul = "\033[94m"
reset = "\033[0m"

print(azul + "===== SISTEMA HOSPITALAR =====" + reset)

while True:
    print("\n1. Cadastrar Paciente")
    print("2. Atender Paciente")
    print("3. Ver Prontuario")
    print("0. Sair")
    
    op = input("Escolha uma opção: ")
    
    if op == "0":
        print(verde + "Saindo... Até logo!" + reset)
        break
    elif op == "1":
        nome = input("Nome do paciente: ")
        cpf = input("CPF: ")
        idade = int(input("Idade: "))
        paciente = Paciente(nome, cpf, idade)
        print(verde + f"Paciente {nome} cadastrado!" + reset)
    elif op == "2":
        m_nome = input("Nome do médico: ")
        m_cpf = input("CPF do médico: ")
        m_reg = input("Registro (CRM): ")
        m_esp = input("Especialidade: ")
        medico = Medico(m_nome, m_cpf, m_reg, m_esp)
        
        p_nome = input("Nome do paciente: ")
        p_cpf = input("CPF do paciente: ")
        p_idade = int(input("Idade do paciente: "))
        paciente = Paciente(p_nome, p_cpf, p_idade)
        
        dept = Departamento(m_esp)
        dept.adicionar_profissional(medico)
        print(medico.atender_paciente(paciente))
    elif op == "3":
        pront = Prontuario()
        nota = input("Escreva a nota do prontuário: ")
        pront.adicionar_nota(nota)
        pront.mostrar()
    else:
        print("Opção inválida! Tente de novo!")