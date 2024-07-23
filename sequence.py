def product(n):
    if n == 1:
        return 1
    else:
        return n * product(n - 1)

print(product(5))




def sum_sequence(limit):
    n = 1
    total_sum = 0
    while True:
        term = 1 + (n-1)*n
        if term >= limit:
            break
        total_sum += term
        n += 1
    return total_sum

limit = 40000000
result = sum_sequence(limit)
print("The sum of all terms less than 40,000,000 is:", result)