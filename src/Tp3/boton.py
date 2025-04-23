class Boton:
    def render(self):
        pass

class BotonWindows(Boton):
    def render(self):
        print("Botón estilo Windows")

class BotonLinux(Boton):
    def render(self):
        print("Botón estilo Linux")

class GUIFactory:
    def crear_boton(self):
        pass

class WindowsFactory(GUIFactory):
    def crear_boton(self):
        return BotonWindows()

class LinuxFactory(GUIFactory):
    def crear_boton(self):
        return BotonLinux()

class Aplicacion:
    def __init__(self, factory):
        self.boton = factory.crear_boton()

    def mostrar_boton(self):
        self.boton.render()
