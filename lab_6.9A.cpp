#include <iostream>
#include <cmath>
using namespace std;
 
int main() {
    double x, epsilon, sum = 0.0, term;
    int n = 1;  
    
    // Input x (in radians) and epsilon
    cout << "Enter the value of x (in radians): ";
    cin >> x;
    cout << "Enter the precision epsilon: ";
    cin >> epsilon;
 
    // First term (sin(x)) calculation
    term = sin(x);
    sum += term;
 
    // Continue adding terms until the term is smaller than epsilon
    while (fabs(term) > epsilon) {
        n++;  // Increment the power of sin(x)
        term = pow(sin(x), n);  // Calculate sin^n(x)
        sum += term;
    }
 
 
    cout << "The sum of the series is: " << sum << endl;
    return 0;
}
