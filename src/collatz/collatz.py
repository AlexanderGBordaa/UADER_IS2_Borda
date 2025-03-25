# Función para calcular el número de Collatz y el número de iteraciones
def collatz_iterations(n):
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations

# Mostrar los números y sus iteraciones en la terminal
for n in range(1, 10001):
    iterations = collatz_iterations(n)
    print(f'Número: {n}, Iteraciones: {iterations}')
