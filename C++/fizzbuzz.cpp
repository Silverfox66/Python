#include <iostream>

int main() {
    int n = 0;
    std::cin >> n;

    if (n % 3 == 0) {
        std::cout << "fizz";
    }
    if (n % 5 == 0) {
        std::cout << "buzz";
    }


    return 0;
}
