import copy

class Prototipo:
    def __init__(self, nombre):
        self.nombre = nombre

    def clonar(self):
        return copy.deepcopy(self)

    def mostrar(self):
        print(f"Soy una copia de: {self.nombre}")
