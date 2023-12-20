numbers = [100, 50, 75, 90, 55]
def get_largest_value(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest

largest = get_largest_value(numbers)
print( f"{largest} is the largest number in the list")
