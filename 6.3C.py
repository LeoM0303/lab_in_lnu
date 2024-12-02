def count_squares_no_mult_div(A, B, C):
    rows = 0
    remaining_height = A
    #кількість рядів квадратів
    while remaining_height >= C:
        rows += 1
        remaining_height -= C
 
    cols = 0
    remaining_width = B
 
    #кількість квадратів у кожному ряду
    while remaining_width >= C:
        cols += 1
        remaining_width -= C
 
    #кількість квадратів через підсумовування
    total_squares = 0
    for _ in range(rows):
        total_squares += cols
 
    return total_squares
 
 
A = int(input("Введіть довжину прямокутника (A): "))
B = int(input("Введіть ширину прямокутника (B): "))
C = int(input("Введіть сторону квадрата (C): "))
 
result = count_squares_no_mult_div(A, B, C)
print("Максимальна кількість квадратів:", result)
