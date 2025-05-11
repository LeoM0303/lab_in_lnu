import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def f(x):
    return abs(0.5 - x)


def calculate_coefficients(N):
    a0 = 2 * quad(f, 0, 1)[0]

    a = []
    b = []
    for n in range(1, N + 1):
        a_n = 2 * quad(lambda x: f(x) * np.cos(2 * np.pi * n * x), 0, 1)[0]
        b_n = 2 * quad(lambda x: f(x) * np.sin(2 * np.pi * n * x), 0, 1)[0]

        a.append(a_n)
        b.append(b_n)

    return a0, a, b

def approximate(x, a0, a, b):
    result = a0 / 2
    for n in range(1, len(a) + 1):
        result += a[n - 1] * np.cos(2 * np.pi * n * x) + b[n - 1] * np.sin(2 * np.pi * n * x)
    return result


#main part
if __name__ == "__main__":
    N = 10
    a0, a, b = calculate_coefficients(N)

    x = np.linspace(0, 1, 500)
    y_exact = f(x)
    y_approx = [approximate(xi, a0, a, b) for xi in x]

    plt.figure(figsize=(10, 5))
    plt.plot(x, y_exact, label='Точна функція')
    plt.plot(x, y_approx, label=f'Наближення (N={N})')
    plt.title('Порівняння точної функції та наближення')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.show()