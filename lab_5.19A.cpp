#include <iostream>
#include <cmath>
 
double y(double x) {
    double numerator = pow(pow(x - 10, 2), 1.0 / 5.0) * sin(x) + pow(4, 5 - x);
    double denominator = exp(-3 * x) / (pow(x, 3) + 10);
    return numerator / denominator;
}
 
int main() {
    double x = 1.0;
    const double step = 0.3;
    const double max_x = 6.0;
 
    std::cout.precision(4);
    std::cout << std::fixed;
 
    while (x <= max_x) {
        std::cout << "y(" << x << ") = " << y(x) << std::endl;
        x += step;
    }
 
    return 0;
}
