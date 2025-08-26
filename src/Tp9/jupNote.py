# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones
def esfuerzo(S):
    return 8 * (S**0.95)

def tiempo(E):
    return 2.4 * (E**0.33)

# 1) Gráfico de Esfuerzo E vs Tamaño S
S_vals = np.linspace(0, 10000, 500)  # 500 puntos entre 0 y 10000
E_vals = esfuerzo(S_vals)

plt.figure(figsize=(8,5))
plt.plot(S_vals, E_vals, label="E = 8·S^0.95", color="blue")
plt.title("Esfuerzo vs Tamaño del Proyecto")
plt.xlabel("Tamaño del Proyecto (S)")
plt.ylabel("Esfuerzo (E)")
plt.grid(True)
plt.legend()
plt.show()

# 2) Gráfico de Tiempo τd vs Esfuerzo E
E_vals2 = np.linspace(1, 500, 500)  # Esfuerzo entre 1 y 500
td_vals = tiempo(E_vals2)

plt.figure(figsize=(8,5))
plt.plot(E_vals2, td_vals, label="τd = 2.4·E^0.33", color="green")
plt.title("Tiempo de Calendario vs Esfuerzo")
plt.xlabel("Esfuerzo (E)")
plt.ylabel("Tiempo de Calendario (τd)")
plt.grid(True)
plt.legend()
plt.show()
