#Calculate and print the sum of all the natural numbers below 1000 that are multiples of 3 or 5.

sum_of_multiples = 0
for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        sum_of_multiples += num
print(sum_of_multiples)
