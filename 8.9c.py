def equation(x):

    return x**4 - 2 * x**3 - 3.74 * x**2 + 8.18 * x - 3.48
 
# метод половинного ділення

def bisection(a, b, epsilon):

    if equation(a) * equation(b) >= 0:

        print("На даному інтервалі кореня немає або їх більше одного.")

        return None
 
    while (b - a) / 2 > epsilon:

        c = (a + b) / 2  

        if equation(c) == 0:  # якщо знайдено точний корінь

            return c

        elif equation(a) * equation(c) < 0:

            b = c 

        else:

            a = c
 
    return (a + b) / 2  

 
def main():

    #вивід рівняння

    print("Рівняння: x^4 - 2x^3 - 3.74x^2 + 8.18x - 3.48 = 0")

    #введення значенть

    a = float(input("Введіть ліву межу інтервалу (a): "))

    b = float(input("Введіть праву межу інтервалу (b): "))

    # точність

    epsilon = float(input("Введіть точність (наприклад, 0.0001): "))
 
    # метод половинного ділення

    root = bisection(a, b, epsilon)
 
    if root is not None:

        print(f"Наближений корінь рівняння: x = {root:.6f}")

        print(f"Перевірка: f(x) = {equation(root):.6e}")

    else:

        print("Не вдалося знайти корінь на заданому інтервалі.")
 
main()

 
