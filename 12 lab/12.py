import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def equations(p):
    x, y = p
    return (np.cos(x + 0.5) - y - 2, np.sin(y) - 2 * x - 1)


# Графічний метод для знаходження початкового наближення
def find_initial_guess():
    x = np.linspace(-2, 2, 400)

    # Перше рівняння: y = cos(x + 0.5) - 2
    y1 = np.cos(x + 0.5) - 2

    # Друге рівняння: y = arcsin(2x + 1) з обробкою помилок
    y2 = np.zeros_like(x)
    for i, val in enumerate(2 * x + 1):
        if -1 <= val <= 1:
            y2[i] = np.arcsin(val)
        else:
            y2[i] = np.nan

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='y = cos(x + 0.5) - 2')
    plt.plot(x, y2, label='y = arcsin(2x + 1)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Графічний метод знаходження початкового наближення')
    plt.grid()
    plt.legend()
    plt.show()

    # Знаходимо точку перетину графіків
    initial_guess = fsolve(equations, (-1, -1))
    print(f"Початкове наближення (графічний метод): x = {initial_guess[0]:.4f}, y = {initial_guess[1]:.4f}")
    return initial_guess


# Метод простих ітерацій
def simple_iteration_method(x0, y0, epsilon=1e-6, max_iter=100):
    print("\nМетод простих ітерацій:")
    x, y = x0, y0
    for i in range(max_iter):
        x_new = (np.sin(y) - 1) / 2
        y_new = np.cos(x + 0.5) - 2

        # Перевірка на збіжність
        if abs(x_new - x) < epsilon and abs(y_new - y) < epsilon:
            print(f"Розв'язок знайдено за {i + 1} ітерацій: x = {x_new:.6f}, y = {y_new:.6f}")
            return x_new, y_new, i + 1

        x, y = x_new, y_new

    print(f"Досягнуто максимальну кількість ітерацій ({max_iter}). Найкращий результат: x = {x:.6f}, y = {y:.6f}")
    return x, y, max_iter


# Метод Ньютона
def newton_method(x0, y0, epsilon=1e-6, max_iter=100):
    print("\nМетод Ньютона:")
    x, y = x0, y0
    for i in range(max_iter):
        f1 = np.cos(x + 0.5) - y - 2
        f2 = np.sin(y) - 2 * x - 1

        J11 = -np.sin(x + 0.5)  # df1/dx
        J12 = -1  # df1/dy
        J21 = -2  # df2/dx
        J22 = np.cos(y)  # df2/dy

        det = J11 * J22 - J12 * J21

        inv_J11 = J22 / det
        inv_J12 = -J12 / det
        inv_J21 = -J21 / det
        inv_J22 = J11 / det

        dx = inv_J11 * f1 + inv_J12 * f2
        dy = inv_J21 * f1 + inv_J22 * f2

        x_new = x - dx
        y_new = y - dy

        # Перевірка на збіжність
        if abs(x_new - x) < epsilon and abs(y_new - y) < epsilon:
            print(f"Розв'язок знайдено за {i + 1} ітерацій: x = {x_new:.6f}, y = {y_new:.6f}")
            return x_new, y_new, i + 1

        x, y = x_new, y_new

    print(f"Досягнуто максимальну кількість ітерацій ({max_iter}). Найкращий результат: x = {x:.6f}, y = {y:.6f}")
    return x, y, max_iter


if __name__ == "__main__":
    # Знаходимо початкове наближення графічним методом
    initial_guess = find_initial_guess()
    x0, y0 = initial_guess

    # Точність
    epsilon = 1e-6

    # Виклик методу простих ітерацій
    x_si, y_si, iter_si = simple_iteration_method(x0, y0, epsilon)

    # Виклик методу Ньютона
    x_n, y_n, iter_n = newton_method(x0, y0, epsilon)

    # Порівняння методів
    print("\nПорівняння методів:")
    print(f"Метод простих ітерацій: {iter_si} ітерацій, розв'язок: x = {x_si:.6f}, y = {y_si:.6f}")
    print(f"Метод Ньютона: {iter_n} ітерацій, розв'язок: x = {x_n:.6f}, y = {y_n:.6f}")
    print(f"Різниця в ітераціях: {iter_si - iter_n}")