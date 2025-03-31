import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def equations(vars):
    x, y = vars
    eq1 = np.cos(x + 0.5) - y - 2
    eq2 = np.sin(y) - 2*x - 1
    return [eq1, eq2]

initial_guess = [0, -2]

solution = fsolve(equations, initial_guess)
x_sol, y_sol = solution

print(f"Розв’язок системи: x ≈ {x_sol:.3f}, y ≈ {y_sol:.3f}")

# Побудова графіків
x_values = np.linspace(-2, 2, 400)
y1_values = np.cos(x_values + 0.5) - 2
y2_values = np.arcsin(2 * x_values + 1)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y1_values, label=r'$y = \cos(x + 0.5) - 2$', color='blue')
plt.plot(x_values, y2_values, label=r'$y = \arcsin(2x + 1)$', color='red')
plt.scatter(x_sol, y_sol, color='black', zorder=3, label='Розв’язок')

# Додавання підписів
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title("Графічний розв’язок системи рівнянь")
plt.grid()
plt.show()
