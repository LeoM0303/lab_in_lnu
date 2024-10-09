#include <iostream>
#include <cmath> 
 
using namespace std;
 
double y(double x) {
    return (1 / cbrt(34 + 6 * x)) - (exp(-3 * x) / (pow(x, 3) + 10));
}
 
int main() {
    double x = 0.0;
    double step = 0.04;  // Крок
    double max_x = 1.5;  // Максимальне значення x
 
    // Виведення результатів для кожного значення x
    while (x <= max_x) {
        cout << "x = " << x << ", y(x) = " << y(x) << endl;
        x += step;
    }
 
    return 0;
}
