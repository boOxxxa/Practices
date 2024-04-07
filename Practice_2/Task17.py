import numpy as np
import matplotlib.pyplot as plt
a, b = 0, 0


def gauss(z, sigma, x0, y0):
    x, y = z
    return np.exp(-((x-x0)**2 + (y-y0)**2) / sigma**2)

neg_gauss = lambda z, sigma, x0, y0: -gauss(z, sigma, x0, y0)

x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
X, Y = np.meshgrid(x, y)
Z = gauss((X, Y), 100, 0, 0)

fig, ax = plt.subplots(1, 1, figsize=(6, 6))
contours = plt.contour(X, Y, Z, 15, colors="black", linewidths=2, linestyles='-.')
plt.clabel(contours, inline=True, fontsize=16)
contours = plt.contourf(X, Y, Z, 200, cmap=plt.cm.hsv, alpha=0.7)
plt.xlabel("Ox")
plt.ylabel("Oy")

plt.show()
