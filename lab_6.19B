#include <iostream>
using namespace std;
 
// Function to calculate factorial
double factorial(int num) {
    double fact = 1;
    for (int i = 1; i <= num; i++) {
        fact *= i;
    }
    return fact;
}
 
int main() {
    double m, x, sum = 1.0; // The first term is 1
    int n;
 
    cout << "Enter the value of m: ";
    cin >> m;
    cout << "Enter the value of x: ";
    cin >> x;
    cout << "Enter the number of terms n: ";
    cin >> n;

    double term = 1.0;
    for (int i = 1; i < n; i++) {
        term *= (m - (i - 1)) * x / i;  // Calculate the next term in the expansion
        sum += term;  // Add the term to the sum
    }
 
    cout << "The result of the binomial expansion is: " << sum << endl;
    return 0;
}
