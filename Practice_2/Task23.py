import numpy as np
from scipy.fft import fft

def f(t, v):
    return np.sin(v * np.cos(2 * np.pi * t))

def spectral_weight(v):
    # Шаг дискретизации времени
    dt = 0.01
    # Создание временной сетки
    t = np.arange(0, 1, dt)
    # Вычисление значения функции на временной сетке
    y = f(t, v)
    # Выполнение преобразования Фурье
    Y = fft(y)
    # Вычисление спектрального веса
    weight = np.max(np.abs(Y))
    return weight

# Заданный параметр v
v = 6

# Вычисление спектрального веса для заданного v
max_weight = spectral_weight(v)

print("Максимальный спектральный вес для v =", v, ":", round(max_weight, 2))
