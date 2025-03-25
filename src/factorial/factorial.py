#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
import math

# Función para calcular el factorial de un número
def calcular_factorial(n):
    return math.factorial(n)

# Función para manejar el rango de números
def calcular_factoriales_desde_hasta(rango):
    inicio, fin = map(int, rango.split('-'))
    if inicio > fin:
        print("El valor de 'inicio' debe ser menor o igual a 'fin'.")
        return
    for num in range(inicio, fin + 1):
        print(f"El factorial de {num} es: {calcular_factorial(num)}")

# Verificar si se proporcionó el rango como argumento
if len(sys.argv) > 1:
    rango = sys.argv[1]
else:
    rango = input("Por favor, ingrese el rango (ej. 4-8): ")

# Llamamos a la función para calcular los factoriales
calcular_factoriales_desde_hasta(rango)
