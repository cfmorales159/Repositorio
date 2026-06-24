from formulas import bisection, fake_position, newton_raphson
from utils import print_table, plot, show_plots

# Variables de entrada

es = 0.05
i_max = 5

x_l = 0.0
x_u = 1.0
x_i = 0.0

f = lambda x: 4*x*x*x*x - 9*x*x + 14*x + 1
df = lambda x: 16*x - 18*x + 14

# Variables auxiliares

f_xi = f(x_i)
df_xi = df(x_i)
df_tan = lambda x: x*df_xi
df_tan_offset = lambda x: df_tan(x) - df_tan(x_i) + f_xi

x_l_point = (x_l, 0.0, "x_l")
x_u_point = (x_u, 0.0, "x_u")
x_i_point = (x_i, 0.0, "x_i")
f_xi_point = (x_i, f_xi, "f(x_i)")

# Opciones de gráfica

plot_samples = 500
plot_range = (x_l-1,x_u+1)

# data_bisection = bisection(f, x_l, x_u, es, i_max)
data_fake_position = fake_position(f, x_l, x_u, es, i_max)
# data_newton_raphson = newton_raphson(f, df, x_i, es, i_max)

# print("Metodo de bisección")
# print_table(data_bisection)
print("Metodo de falsa posición")
print_table(data_fake_position)
# print("Metodo de Newton-Raphson")
# print_table(data_newton_raphson)

# plot([f], [x_l_point,x_u_point],data_bisection,plot_range,plot_samples, "Metodo de bisección")
plot([f], [x_l_point,x_u_point],data_fake_position,plot_range,plot_samples, "Metodo de falsa posición")
# plot([f,df_tan_offset], [x_i_point, f_xi_point],data_newton_raphson,plot_range,plot_samples, "Metodo de Newton-Raphson")

show_plots()