class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.profissional = []  #lista de profissionais

    def adicionar_profissional(self, profissional): 
        self.profissional.append(profissional)

    def listar_profissional(self):
        if len(self.profissional) == 0:
            return f"Departamento: {self.nome} \nNenhum profissional cadastrado."

        texto = f"Departamento: {self.nome}\nProfissionais:\n"
        for p in self.profissional:
            texto += f"Nome: {p.nome} | Registro: {p.registro}\n"
            return texto 