#include <iostream>
#include <cmath>
#include <locale>

int main() {
    setlocale(LC_ALL, "uk_UA");
    double r, A, B, C, D;

    // Введення даних
    std::cout << "Введіть радіус круга (r): ";
    std::cin >> r;

    std::cout << "Введіть розміри першого прямокутника (A і B): ";
    std::cin >> A >> B;

    std::cout << "Введіть розміри другого прямокутника (C і D): ";
    std::cin >> C >> D;

    // Перевірка площі
    double circle_area = M_PI * r * r;
    double rectangles_area = A * B + C * D;

    if (rectangles_area > circle_area) {
        std::cout << "Неможливо вирізати пластини: сума площ перевищує площу круга.\n";
        return 0;
    }

    // Перевірка, чи вміщаються два прямокутники в круг
    double max_width = std::max(A, C);   // найбільша ширина між двома прямокутниками
    double max_height = std::max(B, D);  // найбільша висота між двома прямокутниками

    // Діаметр круга
    double diameter = 2 * r;

    if (max_width <= diameter && max_height <= diameter) {
        std::cout << "Можливо вирізати обидві пластини.\n";
    } else {
        std::cout << "Неможливо вирізати пластини: розміри прямокутників не вміщаються в круг.\n";
    }

    return 0;
}
