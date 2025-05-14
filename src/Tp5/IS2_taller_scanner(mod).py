import os

#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state extendido con memorias
#*--------------------------------------------------------------------

"""State class: Base State class"""
class State:
	def scan(self):
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

#*------- Implementa como barrer las estaciones de AM
class AmState(State):
	def __init__(self, radio):
		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos = 0
		self.name = "AM"

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

	def toggle_memoria(self):
		print("Cambiando a MEMORIA")
		self.radio.state = self.radio.memoriastate

#*------- Implementa como barrer las estaciones de FM
class FmState(State):
	def __init__(self, radio):
		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = 0
		self.name = "FM"

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

#*------- Estado que recorre memorias M1 a M4
class MemoriaState(State):
	def __init__(self, radio):
		self.radio = radio
		self.stations = list(radio.memorias.values())
		self.names = list(radio.memorias.keys())
		self.pos = 0
		self.name = "MEM"

	def scan(self):
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Memoria {}: {} {}".format(self.names[self.pos], self.stations[self.pos][0], self.stations[self.pos][1]))

	def toggle_amfm(self):
		print("Volviendo a FM")
		self.radio.state = self.radio.fmstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:
	def __init__(self):
		self.fmstate = FmState(self)
		self.amstate = AmState(self)
		self.memoriastate = MemoriaState(self)
		self.state = self.fmstate

		# Frecuencias memorizadas (tipo, frecuencia)
		self.memorias = {
			"M1": ("AM", "1470"),
			"M2": ("FM", "90.1"),
			"M3": ("AM", "1320"),
			"M4": ("FM", "100.3")
		}

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def toggle_memoria(self):
		if hasattr(self.state, 'toggle_memoria'):
			self.state.toggle_memoria()
		else:
			print("Cambio a MEM no permitido desde", self.state.name)

	def scan(self):
		self.state.scan()

#*--------------------- MAIN ---------------------
if __name__ == "__main__":
	os.system("clear")
	print("\nCrea un objeto radio y almacena las siguientes acciones")

	radio = Radio()
	# Simulación: 3 FM → AM → 3 AM → MEM → 4 MEMORIAS → FM → repetir
	actions = (
		[radio.scan] * 3 +
		[radio.toggle_amfm] +
		[radio.scan] * 3 +
		[radio.toggle_memoria] +
		[radio.scan] * 4 +
		[radio.toggle_amfm]
	) * 2  # Repetir dos veces

	print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
	for action in actions:
		action()
