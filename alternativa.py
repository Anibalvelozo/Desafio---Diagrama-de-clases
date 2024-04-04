class Alternativa:
    def __init__(self, contenido: str, ayuda: str = None):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar(self):
        print(f"Contenido: {self.contenido}")
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")
