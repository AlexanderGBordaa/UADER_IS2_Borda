class Numero:
    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):
        print(f"Valor: {self.valor}")

class OperacionDecorator(Numero):
    def __init__(self, numero):
        self.numero = numero

    def mostrar(self):
        self.numero.mostrar()

class Sumar2(OperacionDecorator):
    def mostrar(self):
        print("Sumando 2")
        self.numero.valor += 2
        super().mostrar()

class Multiplicar2(OperacionDecorator):
    def mostrar(self):
        print("Multiplicando por 2")
        self.numero.valor *= 2
        super().mostrar()

class Dividir3(OperacionDecorator):
    def mostrar(self):
        print("Dividiendo por 3")
        self.numero.valor /= 3
        super().mostrar()

n = Numero(6)
n.mostrar()

print("\nCon operaciones:")
op = Dividir3(Multiplicar2(Sumar2(n)))
op.mostrar()
