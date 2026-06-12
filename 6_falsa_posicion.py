def falsa_posicion(func, xl, xu, es=0.01, max_iter=100):
    if func(xl) * func(xu) > 0:
        return None, "Error: No hay cambio de signo."
# es= error esperado, Error Specification, Stopping Criterion
    xr = xl
    iteracion = 0
    ea = 100

    print(f"{'Iter':<5} | {'Raíz (xr)':<12} | {'f(xr)':<12} | {'Error (ea) %':<12}")
    print("-" * 55)

    while True:
        xr_viejo = xr
        
        # --- ESTA ES LA ÚNICA LÍNEA QUE CAMBIA RESPECTO A BISECCIÓN ---
        # Aplicamos la fórmula de la línea recta (interpolación lineal)
        fl = func(xl)
        fu = func(xu)
        xr= xu - (fu*(xl-xu))/(fl-fu)# xr=(fu*xl-fl*xu) / (fu - fl) 
        # --------------------------------------------------------------

        iteracion += 1
        f_xr = func(xr)

        if xr != 0:
            ea = abs((xr - xr_viejo) / xr) * 100

        print(f"{iteracion:<5} | {xr:<12.6f} | {f_xr:<12.6e} | {ea:<12.4f}")

        if ea < es or iteracion >= max_iter:
            break

        # La lógica de decisión de intervalos sigue siendo la misma (Bolzano)
        if fl * f_xr < 0:
            xu = xr
        else:
            xl = xr

    return xr, ea

# Probamos con el mismo polinomio del Chapra
f = lambda x: -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2
raiz, error = falsa_posicion(f, 0, 2, es=0.01) # al no especificar max_iter utiliza max_iter=100