"""
Implementación de la conjetura de Collatz.
Solicita un entero positivo (<=1999), valida y devuelve el número de iteraciones
necesarias para alcanzar 1.
"""

def collatz_iter_count(num: int) -> int:
    """Devuelve la cantidad de iteraciones necesarias para que num alcance 1
    aplicando la regla de Collatz.
    Precondición: num es entero positivo (>=1)."""
    iteraciones = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        iteraciones += 1
    return iteraciones

def pedir_entero(maximo=1999) -> int:
    """Lee por consola un entero positivo <= maximo. Lanza ValueError si no válido."""
    entrada = input("Ingrese un entero positivo (max {}): ".format(maximo)).strip()
    if entrada == "":
        raise ValueError("Entrada vacía")
    try:
        n = int(entrada)
    except ValueError:
        raise ValueError("La entrada no es un entero válido")
    if n <= 0:
        raise ValueError("El entero debe ser positivo")
    if n > maximo:
        raise ValueError("El entero supera el máximo permitido ({})".format(maximo))
    return n

def main():
    try:
        n = pedir_entero()
    except ValueError as e:
        print("ERROR:", e)
        return 1
    iter_count = collatz_iter_count(n)
    print("Número de partida: {}".format(n))
    print("Cantidad de iteraciones necesarias para llegar a 1: {}".format(iter_count))
    return 0

if __name__ == "__main__":
    import sys
    exit_code = main()
    sys.exit(exit_code)
    
