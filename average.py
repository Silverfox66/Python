#Finding average of a list of numbers

def get_average(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    average = sum / len(numbers)
    return average

numbers = [100, 50, 75, 90, 55]
average = get_average(numbers)
print(average)