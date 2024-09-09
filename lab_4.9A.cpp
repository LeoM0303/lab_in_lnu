#include <iostream>

int main() {
    double a, b, c;

    // Введення трьох чисел
    std::cout << "Введіть три числа: ";
    std::cin >> a >> b >> c;

    double sum;

    // Шукаємо два найбільші числа
    if (a <= b && a <= c) {
        // Якщо a найменше, то беремо b і c
        sum = b + c;
    } else if (b <= a && b <= c) {
        // Якщо b найменше, то беремо a і c
        sum = a + c;
    } else {
        // Якщо c найменше, то беремо a і b
        sum = a + b;
    }

    // Виведення результату
    std::cout << "Сума двох найбільших чисел: " << sum << std::endl;

    return 0;
}
