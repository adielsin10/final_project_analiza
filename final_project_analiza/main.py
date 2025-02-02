import numpy as np
import Jacobi
import LUfactorization
import bisection_method
import newtonRapson
import lagrange_interpolation
import neville_method_polinom
import bis_p
import neuton
import nevile
import lagrane
import Simpson_method
import trapezoidal_rule

import matplotlib.pyplot as plt


def f1(l):
    return 4.86+0.018*l
def f2(l):
    return l/3000
def f3(l):
    if l <= 0:
       return 0
    return l * (0.0012 + 0.0001 * np.log(l) + 0.000043 * (np.log(l))**2)

def f4(l):
    return 4.2+0.0015*l**(4/3)
def f5(l):
    return 0.069+0.00156*l+0.00000047*l**2

h1=[]
h2=[]
h3=[]
h4=[]
h5=[]


#17 שאלה
x_bisection_m=int(bisection_method.result())
x_nuton=newtonRapson.result()
h1.append((f1(x_bisection_m*500),x_bisection_m*500))
h2.append((f2(600),x_bisection_m*500))
h3.append((f3(x_bisection_m*500),x_bisection_m*500))
h4.append((f4(x_bisection_m*500),x_bisection_m*500))
h5.append((f5(x_bisection_m*500),x_bisection_m*500))
#34 שאלה
y_larange=int(lagrange_interpolation.result())
y_nevile=neville_method_polinom.result()

h1.append((f1(y_larange*700),y_larange*700))
h2.append((f2(y_larange*700),y_larange*700))
h3.append((f3(y_larange*700),y_larange*700))
h4.append((f4(y_larange*700),y_larange*700))
h5.append((f5(y_larange*700),y_larange*700))
#15 שאלה
x_bis=abs(int(bis_p.result()))
x_neuton=neuton.result()
h1.append((f1(80*x_bis),x_bis*80))
h2.append((f2(80*x_bis),x_bis*80))
h3.append((f3(80*x_bis),x_bis*80))
h4.append((f4(80*x_bis),x_bis*80))
h5.append((f5(80*x_bis),x_bis*8))
#33
y_nevi=abs(int(nevile.result()))
y_larg=abs(int(lagrane.result()))

h1.append((f1(400*y_larg),y_larg*400))
h2.append((f2(400*y_larg),y_larg*400))
h3.append((f3(400*y_larg),y_larg*400))
h4.append((f4(400*y_larg),y_larg*400))
h5.append((f5(400*y_larg),y_larg*400))
#14
x_simpon=abs(int(Simpson_method.result()))
x_trapez=trapezoidal_rule.resuult()

h1.append((f1(400*x_simpon),400*x_simpon))
h2.append((f2(400*x_simpon),400*x_simpon))
h3.append((f3(400*x_simpon),400*x_simpon))
h4.append((f4(400*x_simpon),400*x_simpon))
h5.append((f5(400*x_simpon),400*x_simpon))
#28
x_mat_a=abs(int(LUfactorization.result()))
x_jaco=Jacobi.result()

h1.append((f1(x_mat_a*370),x_mat_a*370))
h2.append((f2(x_mat_a*370),x_mat_a*370))
h3.append((f3(x_mat_a*370),x_mat_a*370))
h4.append((f4(x_mat_a*370),x_mat_a*370))
h5.append((f5(x_mat_a*370),x_mat_a*370))



# Extract X and Y values for each function
x_values1 = [x for x, _ in h1]
x_values2 = [x for x, _ in h2]
x_values3 = [x for x, _ in h3]
x_values4 = [x for x, _ in h4]
x_values5 = [x for x, _ in h5]
y_values_h1 = [y for _, y in h1]
y_values_h2 = [y for _, y in h2]
y_values_h3 = [y for _, y in h3]
y_values_h4 = [y for _, y in h4]
y_values_h5 = [y for _, y in h5]

# Plot all functions on the same graph
plt.figure(figsize=(10, 6))
plt.plot(x_values1, y_values_h1, marker='o', linestyle='-', label='h1')
plt.plot(x_values2, y_values_h2, marker='s', linestyle='-', label='h2')
plt.plot(x_values3, y_values_h3, marker='^', linestyle='-', label='h3')
plt.plot(x_values4, y_values_h4, marker='d', linestyle='-', label='h4')
plt.plot(x_values5, y_values_h5, marker='x', linestyle='-', label='h5')

# Labels and title
plt.xlabel('X values (Left element of h)')
plt.ylabel('Y values (Right element of h)')
plt.title('Plot of h1, h2, h3, h4, h5 functions')
plt.legend()
plt.grid(True)

print(h1)
print(h2)
print(h3)
print(h4)
print(h5)
# Show the plot
plt.show()









