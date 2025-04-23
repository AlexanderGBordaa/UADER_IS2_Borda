class Hamburguesa:
    def __init__(self, metodo_entrega):
        self.metodo_entrega = metodo_entrega

    def entregar(self):
        print(f"Hamburguesa entregada por: {self.metodo_entrega}")

class HamburguesaFactory:
    @staticmethod
    def crear_entrega(tipo):
        if tipo == "mostrador":
            return Hamburguesa("mostrador")
        elif tipo == "cliente":
            return Hamburguesa("retirada por el cliente")
        elif tipo == "delivery":
            return Hamburguesa("delivery")
        else:
            raise ValueError("Método de entrega no válido.")
