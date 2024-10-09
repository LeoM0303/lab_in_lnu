#include <iostream>
#include <cmath>
 
double y(double x) {
    // Чисельник
    double numerator = pow((x - 10) * (x - 10), 1.0 / 5.0) * sin(x) + pow(4, 5 - x);
    // Знаменник
    double denominator = exp(-3 * x) / (pow(x, 3) + 10);
    // Функція y(x)
    return numerator / denominator;
}
 
int main() {
    double x = 1.0;
    const double step = 0.3;
    const double max_x = 6.0;
 
    std::cout.precision(6);
    std::cout << std::fixed;
 
    while (x <= max_x) {
        std::cout << "y(" << x << ") = " << y(x) << std::endl;
        x += step;
    }
 
    return 0;
}
