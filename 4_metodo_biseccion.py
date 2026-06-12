import math

def biseccion(func, xl, xu, es=0.01, max_iter=100):
    """
    func: la función a evaluar
    xl, xu: límites inferior y superior del intervalo
    es: error relativo deseado (tolerancia en %)
    max_iter: límite de seguridad para no entrar en bucle infinito
    """
    # Verificación inicial: ¿Hay cambio de signo?
    if func(xl) * func(xu) > 0:
        return None, "Error: No hay cambio de signo en el intervalo."

    xr = xl  # Inicializamos la raíz estimada
    iteracion = 0
    ea = 100 # Error aproximado inicial (100%)

    print(f"{'Iter':<5} | {'Raíz (xr)':<12} | {'Error (ea) %':<12}")
    print("-" * 35)

    while True:
        xr_viejo = xr  # Guardamos el valor anterior para calcular el error
        xr = (xl + xu) / 2 # Nuevo punto medio
        iteracion += 1

        # Calculamos el error relativo aproximado (si no es la primera iteración)
        if xr != 0:
            ea = abs((xr - xr_viejo) / xr) * 100

        print(f"{iteracion:<5} | {xr:<12.6f} | {ea:<12.4f}")

        # --- CRITERIO DE PARADA ---
        if ea < es or iteracion >= max_iter:
            break

        # Decidimos qué mitad del intervalo conservar
        test = func(xl) * func(xr)
        if test < 0:
            xu = xr  # La raíz está en la mitad izquierda
        elif test > 0:
            xl = xr  # La raíz está en la mitad derecha
        else:
            ea = 0   # Encontramos la raíz exacta (suerte loca)

    return xr, ea

# --- PRUEBA CON EL POLINOMIO ---
f = lambda x: -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

# Supongamos que incsearch nos dijo que hay una raíz entre 0 y 2
raiz, error_final = biseccion(f, 0, 2, es=0.05)

print("-" * 35)
print(f"Resultado final: {raiz:.6f} con un error de {error_final:.4f}%")