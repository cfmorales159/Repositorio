import numpy as np
delta_x_inicial = 150
error_deseado = 0.01
# Apicamos la formula
n=np.log2(delta_x_inicial/error_deseado)
print(f"En número de Iteraciones Necesarias es: {np.ceil(n)}") # ceil redondea n hacia arriba
nb10=np.log10(delta_x_inicial/error_deseado)/np.log10(2)
print(f"Resultado A: {n}")
print(f"Resultado B: {nb10}")   # vamos a observar un pequeño error de redondeo