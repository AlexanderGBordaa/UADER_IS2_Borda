import os
#*--------------------------------------------------------------------
#* Design pattern memento, extendido con undo selectivo
#*--------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		self.file = file
		self.content = content

class FileWriterUtility:
	def __init__(self, file):
		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string

	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content

class FileWriterCaretaker:
	def __init__(self):
		self.history = []

	def save(self, writer):
		memento = writer.save()
		if len(self.history) >= 4:
			self.history.pop(0)  # Elimina el más antiguo
		self.history.append(memento)

	def undo(self, writer, index):
		if 0 <= index < len(self.history):
			writer.undo(self.history[-(index + 1)])
		else:
			print(f"No se puede recuperar el estado {index}. Solo hay {len(self.history)} guardados.")

#*--------------------------------------------------------------------
#* Prueba del patrón Memento con múltiples niveles de undo
#*--------------------------------------------------------------------
if __name__ == '__main__':
	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar")
	writer = FileWriterUtility("GFG.txt")

	print("\n[1] Se graba algo y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content)
	caretaker.save(writer)

	print("\n[2] Se graba más info y se salva")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content)
	caretaker.save(writer)

	print("\n[3] Más material agregado y guardado")
	writer.write("Ejemplo de patrón Memento extendido\n")
	print(writer.content)
	caretaker.save(writer)

	print("\n[4] Otro agregado más y se guarda")
	writer.write("Última línea guardada\n")
	print(writer.content)
	caretaker.save(writer)

	print("\n[5] Agregado sin guardar")
	writer.write("Esto NO se guardó\n")
	print(writer.content)

	# Probar undo en diferentes niveles
	for i in range(4):
		print(f"\nDeshacer con undo({i}):")
		caretaker.undo(writer, i)
		print(writer.content)

	print("\nIntento de undo(4) (fuera de rango):")
	caretaker.undo(writer, 4)
