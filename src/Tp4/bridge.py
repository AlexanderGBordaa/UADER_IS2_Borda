class TrenLaminador:
    def producir(self, lamina):
        raise NotImplementedError

class Tren5mts(TrenLaminador):
    def producir(self, lamina):
        print(f"Produciendo lámina de 5 metros para {lamina}")

class Tren10mts(TrenLaminador):
    def producir(self, lamina):
        print(f"Produciendo lámina de 10 metros para {lamina}")

class LaminaAcero:
    def __init__(self, espesor, ancho, tren: TrenLaminador):
        self.espesor = espesor
        self.ancho = ancho
        self.tren = tren

    def producir(self):
        self.tren.producir(self)

    def __str__(self):
        return f"Lámina {self.espesor}\" x {self.ancho}m"
