import random
 
def main():
    # Введення розмірів матриці
    m = int(input("Введіть кількість рядків (M): "))
    n = int(input("Введіть кількість стовпців (N): "))
 
    # Генерація матриці випадковими числами
    matrix = [[random.randint(1, 10) for _ in range(n)] for _ in range(m)]
 
    # Виведення початкової матриці
    print("Початкова матриця:")
    for row in matrix:
        print(row)
 
    # Введення номера стовпця K
    k = int(input(f"Введіть номер стовпця K (1 < K < {n}): ")) - 1
 
    if 1 <= k < n:
        for i in range(m):
            matrix[i].insert(k + 1, 1)
 
        # Виведення оновленої матриці
        print("Оновлена матриця:")
        for row in matrix:
            print(row)
    else:
        print("Помилка: значення K повинно задовольняти умову 1 < K < N")
 
if __name__ == "__main__":
    main()
