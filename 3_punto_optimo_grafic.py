import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x)

x_val = 1.0
valor_real = np.exp(1.0)

# Generamos un rango de exponentes desde 0 hasta -16
exponentes = np.arange(0, -17, -1)
pasos_h = 10.0**exponentes

errores = []

for h in pasos_h:
    # Diferencia centrada
    derivada_aprox = (f(x_val + h) - f(x_val - h)) / (2 * h)
    error_relativo = abs((valor_real - derivada_aprox) / valor_real)
    errores.append(error_relativo)

# Graficamos en escala log-log
plt.figure(figsize=(10, 6))
plt.loglog(pasos_h, errores, 'o-', label='Error Total')

# Etiquetas para entender la gráfica
plt.xlabel('Tamaño del paso (h)')
plt.ylabel('Error Relativo Absoluto')
plt.title('El Dilema del Error Numérico (Chapra Fig. 4.11)')
plt.gca().invert_xaxis() # Invertimos para ver h achicándose de izquierda a derecha
plt.grid(True, which="both", ls="-", alpha=0.5)

# Anotaciones
plt.annotate('Dominio del Truncamiento', xy=(10**-2, 10**-5), xytext=(10**-1, 10**-3),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Dominio del Redondeo', xy=(10**-14, 10**-5), xytext=(10**-12, 10**-2),
             arrowprops=dict(facecolor='red', shrink=0.05))

plt.legend()
plt.show()