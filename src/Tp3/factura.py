class Factura:
    def __init__(self, total, condicion_impositiva):
        self.total = total
        self.condicion_impositiva = condicion_impositiva

    def imprimir(self):
        print(f"Factura: ${self.total}, Condición: {self.condicion_impositiva}")

class FacturaFactory:
    @staticmethod
    def crear_factura(total, condicion):
        if condicion in ["IVA Responsable", "IVA No Inscripto", "IVA Exento"]:
            return Factura(total, condicion)
        else:
            raise ValueError("Condición impositiva inválida.")
