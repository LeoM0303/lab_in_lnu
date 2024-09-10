#include <iostream>
#include <cmath>
#include <locale>

int main() {
    setlocale(LC_ALL, "uk_UA");
    double S;

    // Площа
    std::cout << "Введіть площу круга: ";
    std::cin >> S;

    // Перевірка на правильність даних
    if (S <= 0) {
        std::cout << "Памʼятай, площа має бути додатнім числом.\n";
        return 1; // Завершення програми з кодом помилки
    }

    // Обчислюємо радіус
    double r = sqrt(S / M_PI);

    // Обчислюємо діаметр
    double D = r * 2;

    // Обчислюємо довжину кола
    double L = 2 * M_PI * r;

    // Вивід інформації
    std::cout << "Діаметр кола: " << D << "\n";
    std::cout << "Довжина кола: " << L << "\n";

    return 0; // Успішне завершення програми
}
