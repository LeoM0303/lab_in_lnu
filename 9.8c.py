import numpy as np
from scipy.integrate import quad

# Фізичні константи
h = 6.626e-34       # Планка (Дж·с)
c = 3e8             # Швидкість світла (м/с)
k = 1.38e-23        # Больцмана (Дж/К)
sigma = 5.67032e-8  # Стефана-Больцмана (Вт/(м²·К⁴))

# Закон Планка
def planck_law(lambda_, T):
    numerator = 2 * h * c**2 / lambda_**5
    exponent = h * c / (lambda_ * k * T)
    # Чисельно стабільна форма для уникнення переповнення
    denominator = np.expm1(exponent)
    return numerator / denominator

# Основна частина коду
T = 3000  # Температура (наприклад, 3000 К)
print(f"Обчислення для температури T = {T} K")

# Інтегруємо закон Планка (обмежимо верхню межу, наприклад, до 10 мкм)
integral, _ = quad(planck_law, 1e-9, 1e-2, args=(T,))
P_sb = sigma * T**4  # Закон Стефана-Больцмана

# Результати
print(f"Потужність інтегрування закону Планка: {integral:.5e} Вт/м²")
print(f"Потужність закону Стефана-Больцмана: {P_sb:.5e} Вт/м²")

# Перевірка
if np.isclose(integral, P_sb, rtol=1e-3):
    print("Результати співпадають! Закон Стефана-Больцмана підтверджено.")
else:
    print("Результати не співпадають. Можливо, є помилка.")