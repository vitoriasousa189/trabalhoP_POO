class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.profissional = []  #lista de profissionais

    def adicionar_profissional(self, profissional): 
        self.profissional.append(profissional)

    def listar_profissional(self):
        if len(self.profissional) == 0:
            print(f"Departamento: {self.nome} \nNenhum profissional cadastrado.")
        else:
            print(f"Departamento: {self.nome}")
            for profissional in self.profissional:
                print(f"Nome: {profissional.nome} | Registro: {profissional.registro}\n")
      
                