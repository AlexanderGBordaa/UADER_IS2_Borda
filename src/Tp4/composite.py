class Componente:
    def mostrar(self, nivel=0):
        raise NotImplementedError

class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Pieza: {self.nombre}")

class SubConjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, comp):
        self.componentes.append(comp)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"SubConjunto: {self.nombre}")
        for c in self.componentes:
            c.mostrar(nivel + 1)

principal = SubConjunto("Producto Principal")
for i in range(1, 4):
    sub = SubConjunto(f"SubConjunto{i}")
    for j in range(1, 5):
        sub.agregar(Pieza(f"Pieza{i}.{j}"))
    principal.agregar(sub)

sub_opcional = SubConjunto("SubConjuntoOpcional")
for j in range(1, 5):
    sub_opcional.agregar(Pieza(f"PiezaOpcional.{j}"))
principal.agregar(sub_opcional)

principal.mostrar()
