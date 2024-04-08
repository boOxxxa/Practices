
from scipy.optimize import minimize
import numpy as np
def f(x):
    return -(x**2 * (x - 4)**2 * np.exp(-x**2))
x0 = float(input("Введите число "))
result = minimize(f, x0=x0, method='Nelder-Mead')
x_max = round(result.x[0], 2)
print("Координата локального максимума:", x_max)