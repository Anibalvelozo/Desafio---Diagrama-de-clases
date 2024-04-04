class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        self.correo = correo
        self.edad = edad
        self.region = region

    def modificar_edad(self, nueva_edad: int):
        self.edad = nueva_edad

    def modificar_region(self, nueva_region: int):
        self.region = nueva_region
