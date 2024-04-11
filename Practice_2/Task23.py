
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