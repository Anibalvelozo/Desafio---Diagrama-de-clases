from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, ayuda: str = None, requerida: bool = True, alternativas: list = None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = alternativas if alternativas else []

    def mostrar(self):
        print(f"Enunciado: {self.enunciado}")
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")
        print("Alternativas:")
        for alternativa in self.alternativas:
            alternativa.mostrar()
