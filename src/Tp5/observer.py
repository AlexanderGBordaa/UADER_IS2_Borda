class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def emit(self, id_code):
        print(f"\nID emitido: {id_code}")
        for observer in self.observers:
            observer.notify(id_code)

class Observer:
    def __init__(self, id_code):
        self.id_code = id_code

    def notify(self, emitted_id):
        if emitted_id == self.id_code:
            print(f"¡Coincidencia! Observer con ID {self.id_code} activado.")

# Crear sujeto y observadores
subject = Subject()

observer1 = Observer("A123")
observer2 = Observer("B456")
observer3 = Observer("C789")
observer4 = Observer("X999")

subject.subscribe(observer1)
subject.subscribe(observer2)
subject.subscribe(observer3)
subject.subscribe(observer4)

# Emitimos 8 códigos
emitted_ids = ["B456", "Z000", "A123", "C789", "X999", "Y111", "B456", "M321"]

for id_code in emitted_ids:
    subject.emit(id_code)
