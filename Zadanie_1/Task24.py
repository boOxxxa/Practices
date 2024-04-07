import math


def trapez(func, a, b, N):
    h = (b - a) / N
    result = 0.5 * (func(a) + func(b))
    for i in range(1, N):
        result += func(a + i * h)
    result *= h
    return round(result, 8)


a = 5
b = 7
N = 100
integral = trapez(math.sin, a, b, N)
print(integral)