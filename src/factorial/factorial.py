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
    return math.factorial(n)  # Devuelve el factorial de 'n' utilizando la función 'factorial' del módulo math

# Función para manejar los diferentes tipos de rangos
def calcular_factoriales(rango):
    if '-' in rango:  # Verifica si el rango contiene un guion, lo que indica un rango
        # Verificar si el rango es del tipo "hasta" o "desde"
        if rango.startswith('-'):  # Rango de la forma "-10" (hasta)
            fin = int(rango[1:])  # Eliminar el "-" y convertir el valor restante a entero
            inicio = 1  # Establecer el inicio del rango en 1
            if fin < inicio:  # Verificar que 'fin' no sea menor que 'inicio'
                print("El valor de 'hasta' debe ser mayor o igual a 1.")
                return
            # Imprimir el factorial de cada número desde 1 hasta 'fin'
            for num in range(inicio, fin + 1):
                print(f"El factorial de {num} es: {calcular_factorial(num)}")
        elif rango.endswith('-'):  # Rango de la forma "20-" (desde)
            inicio = int(rango[:-1])  # Eliminar el "-" y convertir el valor restante a entero
            fin = 60  # Establecer el fin del rango en 60
            if inicio > fin:  # Verificar que 'inicio' no sea mayor que 'fin'
                print("El valor de 'desde' debe ser menor o igual a 60.")
                return
            # Imprimir el factorial de cada número desde 'inicio' hasta 60
            for num in range(inicio, fin + 1):
                print(f"El factorial de {num} es: {calcular_factorial(num)}")
        else:
            # Si el formato no es válido, imprime un mensaje de error
            print("Formato de rango incorrecto. Use '-hasta' o 'desde-'.")
    else:
        # Si el rango es completo, de "inicio-hasta", por ejemplo "4-8"
        inicio, fin = map(int, rango.split('-'))  # Separa el rango en 'inicio' y 'fin' y los convierte a enteros
        if inicio > fin:  # Verifica que 'inicio' no sea mayor que 'fin'
            print("El valor de 'inicio' debe ser menor o igual a 'fin'.")
            return
        # Imprimir el factorial de cada número desde 'inicio' hasta 'fin'
        for num in range(inicio, fin + 1):
            print(f"El factorial de {num} es: {calcular_factorial(num)}")

# Verificar si se proporcionó el rango como argumento en la línea de comandos
if len(sys.argv) > 1:
    rango = sys.argv[1]  # Si hay un argumento, lo usa como rango
else:
    # Si no hay argumentos, solicita al usuario que ingrese el rango manualmente
    rango = input("Por favor, ingrese el rango (ej. 4-8, -10, 20-): ")

# Llamamos a la función para calcular los factoriales
calcular_factoriales(rango)
