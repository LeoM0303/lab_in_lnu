#include <iostream>
#include <cmath> // Підключення бібліотеки cmath для функцій sqrt, pow та sin
#include <locale>

int main() {
    setlocale(LC_ALL, "ua_UK");
    double x, y, z; // Змінні x, y та z мають бути визначені з деякими значеннями
    
    x = 1.0;
    y = 2.0;
    z = 3.0;

    // Обчислення a
    double a = sqrt(abs(x) + 1 / (sqrt(3 / (2 + y))));

    // Обчислення b
    double b = sin(pow(log(z / 8), 2));

    // Виведення результатів
    std::cout << "a = " << a << std::endl;
    std::cout << "b = " << b << std::endl;

    return 0;
}
