import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# -----------------------------
# Modelo PNR
# -----------------------------
def E(t, K, a):
    """Esfuerzo instantáneo"""
    return 2 * K * a * t * np.exp(-a * t**2)

def E_acum(t, K, a):
    """Esfuerzo acumulado"""
    return K * (1 - np.exp(-a * t**2))

# -----------------------------
# Dataset histórico
# -----------------------------
t_data = np.array([1,2,3,4,5,6,7,8,9,10])  # meses
E_data = np.array([8,21,25,30,25,24,17,15,11,6])  # PM instantáneo

K_hist = np.sum(E_data)

# Ajuste de a
popt, _ = curve_fit(lambda t, a: E(t, K_hist, a), t_data, E_data, p0=[0.1])
a_calibrado = popt[0]

print(f"Esfuerzo histórico total K={K_hist:.1f} PM")
print(f"Parámetro a calibrado={a_calibrado:.4f}")

# -----------------------------
# (a) Función que recibe K en PM
# -----------------------------
def graficar_modelo(K_proyecto, a_valor=None, titulo="Proyecto"):
    if a_valor is None:
        a_valor = a_calibrado
    t_vals = np.linspace(0,12,200)
    E_vals = E(t_vals, K_proyecto, a_valor)

    # Graficar
    plt.scatter(t_data, E_data, label="Datos históricos", color="black")
    plt.plot(t_vals, E(t_vals, K_hist, a_calibrado), "r--", label="Modelo calibrado (histórico)")
    plt.plot(t_vals, E_vals, "g-", label=f"Proyecto K={K_proyecto} PM")
    plt.title(titulo)
    plt.xlabel("Tiempo (meses)")
    plt.ylabel("Esfuerzo instantáneo (PM/mes)")
    plt.legend()
    plt.grid(True)
    plt.show()

# -----------------------------
# (b) Proyecto de 72 PM
# -----------------------------
graficar_modelo(72, titulo="Proyecto de 72 PM")

# Comentario esperado:
print("\nEl modelo suavizado para 72 PM muestra una curva en forma de campana, más regular que los puntos históricos, que tienen variaciones y picos. El ajuste refleja una tendencia promedio mientras que los datos observados presentan irregularidades propias de la realidad.")

# -----------------------------
# (c) Proyecto con a cuadruplicado
# -----------------------------
graficar_modelo(72, a_valor=4*a_calibrado, titulo="Proyecto de 72 PM con a x4")

# Comentario esperado:
print("\nCon a cuadruplicado la curva se concentra en un tiempo más corto y con un pico mucho mayor. Esto representa la 'Zona imposible': el modelo asume una productividad irreal concentrada en poco tiempo, lo que en la práctica implicaría sobrecarga y riesgo de fracaso del proyecto.")
