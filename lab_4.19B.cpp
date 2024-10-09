#include <iostream>
using namespace std;
 
char get_new_direction(char current_direction, int command) {
    switch(command) {
        case 0:
            // продовжувати рух в тому ж напрямку
            return current_direction;
 
        case 1:
            // поворот ліворуч
            switch(current_direction) {
                case 'N': return 'W';
                case 'W': return 'S';
                case 'S': return 'E';
                case 'E': return 'N';
            }
 
        case -1:
            // поворот праворуч
            switch(current_direction) {
                case 'N': return 'E';
                case 'E': return 'S';
                case 'S': return 'W';
                case 'W': return 'N';
            }
 
        default:
            // Якщо команда не є 0, 1, або -1, то це неправильна команда
            cout << "False command" << endl;
            return current_direction;
    }
}
 
int main() {
    // Приклад вхідних даних
    char C = 'N'; // Початковий напрямок
    int N = -1;   // Команда
 
    // Отримати новий напрямок після виконання команди
    char new_direction = get_new_direction(C, N);
    cout << "New direction " << new_direction << endl;
 
    return 0;
}
