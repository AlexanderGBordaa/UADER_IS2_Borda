#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import math

class Factorial:
    def __init__(self, min_value, max_value):
        # Constructor que recibe los valores min y max para el cálculo del factorial
        self.min_value = min_value
        self.max_value = max_value

    def calcular_factorial(self, n):
        # Método para calcular el factorial de un número 'n'
        return math.factorial(n)

    def run(self):
        # Método que ejecuta el cálculo de los factoriales en el rango [min_value, max_value]
        if self.min_value > self.max_value:
            print("El valor de 'min' debe ser menor o igual a 'max'.")
            return
        
        for num in range(self.min_value, self.max_value + 1):
            print(f"El factorial de {num} es: {self.calcular_factorial(num)}")

# Solicitar al usuario el rango o recibirlo como argumento
if __name__ == "__main__":
    min_value = int(input("Ingrese el valor mínimo: "))
    max_value = int(input("Ingrese el valor máximo: "))
    
    # Crear una instancia de la clase Factorial con los valores ingresados
    factorial_obj = Factorial(min_value, max_value)
    
    # Ejecutar el método run para calcular los factoriales en el rango especificado
    factorial_obj.run()
