import numpy as np
import matplotlib.pyplot as plt
tmax = 1
dt = 0.0025
t = np.arange(0, tmax, dt)
freq = 10
wave = np.sin(2 * np.pi * freq * t) + np.sin(2 * np.pi * 2 * freq * t)
noise = 2 * (2 * np.random.sample(t.size) - 1)
plt.plot(t, wave + noise, lw = 1, color = 'tab:blue', label = 'noisy')
plt.xlim(0, 0.5)
plt.xlabel('time', fontsize = 14)
plt.ylabel('Amplitude', fontsize = 14)
plt.show()
