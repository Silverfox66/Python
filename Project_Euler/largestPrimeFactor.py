def largest_prime_factor(n):
    i = 2
    while n % i == 0:
        n //= i
    i = 3
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 2
    return n

n = 600851475143
print(largest_prime_factor(n))
