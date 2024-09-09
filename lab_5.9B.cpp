#include <iostream>
#include <iomanip>

int main() {
    std::cout << std::fixed << std::setprecision(6);  // Встановлюємо точність виводу до 6 десяткових знаків
    std::cout << "См³\t\tМ³\t\tЛітри\n";  // Заголовки колонок

    for (int cm3 = 1000; cm3 <= 2000; cm3 += 50) {
        double m3 = cm3 * 1e-6;     // Перетворення в кубічні метри
        double liters = cm3 * 0.001;  // Перетворення в літри
        std::cout << cm3 << "\t\t" << m3 << "\t\t" << liters << "\n";  // Виведення результатів
    }

    return 0;
}
