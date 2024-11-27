#include <iostream>
#include <cmath>

using namespace std;

bool is_prime(int num) {
    if (num <= 1) {
        return false;
    }
    if (num <= 3) {
        return true;
    }
    if (num % 2 == 0 || num % 3 == 0) {
        return false;
    }

    for (int i = 5; i * i <= num; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int count = 0, num = 2;

    while (count < 10001) {
        if (is_prime(num)) {
            count++;
        }
        num++;
    }

    cout << "The 10001st prime number is: " << num - 1 << endl;

    return 0;
}