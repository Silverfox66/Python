#include <iostream>
#include <cmath>

using namespace std;

bool is_prime(long long n) {
    if (n <= 1) {
        return false;
    }
    if (n <= 3) {
        return true;
    }
    if (n % 2 == 0 || n % 3 == 0) {
        return false;
    }

    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }

    return true;
}

long long largest_prime_factor(long long n) {
    long long largest_prime = 2;

    while (n % 2 == 0) {
        n /= 2;
    }

    for (long long i = 3; i <= sqrt(n); i += 2) {
        while (n % i == 0) {
            largest_prime = i;
            n /= i;
        }
    }

    if (n > 2) {
        largest_prime = n;
    }

    return largest_prime;
}

int main() {
    long long n = 600851475143;
    long long largest_prime = largest_prime_factor(n);
    cout << "The largest prime factor of " << n << " is " << largest_prime << endl;
    return 0;
}