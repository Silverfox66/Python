#Solving for exponents
def exponent_func(base, exp):
    if(base == 0 and exp == 0):
        return "UNDEFINED"
    if(exp == 0):
        return 1
    if(base == 0):
        return 0

# l = [33, 500, 32, 650, 78]

#largest = l[0]
#for x in l:
#     if(x > largest):
#          largest = x
#print("largest:", largest)

#numbers = [33, 500, 32, 650, 78]
#largest_number = max(numbers)
#print("The largest number is:", largest_number)

# l = [33, 500, 32, 650, 78]

# largest = l[0]
# index = 0
# while(index > largest):
#     if(l[index] > largest):
#          largest = l[index]
#     index += 1
# print("largest:", largest)

# sum = 0
# for x in l:
#     sum += x
# print("sum:", sum)

# product = 1
# for x in l:
#     sum *= x
# print("product:", sum)

# average = sum / len(l)
# print("average:", average)

base = int(input("Please type in your base number: "))
exponent = int(input("Please type in your exponent: "))
result = base ** exponent
print(result)