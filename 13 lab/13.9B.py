import numpy as np
import matplotlib.pyplot as plt

def equation1(x):
    return np.cos(x + 0.5) - 2  # y = cos(x + 0.5) - 2

def equation2(y):
    return (np.sin(y) - 1) / 2  # x = (sin(y) - 1) / 2

x_values = np.linspace(-5, 5, 400)
y_values = np.linspace(-5, 5, 400)

# operation
y1 = equation1(x_values)
x2 = equation2(y_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y1, label='$\\cos(x + 0.5) - y = 2$', color='green')
plt.plot(x2, y_values, label='$\\sin(y) - 2x = 1$', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графіки системи нелінійних рівнянь')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()