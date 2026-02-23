import math
def f(x):
    return: -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2
# 2. Parámetros del problema
x = 0.5
h = 0.5
valor_real = -0.9125  # Valor exacto de la derivada f'(0.5)
# 3. Fórmulas de Diferencias Finitas
df_forward  = (f(x + h) - f(x)) / h
df_backward = (f(x) - f(x - h)) / h
df_centered = (f(x + h) - f(x - h)) / (2 * h)
# 4. Cálculo de errores relativos porcentuales
def error(aprox):
    return abs((valor_real - aprox) / valor_real) * 100
print(f"--- Resultados para h = {h} ---")
print(f"Forward (Adelante):  {df_forward:.4f}  | Error: {error(df_forward):.2f}%")
print(f"Backward (Atrás):   {df_backward:.4f} | Error: {error(df_backward):.2f}%")
print(f"Centered (Centrada): {df_centered:.4f}  | Error: {error(df_centered):.2f}%")