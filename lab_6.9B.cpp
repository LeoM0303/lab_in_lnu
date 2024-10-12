#include <iostream>
using namespace std;
 
int main() {
    int n;
    double sum = 0.0;
 
    // Input number of terms n
    cout << "Enter the number of terms: ";
    cin >> n;
 
 
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            sum += 1.0 / (2 * i + 1);  // Add for even terms
        } else {
            sum -= 1.0 / (2 * i + 1);  // Subtract for odd terms
        }
    }
 
    // Multiply by 4 to approximate pi
    double pi = sum * 4;
    cout << "Approximation of pi: " << pi << endl;
 
    return 0;
}
