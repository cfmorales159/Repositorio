import numpy as np
# OBSERVAR SE TIENEN DOS EJEMPLOS DE FUNCIONES, CONVERGE OTRA DIVERGE
#def f(x):
    # Función del ejemplo del Chapra: f(x) = e^(-x) - x
   # return np.exp(-x) - x

def f(x):
    # Función del ejemplo del Chapra: f(x) = e^(-x) - x
    return x**2-2*x+4

#def df(x):
    # DERIVADA: Aquí el alumno debe aplicar lo visto en clase
    # f'(x) = -e^(-x) - 1
   # return -np.exp(-x) - 1
def df(x):
    # DERIVADA: Aquí el alumno debe aplicar lo visto en clase
    #
    return 2*x-2

def newton_raphson(x0, tol, max_iter):
    print(f"{'Iter':<10} {'xi':<15} {'error (%)':<15}")
    print("-" * 40)
    
    xi = x0
    for i in range(max_iter): # esta sentencia pone freno a posible bucle
        # --- PARTE A COMPLETAR POR EL ALUMNO ---
        # Aplicar la fórmula: x_i+1 = x_i - f(x_i) / f'(x_i)
        
        derivada = df(xi)
        
        if derivada == 0:
            print("Error: Derivada nula. El método no puede continuar.")
            break
            
        xi_nuevo = xi - (f(xi) / derivada)
        # ---------------------------------------
  
        
        # Cálculo del error relativo aproximado (Chapra Eq. 3.5)
        ea = abs((xi_nuevo - xi) / xi_nuevo) * 100
        
        print(f"{i+1:<10} {xi_nuevo:<15.6f} {ea:<15.6f}")
        
        if ea < tol:
            print(f"\nConvergencia alcanzada en la iteración {i+1}")
            return xi_nuevo
        
        xi = xi_nuevo
        
    print("\nSe alcanzó el máximo de iteraciones sin converger.")
    return xi

# Parámetros iniciales
x_inicial = 0 # se elije adivinando por donde podría estar la raíz
tolerancia = 0.0001 # 0.0001%
iteraciones = 10

raiz = newton_raphson(x_inicial, tolerancia, iteraciones)
print(f"La raíz aproximada es: {raiz}")


 # Verificamos que xi_nuevo no sea cero antes de dividir
""" if xi_nuevo != 0:
    ea = abs((xi_nuevo - xi) / xi_nuevo) * 100
else:
    ea = 100  """# O un valor por defecto si cae en cero 
# Descomentar shift+alt+a

