#include <iostream>
#include <locale>

int main(){
    setlocale(LC_ALL, "uk_UA");
    std::cout << 1 << "\n" << 2 << "\n" << 3 << "\n" << 4 << "\n";

    return 0;
}
