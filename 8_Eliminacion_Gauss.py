import numpy as np

# =====================================================================
# BLOQUE 1: LA PRIMERA FUNCIÓN (Solo se encarga de triangular)
# =====================================================================
def eliminacion_adelante(A, B):
    # Unimos la matriz A y el vector B en la matriz aumentada
    M = np.hstack([A, np.atleast_2d(B).T]).astype(float)
    n = len(B)
    
    # Los 3 bucles anidados del Chapra para hacer ceros abajo de la diagonal
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = M[i, k] / M[k, k]
            for j in range(k, n + 1):
                M[i, j] = M[i, j] - factor * M[k, j]
                
    return M # Devuelve la matriz ya escalonada (triangular superior)


# =====================================================================
# BLOQUE 2: LA SEGUNDA FUNCIÓN (Solo se encarga del efecto dominó)
# =====================================================================
def sustitucion_atras(M_triangular):
    n = M_triangular.shape[0]
    x = np.zeros(n) # Array vacío para guardar las respuestas [x0, x1, x2...]
    
    # Despejamos la última incógnita (la base del dominó)
    x[n-1] = M_triangular[n-1, n] / M_triangular[n-1, n-1]
    
    # Bucle que va en reversa hacia arriba despejando las demás
    for i in range(n - 2, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += M_triangular[i, j] * x[j]
        
        x[i] = (M_triangular[i, n] - suma) / M_triangular[i, i]
        
    return x # Devuelve el vector con las soluciones finales


# =====================================================================
# BLOQUE 3: EL PROGRAMA PRINCIPAL (El flujo que une a las funciones)
# =====================================================================
# 1. Definimos el problema matemático en papel
A = np.array([[3, 2, -1],
              [2, -2, 4],
              [-1, 0.5, -1]])

B = np.array([1, -2, 0])

print("--- Ejecutando el sistema ---")

# 2. LLAMAMOS A LA PRIMERA FUNCIÓN: Dejamos la matriz en forma de escalera
matriz_escalonada = eliminacion_adelante(A, B)

# 3. LLAMAMOS A LA SEGUNDA FUNCIÓN: Pasamos la escalera para obtener los valores de X
resultado_final = sustitucion_atras(matriz_escalonada)

# 4. Mostramos la solución en la terminal
print("Las soluciones del sistema son:")
print(f"x0 = {resultado_final[0]:.4f}")
print(f"x1 = {resultado_final[1]:.4f}")
print(f"x2 = {resultado_final[2]:.4f}")