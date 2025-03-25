#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    # Verifica si se pasó un argumento
    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
            print(f"El factorial de {num} es: {factorial(num)}")
        except ValueError:
            print("Por favor ingrese un número válido.")
    else:
        num = int(input("Ingrese un número: "))
        print(f"El factorial de {num} es: {factorial(num)}")
