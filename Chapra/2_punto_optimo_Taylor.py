import math

def f(x):
    return math.exp(x)

x = 1.0
valor_real = math.exp(1) # La derivada de e^x es e^x, evaluada en 1 es e

print(f"{'log10(h)':>10} | {'Paso h':>15} | {'Error Total %':>20}")
print("-" * 50)

# Vamos a probar desde h = 1 (10^0) hasta h = 10^-16
for i in range(0, 17):
    h = 10**(-i)
    
    # Usamos Diferencia Centrada (la "mejor" que vimos)
    derivada_aprox = (f(x + h) - f(x - h)) / (2 * h)
    
    error = abs((valor_real - derivada_aprox) / valor_real) * 100
    
    print(f"{-i:>10} | {h:>15.1e} | {error:>20.15f}%")