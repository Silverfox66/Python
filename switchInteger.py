def swap_numbers_arithmetic(a, b):
    print(f"Original a: {a}, b: {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"Swapped a: {a}, b: {b}")
    return a, b

a = -5
b = 10
a, b = swap_numbers_arithmetic(a, b)


def swap_numbers_xor(a, b):
    print(f"Original a: {a}, b: {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"Swapped a: {a}, b: {b}")
    return a, b


a = -5
b = 10
a, b = swap_numbers_xor(a, b)

