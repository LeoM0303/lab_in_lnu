

import math
 
def equation(x):

    return math.sqrt(x) + math.exp(x) + x**3 + x - 62.8
 
def bisection_method(func, a, b, tol=1e-6):

    if func(a) * func(b) >= 0:

        raise ValueError("Функція повинна мати різні знаки на кінцях інтервалу!")

    while (b - a) / 2 > tol:

        c = (a + b) / 2  # Середина інтервалу

        if func(c) == 0:  

            return c

        elif func(a) * func(c) < 0:

            b = c  # Корінь знаходиться в лівій половині

        else:

            a = c  # Корінь знаходиться в правій половині

    return (a + b) / 2
 
 
a = 3  # Ліва межа інтервалу

b = 5  # Права межа інтервалу

tolerance = 1e-6  # Точність
 
try:

    root = bisection_method(equation, a, b, tol=tolerance)

    print(f"Знайдений корінь рівняння: x = {root:.6f}")

    print(f"Перевірка: f(x) = {equation(root):.6e}")

except ValueError as e:

    print(e)

 
