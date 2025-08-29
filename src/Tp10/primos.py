#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

# Establecemos el límite inferior 1 superior 500 para la busqueda de numeros primos
lower = 1
upper = 500

# Imprimimos el mensaje inicial indicando el rango en el que buscaremos números primos
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1: # Verificamos si el número es mayor que 1
       for i in range(2, num):
           if (num % i) == 0:
               break # Si encontramos un divisor, terminamos el bucle 'for'
       else:   # Si no encontramos ningún divisor, el número es primo
           print(num)
