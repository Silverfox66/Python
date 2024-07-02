def add_without_addition(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b      
        b = carry << 1

    return a

x = int(input("Please type in the first number you would like to add: "))
y = int(input("Please type in the second number you would like to add: "))
result = add_without_addition(x, y)
print(f"The sum of {x} and {y} is: {result}")
