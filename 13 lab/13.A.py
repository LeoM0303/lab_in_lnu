import numpy as np
import matplotlib.pyplot as plt

def maxwell_distribution(v, m0, T):
    k = 1.38e-23  # Постійна Больцмана, Дж/К
    factor = 4 * np.pi * (m0 / (2 * np.pi * k * T)) ** (3/2)
    return factor * v**2 * np.exp(-m0 * v**2 / (2 * k * T))

#N2
m0 = 4.65e-26
T = 300

#speed
v = np.linspace(0, 2000, 500)
f_v = maxwell_distribution(v, m0, T)

# build graf
plt.figure(figsize=(8, 6))
plt.plot(v, f_v, label=r'$f(v)$, функція Максвелла', color='blue')
plt.xlabel("Швидкість, м/с")
plt.ylabel("Ймовірність")
plt.title("Розподіл Максвелла за швидкостями")
plt.legend()
plt.grid()
plt.show()
