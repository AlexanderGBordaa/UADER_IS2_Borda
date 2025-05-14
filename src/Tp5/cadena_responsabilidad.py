class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, number):
        if self.successor:
            return self.successor.handle(number)
        else:
            print(f"{number} no consumido.")
            return None

class PrimeHandler(Handler):
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            print(f"{number} consumido por PrimeHandler")
        else:
            super().handle(number)

class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"{number} consumido por EvenHandler")
        else:
            super().handle(number)

# Cadena: PrimeHandler -> EvenHandler
chain = PrimeHandler(successor=EvenHandler())

for i in range(1, 101):
    chain.handle(i)
