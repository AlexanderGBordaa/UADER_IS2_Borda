class Avion:
    def __init__(self):
        self.body = None
        self.turbinas = None
        self.alas = None
        self.tren = None

    def mostrar(self):
        print(f"Avión con cuerpo: {self.body}, {self.turbinas}, {self.alas}, {self.tren}")

class AvionBuilder:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self):
        self.avion.body = "Cuerpo de aluminio"
        return self

    def construir_turbinas(self):
        self.avion.turbinas = "2 turbinas"
        return self

    def construir_alas(self):
        self.avion.alas = "2 alas"
        return self

    def construir_tren(self):
        self.avion.tren = "Tren de aterrizaje retráctil"
        return self

    def obtener_avion(self):
        return self.avion
