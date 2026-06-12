#!/usr/bin/env python3
import math

def f(x):
    """Función: e^-x - x^2"""
    return math.exp(-x) - x**2

def biseccion(a, b, tol_porcentual, max_iter=50):
    # Verificación del Teorema del Valor Intermedio
    if f(a) * f(b) >= 0:
        print("Error: La función no cambia de signo en el intervalo dado.")
        print("Bisección no puede garantizar una raíz en este rango.")
        return None

    print(f"--- Iniciando Bisección ---")
    print(f"Intervalo: [{a}, {b}] | Tolerancia: {tol_porcentual}%\n")
    
    x_old = 0
    
    for i in range(1, max_iter + 1):
        # 1. Cálculo del punto medio
        x_r = (a + b) / 2
        
        # 2. Cálculo del Error Relativo Porcentual (ea)
        # Solo se calcula a partir de la segunda iteración
        if i > 1:
            error_relativo = abs((x_r - x_old) / x_r) * 100
        else:
            error_relativo = 100.0 # Valor inicial
            
        print(f"Iteración {i:02d}: x = {x_r:.10f} | Error = {error_relativo:.2e}%")
        
        # 3. Criterio de parada
        if error_relativo < tol_porcentual:
            print(f"\n Convergencia del Método de Biseccion")
            print(f"La raíz aproximada es: {x_r:.10f} Cantidad de Iteraciones {i:.1f}")
            return x_r
        
        # 4. Decidir qué mitad del intervalo conservar
        if f(a) * f(x_r) < 0:
            b = x_r
        else:
            a = x_r
            
        x_old = x_r
        
    print("\nSe alcanzó el máximo de iteraciones.")
    return x_r

# --- EJECUCIÓN ---
if __name__ == "__main__":
    # Buscamos en el intervalo [0, 1] con tolerancia del 0.0001%
    raiz = biseccion(a=0, b=1, tol_porcentual=1e-4)

# NEWTON RAPSHON

def df(x):
    """Derivada de la función: -e^-x - 2x"""
    return -math.exp(-x) - 2*x

def newton_raphson(x0, tol_porcentual, max_iter=50):
    print(f"--- Iniciando Newton-Raphson ---")
    print(f"Punto inicial: {x0} | Tolerancia: {tol_porcentual}%\n")
    
    x_i = x0
    
    for i in range(1, max_iter + 1):
        f_val = f(x_i)
        df_val = df(x_i)
        
        # 1. Validación de seguridad (evitar división por cero)
        if abs(df_val) < 1e-12:
            print(f"ERROR: Derivada nula en x = {x_i}. El método diverge.")
            return None
        
        # 2. Aplicación del Polinomio de Taylor grado 1 (Despeje de xi+1)
        x_next = x_i - f_val / df_val
        
        # 3. Cálculo del Error Relativo Porcentual
        # Usamos abs(x_next) en el denominador para evitar errores de signo
        if x_next != 0:
            error_relativo = abs((x_next - x_i) / x_next) * 100
        else:
            error_relativo = 100.0  # Valor inicial por defecto si pasa por el origen
            
        # 4. Mostrar progreso con formato preciso
        print(f"Iteración {i:02d}: x = {x_next:.10f} | Error = {error_relativo:.2e}%")
        
        # 5. Criterio de parada
        if error_relativo < tol_porcentual:
            print(f"\nConvergencia de Newton-Rapshon")
            print(f"La raíz aproximada es: {x_next:.10f} Cantidad de Iteraciones {i:.1f}")
            return x_next
            
        x_i = x_next
        
    print("\nSe alcanzó el máximo de iteraciones sin converger.")
    return x_i

# --- EJECUCIÓN ---
if __name__ == "__main__":
    # Parámetros: Punto inicial x0 = 0, Tolerancia = 0.0001%
    raiz = newton_raphson(x0=0, tol_porcentual=1e-4)