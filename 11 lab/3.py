import numpy as np


A = np.array([[2, 3, 4],
              [1, 2, 1],
              [5, 1, 1]], dtype=float)

# Вільні члени
b = np.array([6, 7, 7], dtype=float)

# Розширена матриця
Ab = np.hstack([A, b.reshape(-1, 1)])

# Метод Гауса (прямий хід)
n = len(b)
for i in range(n):
    # Робимо діагональний елемент рівним 1
    Ab[i] = Ab[i] / Ab[i, i]

    # Зануляємо всі елементи під діагоналлю
    for j in range(i + 1, n):
        Ab[j] = Ab[j] - Ab[i] * Ab[j, i]

# Зворотний хід
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = Ab[i, -1] - np.sum(Ab[i, i + 1:n] * x[i + 1:n])

# Вивід розв'язку
print("Розв'язок системи:", x)
