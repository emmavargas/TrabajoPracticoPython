class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista = []

    def agregar(self, dato):
        self.lista.append(dato)
