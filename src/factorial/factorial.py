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

# Función para manejar los diferentes tipos de rangos
def calcular_factoriales(rango):
    if '-' in rango:
        # Verificar si el rango es del tipo "hasta" o "desde"
        if rango.startswith('-'):  # Rango de la forma "-10"
            fin = int(rango[1:])  # Eliminar el "-" y convertir a entero
            inicio = 1  # Establecer el inicio a 1
            if fin < inicio:
                print("El valor de 'hasta' debe ser mayor o igual a 1.")
                return
            for num in range(inicio, fin + 1):
                print(f"El factorial de {num} es: {calcular_factorial(num)}")
        elif rango.endswith('-'):  # Rango de la forma "20-"
            inicio = int(rango[:-1])  # Eliminar el "-" y convertir a entero
            fin = 60  # Establecer el fin a 60
            if inicio > fin:
                print("El valor de 'desde' debe ser menor o igual a 60.")
                return
            for num in range(inicio, fin + 1):
                print(f"El factorial de {num} es: {calcular_factorial(num)}")
        else:
            print("Formato de rango incorrecto. Use '-hasta' o 'desde-'.")
    else:
        # Si el rango es completo, de "inicio-hasta"
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
    rango = input("Por favor, ingrese el rango (ej. 4-8, -10, 20-): ")

# Llamamos a la función para calcular los factoriales
calcular_factoriales(rango)
