class Prontuario:
    def __init__(self):
        self.registro = []

    def adicionar_nota(self, nota):
        self.registro.append(nota)

    def mostrar(self):
        if not self.registro:
            return "Prontuario vazio"
        texto = ""
        for item in self.registro:
            texto = texto + item + "\n"
        return texto