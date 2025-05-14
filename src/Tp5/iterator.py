class CharIterator:
    def __init__(self, string):
        self.string = string

    def forward(self):
        for char in self.string:
            yield char

    def reverse(self):
        for char in reversed(self.string):
            yield char

# Ejemplo de uso
iterator = CharIterator("Hola Mundo")
print("Dirección directa:")
for c in iterator.forward():
    print(c, end=' ')

print("\nDirección inversa:")
for c in iterator.reverse():
    print(c, end=' ')
