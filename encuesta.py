class Encuesta:
    def __init__(self, nombre: str, preguntas: list):
        self.nombre = nombre
        self.preguntas = preguntas
        self.listados_respuestas = []

    def mostrar_encuesta(self):
        print(f"Nombre de la encuesta: {self.nombre}")
        print("Preguntas:")
        for pregunta in self.preguntas:
            pregunta.mostrar_pregunta()

    def agregar_listado_respuestas(self, listado_respuestas):
        self.listados_respuestas.append(listado_respuestas)


class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, preguntas: list, edad_minima: int, edad_maxima: int):
        super().__init__(nombre, preguntas)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    def agregar_listado_respuestas(self, listado_respuestas):
        usuario_edad = listado_respuestas.usuario.edad
        if self.edad_minima <= usuario_edad <= self.edad_maxima:
            super().agregar_listado_respuestas(listado_respuestas)
        else:
            print("El usuario no cumple con el rango de edad para esta encuesta.")


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, preguntas: list, regiones_permitidas: list):
        super().__init__(nombre, preguntas)
        self.regiones_permitidas = regiones_permitidas

    def agregar_listado_respuestas(self, listado_respuestas):
        usuario_region = listado_respuestas.usuario.region
        if usuario_region in self.regiones_permitidas:
            super().agregar_listado_respuestas(listado_respuestas)
        else:
            print("El usuario no pertenece a una región permitida para esta encuesta.")
