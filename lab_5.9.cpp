#include <iostream>
#include <cmath>
#include <iomanip>

// Функція для обчислення y(x)
double y(double x) {
    if (x == 0) { // Уникнення ділення на нуль
        return std::numeric_limits<double>::quiet_NaN(); // Повернення NaN
    }
    return 1.0 / (std::cbrt(34 + 6 * x) - (exp(-3 * x) / (pow(x, 3) + 10)));
}

int main() {
    std::cout << std::fixed << std::setprecision(3); // Встановлення точності виводу до 3 десяткових знаків
    for (double x = 0; x <= 0.52; x += 0.04) {
        double result = y(x);
        std::cout << "y(" << x << ") = ";
        if (std::isnan(result)) { // Перевірка, чи результат є NaN
            std::cout << "невизначено";
        } else {
            std::cout << result;
        }
        std::cout << std::endl;
    }
    return 0;
}
