#include <iostream>
#include <locale>

int main() {
    setlocale(LC_ALL, "uk_UA");
    int K;
    std::cout << "Введіть день року (K від 1 до 365): ";
    std::cin >> K;

    // Перевірка на правильність введення
    if (K < 1 || K > 365) {
        std::cout << "Число K повинно бути в межах від 1 до 365.\n";
        return 1;
    }

    // Дано: 1 серпня - це 213-й день року і це субота (номер дня тижня - 6).
    const int august_1_day_of_year = 213;
    const int august_1_weekday = 6; // Субота

    // Обчислюємо різницю між введеним днем і 1 серпня
    int delta_days = K - august_1_day_of_year;

    // Визначаємо день тижня для K-го дня
    int weekday = (august_1_weekday + delta_days) % 7;
    
    // Якщо результат від'ємний, додаємо 7, щоб отримати коректний день тижня
    if (weekday <= 0) {
        weekday += 7;
    }

    // Виводимо результат
    std::cout << "День тижня для дня " << K << " року: ";

    switch (weekday) {
        case 1: std::cout << "Понеділок\n"; break;
        case 2: std::cout << "Вівторок\n"; break;
        case 3: std::cout << "Середа\n"; break;
        case 4: std::cout << "Четвер\n"; break;
        case 5: std::cout << "П'ятниця\n"; break;
        case 6: std::cout << "Субота\n"; break;
        case 7: std::cout << "Неділя\n"; break;
    }

    return 0;
}
