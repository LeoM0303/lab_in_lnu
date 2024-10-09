#include <iostream>
#include <iomanip>
#include <locale>
 
int main() {
    setlocale(LC_ALL, "uk_UA");
    // Заголовок таблиці
    std::cout << std::setw(10) << "см^3" << std::setw(15) << "м^3" << std::setw(15) << "літри" << std::endl;
    for (int cm3 = 1000; cm3 <= 2000; cm3 += 50) {
        // Перетворення
        double m3 = cm3 * 0.000001;  // см³ -> м³
        double liters = cm3 * 0.001; // см³ -> літри
        // Виведення значень у вигляді таблиці
        std::cout << std::setw(10) << cm3 << std::setw(15) << std::fixed << std::setprecision(6) << m3 
<< std::setw(15) << liters << std::endl;
    }
 
    return 0;
}
