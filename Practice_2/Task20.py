from scipy.optimize import minimize
def f(xy, a, b):
    x, y = xy
    return (x + y)**2 - 2*x*(y + a) - 2*y*b + a + b
a = int(input("A "))
b = int(input("B "))
xy0 = [0, 0]
result = minimize(f, xy0, args=(a, b))
x_min, y_min = result.x
print("Координата локального минимума (x, y):", (round(x_min, 2), round(y_min, 2)))
