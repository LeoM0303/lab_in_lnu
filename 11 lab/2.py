import numpy as np

A = np.array([[4, -6, -1],
              [3, 2, -1],
              [-4, 3, 0]])

B = np.array([[0, 1, -3],
              [3, -2, 5],
              [6, 0, 1]])

# Обчислення AB
AB = np.dot(A, B)
print("AB =\n", AB)

# Обчислення (AB)^T
AB_T = np.transpose(AB)
print("(AB)^T =\n", AB_T)

# Обчислення B^T
BT = np.transpose(B)
print("B^T =\n", BT)

# Обчислення A^T
AT = np.transpose(A)
print("A^T =\n", AT)

# Обчислення B^T A^T
BT_AT = np.dot(BT, AT)
print("B^T A^T =\n", BT_AT)

# Обчислення (AB)^T - B^T A^T
result = AB_T - BT_AT
print("(AB)^T - B^T A^T =\n", result)