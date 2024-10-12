#include <iostream>
#include <cmath>
using namespace std;
 
int main() {
    double x, sum = 0.0, term;
    int n, i = 1;  
    // Input x (in radians) and number of terms n
    cout << "Enter the value of x (in radians): ";
    cin >> x;
    cout << "Enter the number of terms n: ";
    cin >> n;
 
    // First term (sin(x)) calculation
    term = sin(x);
    sum += term;
 
    // Calculate the sum for the next (n - 1) terms
    while (i < n) {
        i++; 
        term = pow(sin(x), i);  
        sum += term;
    }
 
    cout << "The sum of the series is: " << sum << endl;
    return 0;
}
