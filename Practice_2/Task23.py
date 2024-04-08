# import numpy as np
# from scipy.optimize import minimize_scalar
#
# # Определение функции f(t)
# def f(t, v):
#     return np.sin(v * np.cos(2 * np.pi * t))
#
# # Функция для вычисления спектрального веса для заданной частоты
# def spectral_weight(freq, v):
#     t = np.linspace(0, 1, 1000)  # временная ось
#     signal = f(t, v)
#     spectrum = np.abs(np.fft.fft(signal))
#     return spectrum[int(freq)]
#
# # Функция для нахождения частоты с максимальным спектральным весом
# def find_max_spectrum_freq(v):
#     # Минимизация отрицательного спектрального веса, чтобы найти максимальный
#     result = minimize_scalar(lambda freq: -spectral_weight(freq, v), bounds=(0, 10), method='bounded')
#     return result.x
#
# # Ввод значения v с клавиатуры
# v = float(input("Введите значение v: "))
#
# # Поиск частоты с максимальным спектральным весом
# max_freq = find_max_spectrum_freq(v)
# print("Неотрицательная частота с максимальным спектральным весом:", max_freq)
# for i in range(1,100):
#     if(find_max_spectrum_freq(i)<6):
#         print("Максимальный спектральный вес для v =", i, ":", round(find_max_spectrum_freq(i), 2))
#     #print("Максимальный спектральный вес для v =", i, ":", round(spectral_weight(i), 2))
# print("Максимальный спектральный вес для v =", v, ":", round(max_freq, 2))
import numpy as np

# Определение функции f(t)
def f(t, v):
    return np.sin(v * np.cos(2 * np.pi * t))

# Функция для вычисления спектрального веса для заданной частоты
def spectral_weight(freq, v):
    t = np.linspace(0, 10, 100)  # временная ось
    signal = f(t, v)
    spectrum = np.abs(np.fft.fft(signal))
    freq_index = int(freq * len(t))
    return spectrum[freq_index]

# Функция для нахождения частоты с максимальным спектральным весом
def find_max_spectrum_freq(v):
    t = np.linspace(0, 100,100)  # временная ось
    freqs = np.fft.fftfreq(len(t))
    signal = f(t, v)
    spectrum = np.abs(np.fft.fft(signal))
    max_freq_index = np.argmax(spectrum)
    max_freq = freqs[max_freq_index]
    return max_freq

# Ввод значения v с клавиатуры
v = float(input("Введите значение v: "))

# Поиск частоты с максимальным спектральным весом
max_freq = find_max_spectrum_freq(v)
print("Неотрицательная частота с максимальным спектральным весом:", max_freq)