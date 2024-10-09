#include <iostream>
#include <cmath> 
 
using namespace std;
 
int main() {
    // Цикл для перших 20 елементів послідовності
    for (int i = 1; i <= 20; ++i) {
        // Обчислення значення послідовності 3 - 3 * sin(i^2)
        double value = 3 - 3 * sin(i * i);
 
        // Виводимо тільки від'ємні елементи
        if (value < 0) {
            cout << "Element " << i << ": " << value << endl;
        }
    }
 
    return 0;
}
