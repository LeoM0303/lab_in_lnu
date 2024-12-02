def f(x):
    return x / (x ** 2 + 1) ** 2

#методи прямокутників
def left_rectangle_method(a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        x = a + i * h
        result += f(x)
    return result * h


def right_rectangle_method(a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(1, n + 1):
        x = a + i * h
        result += f(x)
    return result * h


def middle_rectangle_method(a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        x = a + (i + 0.5) * h
        result += f(x)
    return result * h

#метод трапеції
def trapezoid_method(a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        result += f(x)
    return result * h

#метод Сміпсона
def simpson_method(a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * f(x)
        else:
            result += 4 * f(x)
    return result * h / 3


def main():
    print("Програма для обчислення визначеного інтеграла")
    a = 0  # Нижня межа інтегрування
    b = 1  # Верхня межа інтегрування
    n = int(input("Введіть кількість інтервалів (n): "))

    print("Оберіть метод обчислення:")
    print("1 - Метод лівих прямокутників")
    print("2 - Метод правих прямокутників")
    print("3 - Метод середніх прямокутників")
    print("4 - Метод трапецій")
    print("5 - Метод Сімпсона")

    method = int(input("Ваш вибір (1/2/3/4/5): "))

    if method == 1:
        result = left_rectangle_method(a, b, n)
        print(f"Результат обчислення методом лівих прямокутників: {result}")
    elif method == 2:
        result = right_rectangle_method(a, b, n)
        print(f"Результат обчислення методом правих прямокутників: {result}")
    elif method == 3:
        result = middle_rectangle_method(a, b, n)
        print(f"Результат обчислення методом середніх прямокутників: {result}")
    elif method == 4:
        result = trapezoid_method(a, b, n)
        print(f"Результат обчислення методом трапецій: {result}")
    elif method == 5:
        result = simpson_method(a, b, n)
        print(f"Результат обчислення методом Сімпсона: {result}")
    else:
        print("Невірний вибір методу")


if __name__ == "__main__":
    main()
