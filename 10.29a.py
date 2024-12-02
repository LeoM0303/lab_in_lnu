import random
 
M = int(input("Введіть розмір матриці M: "))
 
 
A = [[random.randint(1, 10) for _ in range(M)] for _ in range(M)]
 
 
print("Згенерована матриця:")
for row in A:
    print(row)
 
 
sum_diag = 0
for i in range(M):
    sum_diag += A[i][i]
 
# Виведення результату
print("Сума елементів головної діагоналі:", sum_diag)
