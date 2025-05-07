class LetraFlyweight:
    def __init__(self, caracter, fuente, tamaño):
        self.caracter = caracter
        self.fuente = fuente
        self.tamaño = tamaño

    def mostrar(self, posicion):
        print(f"{self.caracter} en {posicion} con fuente {self.fuente} y tamaño {self.tamaño}")

class FabricaLetras:
    _letras = {}

    def get_letra(self, caracter, fuente, tamaño):
        clave = (caracter, fuente, tamaño)
        if clave not in self._letras:
            self._letras[clave] = LetraFlyweight(caracter, fuente, tamaño)
        return self._letras[clave]

fabrica = FabricaLetras()
texto = [
    ('H', 0), ('o', 1), ('l', 2), ('a', 3)
]

for char, pos in texto:
    letra = fabrica.get_letra(char, "Arial", 12)
    letra.mostrar(pos)
