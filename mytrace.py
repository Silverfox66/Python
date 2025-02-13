#Define a function that subtracts two numbers if the first is greater, otherwise it adds them, then uses this function to perform calculations and print the results.

def my_function(x, y):
    if(x > y):
        return x - y
    else:
        return x + y

x = 5
y = 3

z = my_function(x, y)

x = 2
y = x + z

print(z)
print(y)
print(z)
#Play with debug