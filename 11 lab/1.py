import numpy as np

A = np.array([[8, 0, -2],
              [1, -3, 7],
              [0, -2, -4]])

B = np.array([[-3, 1, -7],
              [1, 3, -8],
              [0, 1, -4]])

AB = np.dot(A, B)
BA = np.dot(B, A)
result = AB - BA

print("AB - BA =\n", result)