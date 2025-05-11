import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Зчитування даних з файлу
data = np.loadtxt('data.txt')
x = data[:, 0]
y1 = data[:, 1]
y2 = data[:, 2]

# Апроксимація поліномами різних степенів
degrees = [1, 2, 6]  # Степені поліномів для апроксимації

plt.figure(figsize=(12, 8))

# Графік для першого набору даних (y1)
plt.subplot(2, 1, 1)
plt.scatter(x, y1, facecolors='none', edgecolors='r', label='Експериментальні точки (y1)', s=100)
for degree in degrees:
    coeffs = np.polyfit(x, y1, degree)
    poly = np.poly1d(coeffs)
    x_fit = np.linspace(min(x), max(x), 100)
    plt.plot(x_fit, poly(x_fit), label=f'Апроксимація (степінь {degree})')
plt.xlabel('x')
plt.ylabel('y1')
plt.title('Апроксимація першого набору даних')
plt.legend()
plt.grid(True)

# Графік для другого набору даних (y2)
plt.subplot(2, 1, 2)
plt.scatter(x, y2, facecolors='none', edgecolors='b', label='Експериментальні точки (y2)', s=100)
for degree in degrees:
    coeffs = np.polyfit(x, y2, degree)
    poly = np.poly1d(coeffs)
    x_fit = np.linspace(min(x), max(x), 100)
    plt.plot(x_fit, poly(x_fit), label=f'Апроксимація (степінь {degree})')
plt.xlabel('x')
plt.ylabel('y2')
plt.title('Апроксимація другого набору даних')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()