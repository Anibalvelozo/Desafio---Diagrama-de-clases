class ListadoRespuestas:
    def __init__(self, usuario, respuestas: list = None):
        self.usuario = usuario
        self.respuestas = respuestas if respuestas else []
