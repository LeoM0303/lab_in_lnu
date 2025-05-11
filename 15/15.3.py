import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([4.0, 3.5, 5.0, 6.0, 3.4])

poly = lagrange(x_data, y_data)

x_interp = np.linspace(min(x_data), max(x_data), 100)
y_interp = poly(x_interp)

plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, color='red', label='Експериментальні точки', zorder=5)
plt.plot(x_interp, y_interp, label=f'Інтерполюючий поліном (степінь {len(x_data)-1})', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік експериментальних точок та інтерполюючого полінома')
plt.legend()
plt.grid(True)
plt.show()

print("Коефіцієнти полінома:", np.poly1d(poly).coeffs)