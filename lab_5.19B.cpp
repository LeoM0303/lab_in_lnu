#include <iostream>
#include <cmath>  
 
// Function to calculate f(x)
double f(double x) {
    return x / 2.0 - sin(x);
}
 
int main() {
    double start = 0, end = 10; 
    double step = 0.01;         
    int sign_changes = 0;      
 
    // Initial value of the function
    double previous_value = f(start);
    double current_value;
 
    // Checking the range for sign changes
    for (double x = start + step; x <= end; x += step) {
        current_value = f(x);
        // Check if the function has changed sign
        if (previous_value * current_value < 0) {
            sign_changes++;
            std::cout << "Sign change at x = " << x << ", f(x) = " << current_value << std::endl;
        }
        previous_value = current_value;
    }
 
    std::cout << "Total sign changes: " << sign_changes << std::endl;
 
    return 0;
}
