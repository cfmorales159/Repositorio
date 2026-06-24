def error(measured, real):
    return abs((measured - real) / measured) * 100.0

def bisection(f, xl, xu, es = 0.05, i_max = 20):
    data = []
    i = 0
    xr = xl
    ea = 100.0
    while (i < i_max) and (es < ea):
        xr_prev = xr
        xr = (xl+xu)/2
        if xr != 0:
            ea = error(xr, xr_prev)
        fxl = f(xl)
        fxr = f(xr)
        if (fxl*fxr > 0):
            xl = xr
        else:
            xu = xr
        i += 1
        data.append((i,xr,ea))
    return data

def fake_position(f, xl, xu, es = 0.05, i_max = 20):
    data = []
    i = 0
    xr = xl
    ea = 100.0
    while (i < i_max) and (es < ea):
        xr_prev = xr
        xr = xu - (f(xu)*(xl - xu)/(f(xl)-f(xu)))
        if xr != 0:
            ea = error(xr, xr_prev)
        if (f(xl)*f(xr) > 0):
            xl = xr
        else:
            xu = xr
        i += 1
        data.append((i,xr,ea))
    return data

def newton_raphson(f, df, x1, es = 0.05, i_max = 20):
    data = []
    i = 0
    xr = x1
    ea = 100.0
    while (i < i_max) and (es < ea):
        dx1 = df(x1)
        if(dx1 == 0):
            print("Error: Derivada nula.")
        xr_prev = xr
        xr = xr - (f(xr) / dx1)
        if xr != 0:
            ea = error(xr, xr_prev)
        i += 1
        data.append((i,xr,ea))
    return data