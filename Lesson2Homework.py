# Exercise 3: Finding the Largest Value
# 1. Create a list of the following numbers: 100, 50, 75, 90, 55. Call the list numbers.
# 2. Create a function called get_largest_value(numbers), with parameter numbers.
#         a. Inside the function, find the largest number in numbers and store the value in a variable called largest. (Hint, use a 
#            for loop with an if statement inside the for loop. Compare the current number in the list to the current value of 
#            largest, and update largest if needed).
#        b. Return largest.
# 3. Call the function, passing numbers as an input to the function. Store the return value of the function in a variable 
#         called largest.
# 4. Print the largest.
numbers = [100, 50, 75, 90, 55]
def get_largest_value(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest

largest_num = get_largest_value(numbers)
print( f"{largest_num} is the largest number in the list!")
#How to use debug in VS Code
# Parameters or Arguments?